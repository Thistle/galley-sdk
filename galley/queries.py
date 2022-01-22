import logging
from typing import Any, Dict, List, Optional

from sgqlc.operation import Operation
from sgqlc.types import ArgDict, Field, Type

from galley.common import make_request_to_galley, validate_response_data
from galley.enums import MenuCategoryEnum
from galley.types import (FilterInput, Menu, MenuFilterInput,
                          PaginationOptions, Recipe, RecipeConnection,
                          RecipeConnectionFilter)

logger = logging.getLogger(__name__)

DEFAULT_PAGE_SIZE = 25


class Viewer(Type):
    recipeConnection = Field(
        RecipeConnection,
        args=(ArgDict({
            'filters': RecipeConnectionFilter,
            'paginationOptions': PaginationOptions
        }))
    )
    recipes = Field(Recipe, args=(ArgDict({'where': FilterInput})))
    recipe = Field(Recipe, args=(ArgDict({'id': str})))
    menus = Field(Menu, args=(ArgDict({'where': MenuFilterInput})))


# This is graphql root for querying data according to sgqlc lib. So this class name has to be Query.
class Query(Type):
    viewer = Field(Viewer)

    @staticmethod
    def recipe_data_struct() -> Dict:
        return {
            'data': {
                'viewer': {
                    'recipes': [{
                        'id': str,
                        'externalName': str,
                        'instructions': Any,
                        'notes': Any,
                        'description': Any
                    }]
                }
            }
        }


# RECIPE QUERIES

def recipe_connection_query(recipe_ids: List[str], page_size: int = DEFAULT_PAGE_SIZE, start_index: int = 0) -> Optional[Operation]:
    query = Operation(Query)
    query.viewer.recipeConnection(
        filters=RecipeConnectionFilter(id=recipe_ids),
        paginationOptions=PaginationOptions(first=page_size, startIndex=start_index)
    )
    query.viewer.recipeConnection.edges()
    query.viewer.recipeConnection.pageInfo()
    query.viewer.recipeConnection.totalCount

    query.viewer.recipeConnection.edges.node.__fields__(
        'id', 'externalName', 'name', 'notes', 'description', 'media', 'categoryValues', 'reconciledNutritionals', 'recipeItems',
    )
    query.viewer.recipeConnection.edges.node.media.__fields__('altText', 'caption', 'sourceUrl')
    query.viewer.recipeConnection.edges.node.recipeItems.__fields__('ingredient', 'subRecipe', 'preparations')
    query.viewer.recipeConnection.edges.node.recipeItems.ingredient.__fields__('externalName', 'categoryValues')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents(levels=[1]).__fields__('id', 'quantityUnitValues', 'recipeItem')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.quantityUnitValues.__fields__('unit', 'value')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.quantityUnitValues.unit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.__fields__(
        'preparations', 'ingredient', 'subRecipe', 'subRecipeId', 'quantity', 'unit'
    )
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.preparations.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.ingredient.__fields__('categoryValues', 'externalName')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.ingredient.categoryValues.__fields__('id', 'name', 'category')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.subRecipe.__fields__(
        'id', 'allIngredients', 'externalName', 'name', 'reconciledNutritionals', 'nutritionalsQuantity', 'nutritionalsUnit'
    )
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.unit.__fields__('id', 'name')

    return query


def get_raw_recipes_data(recipe_ids: List[str]) -> Optional[List[Dict]]:
    has_next_page = True
    page_size = DEFAULT_PAGE_SIZE
    start_index = 0

    raw_recipes_data = []

    if recipe_ids is None:
        return []

    while has_next_page:
        query = recipe_connection_query(recipe_ids=recipe_ids, page_size=page_size, start_index=start_index)
        raw_data = make_request_to_galley(op=query, variables={'recipeId': recipe_ids or []})
        validated_data = validate_response_data(raw_data, 'recipeConnection')

        if not validated_data:
            return None

        edges = validated_data.get('edges', [])

        for edge in edges:
            recipe = edge.get('node', {})
            if recipe:
                raw_recipes_data.append(recipe)

        page_info = validated_data.get('pageInfo', {})
        start_index = page_info.get('endIndex')
        has_next_page = page_info.get('hasNextPage', False)

    return raw_recipes_data


def get_menu_query(dates: List[str]) -> Optional[List[Dict]]:
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates)).__fields__(
        'id', 'name', 'date', 'location', 'categoryValues', 'menuItems'
    )
    query.viewer.menus.menuItems.__fields__('id', 'recipeId', 'categoryValues', 'recipe')
    query.viewer.menus.menuItems.recipe.__fields__('externalName', 'recipeItems', 'categoryValues')
    query.viewer.menus.menuItems.recipe.recipeItems.__fields__('subRecipeId', 'preparations')
    query.viewer.menus.menuItems.recipe.recipeItems.preparations.__fields__('id', 'name')
    return query


def get_raw_menu_data(dates: List[str],
                      location_name: str,
                      menu_type: str
                      ) -> Optional[List[Dict]]:
    """
    Returns a list of dictionaries containing the menu data for the week.
    if there is no menu data for the week, returns None.

    :param date: The date for which the menu is to be fetched. In the form
    :param location_name: The name of the location for which the menu is to be
    fetched. ex. "Vacaville"
    :param menu_type: The type of menu to be fetched. ex. "production",
    "development"
    """
    query = get_menu_query(dates=dates)  # type: Operation
    validated_response_data = validate_response_data(
            make_request_to_galley(
                op=query.__to_graphql__(auto_select_depth=3),
                variables={'date': dates}),
            'menus')

    response = []
    if validated_response_data:
        for menu in validated_response_data:
            if menu['location']['name'] == location_name:
                categoryValues = menu['categoryValues']
                for categoryValue in categoryValues:
                    if (categoryValue['category']['id'] == MenuCategoryEnum.MENU_TYPE.value and \
                        categoryValue['name'] == menu_type):
                        response.append(menu)
                    else:
                        continue
    return response
