import logging
from re import template
from typing import Any, Dict, Iterable, List, Optional

from sgqlc.operation import Operation
from sgqlc.types import ArgDict, Field, Type

from galley.common import make_request_to_galley, validate_response_data
from galley.enums import MenuCategoryEnum, PreparationEnum
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


# This is graphql root for querying data according to sgqlc lib.
# So this class name has to be Query.
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
                        'description': Any,
                        'parentRecipeItems': Any,
                    }]
                }
            }
        }


# RECIPE QUERIES

def recipe_connection_query(
    recipe_ids: List[str],
    page_size: int = DEFAULT_PAGE_SIZE,
    start_index: int = 0
) -> Optional[Operation]:
    query = Operation(Query)
    query.viewer.recipeConnection(
        filters=RecipeConnectionFilter(id=recipe_ids),
        paginationOptions=PaginationOptions(first=page_size, startIndex=start_index)
    )
    query.viewer.recipeConnection.edges()
    query.viewer.recipeConnection.pageInfo()
    query.viewer.recipeConnection.totalCount

    query.viewer.recipeConnection.edges.node.\
        __fields__('id', 'externalName', 'name', 'notes', 'description', 'media', 'categoryValues', 'reconciledNutritionals')
    query.viewer.recipeConnection.edges.node.media.\
        __fields__('altText', 'caption', 'sourceUrl')
    query.viewer.recipeConnection.edges.node.recipeItems.\
        __fields__('ingredient')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.\
        __fields__('id', 'allIngredients', 'name', 'externalName', 'reconciledNutritionals', 'nutritionalsQuantity', 'nutritionalsUnit', 'recipeInstructions')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.recipeTreeComponents.\
        __fields__('id')
    query.viewer.recipeConnection.edges.node.recipeItems.preparations.\
        __fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.ingredient.\
        __fields__('externalName', 'categoryValues')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents(levels=[1]).\
        __fields__('id', 'quantityUnitValues', 'recipeItem')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.quantityUnitValues.\
        __fields__('unit', 'value')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.quantityUnitValues.unit.\
        __fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.\
        __fields__('preparations', 'ingredient', 'subRecipe', 'subRecipeId', 'quantity', 'unit')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.preparations.\
        __fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.ingredient.\
        __fields__('categoryValues', 'externalName')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.ingredient.categoryValues.\
        __fields__('id', 'name', 'category')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.subRecipe.\
        __fields__('id', 'allIngredients', 'externalName', 'name', 'reconciledNutritionals', 'nutritionalsQuantity', 'nutritionalsUnit')
    query.viewer.recipeConnection.edges.node.recipeTreeComponents.recipeItem.unit.\
        __fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.dietaryFlagsWithUsages.dietaryFlag.\
        __fields__('id')
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

def get_menu_query(dates: List[str]) -> Operation:
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates)).__fields__('id', 'name', 'date', 'location', 'categoryValues', 'menuItems')
    query.viewer.menus.menuItems.__fields__('id', 'recipeId', 'categoryValues', 'recipe')
    query.viewer.menus.menuItems.recipe.__fields__('externalName', 'name', 'recipeItems', 'categoryValues', 'media', 'isDish', 'dietaryFlagsWithUsages')
    query.viewer.menus.menuItems.recipe.dietaryFlagsWithUsages.dietaryFlag.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.media.__fields__('altText', 'caption', 'sourceUrl')
    query.viewer.menus.menuItems.recipe.recipeItems.__fields__('subRecipeId', 'preparations')
    query.viewer.menus.menuItems.recipe.recipeItems.preparations.__fields__('id', 'name')
    return query

def get_ops_menu_query(dates: List[str]) -> Operation:
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates)).__fields__('id', 'name', 'date', 'location', 'categoryValues', 'menuItems')
    query.viewer.menus.menuItems.__fields__('id', 'recipeId', 'categoryValues', 'recipe', 'volume', 'unit')
    query.viewer.menus.menuItems.recipe.files.__fields__('photos')
    query.viewer.menus.menuItems.recipe.__fields__('id', 'name', 'categoryValues')
    query.viewer.menus.menuItems.recipe.files.photos.__fields__('sourceUrl', 'caption')
    # query top level recipeTreeComponents
    query.viewer.menus.menuItems.recipe.recipeTreeComponents(levels=[1]).__fields__('quantityUnitValues')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues', 'dietaryFlags')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.__fields__('preparations')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.__fields__('id', 'name', 'externalName', 'categoryValues', 'recipeInstructions', 'dietaryFlagsWithUsages')
    # query second level recipeTreeComponents
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents(levels=[1]).__fields__('quantityUnitValues')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues', 'dietaryFlags')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents.recipeItem.subRecipe.__fields__('id', 'name', 'externalName', 'categoryValues', 'recipeInstructions', 'dietaryFlagsWithUsages')
    # query third level recipeTreeComponents
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents(levels=[1]).__fields__('quantityUnitValues')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents.ingredient.__fields__('id', 'name', 'externalName', 'dietaryFlags')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents.recipeItem.subRecipe.recipeTreeComponents.recipeItem.subRecipe.__fields__('id', 'name', 'externalName', 'dietaryFlagsWithUsages')
    return query

def get_raw_menu_data(dates: List[str],
                      location_name: str,
                      menu_type: str,
                      is_ops: bool=False,
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
    query = get_menu_query(dates=dates)

    if is_ops:
        query = get_ops_menu_query(dates=dates)

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
                    if (
                        categoryValue['category']['id'] == MenuCategoryEnum.MENU_TYPE.value
                        and
                        categoryValue['name'] == menu_type
                    ):
                        response.append(menu)
                    else:
                        continue
    return response

def get_ops_recipe_items_query(recipe_ids: List[str]) -> Operation:
    query = Operation(Query)
    query.viewer.recipes(where=FilterInput(id=recipe_ids)).__fields__('id', 'parentRecipeItems')
    query.viewer.recipes.parentRecipeItems.__fields__('recipe')
    query.viewer.recipes.parentRecipeItems.recipe.__fields__('recipeItems')
    query.viewer.recipes.parentRecipeItems.recipe.recipeItems.__fields__('id', 'subRecipe', 'preparations')
    query.viewer.recipes.parentRecipeItems.recipe.recipeItems.subRecipe.__fields__('id')
    query.viewer.recipes.parentRecipeItems.recipe.recipeItems.preparations.__fields__('id', 'name')
    return query

def get_raw_recipe_items_data(recipe_ids: List) -> Iterable[List[Dict]]:
    """
    Returns a list of dictionaries containing the recipe items data for the
    recipe ids. If there is no recipe items data for the recipe ids, returns None.

    :param recipe_ids: The recipe ids for which the recipe items data is to be
    fetched.
    """
    query = get_ops_recipe_items_query(recipe_ids=recipe_ids)

    validated_response_data = validate_response_data(
            make_request_to_galley(
                op=query.__to_graphql__(auto_select_depth=3),
                variables={'id': recipe_ids}),
            'recipes')
    return validated_response_data

def get_untagged_core_recipe_item_ids(ids):
    recipe_item_ids = []
    ids = [id for id in ids if type(id) == str]
    if len(ids) <= 0:
        error = "No valid recipe ids provided. All ids must be a string."
        logger.exception(error)
        raise ValueError(error)

    recipes = get_raw_recipe_items_data(ids)

    # prepare collection data: ensure concurrent order between ids and recipes
    templateRecipe = {
        "parentRecipeItems": [{
            "recipe": {
                "recipeItems": [{
                    "subRecipe": {
                        "id": None
                    }
                }]
            }
        }]
    }
    recipeCollection = {}
    for recipe in recipes:
        recipeId = recipe["id"]
        recipePos = ids.index(recipeId)
        parentItems = templateRecipe["parentRecipeItems"]
        if recipePos >= 0:
            parentItems = recipe["parentRecipeItems"]
            # collect all recipe items 2d array
            recipeCollection[recipeId] = [parentItem['recipe']['recipeItems'] \
                        for parentItem in parentItems]
            '''
            print("   ", recipeId, " ::: ", recipePos, " ::: ", ids[recipePos])
            print("\n\n.....................................\n\n")
            print(len(recipeItems))
            print("\n\n********************>>>>>>>>>>>>>>>>>>>\n\n")
            # single array and filter out only the subrecipes whose ids matching the entry recipe id
            recipeCollection[recipeId] = [recipeItem for recipeItem in recipeItems \
                                         if recipeItem and recipeItem['subRecipe'] \
                                            and recipeItem['subRecipe']['id'] == ids[recipePos]]
            '''

    '''
    # check for untagged recipe items
    for recipeInCollection in recipeCollection:
        preparationSet = {preparation.get('id') for preparation \
                         in recipeInCollection['preparations']}
        if PreparationEnum.CORE_RECIPE.value in preparationSet:
            recipe_item_ids.append(recipeInCollection[id])

    from pprint import pprint
    print("\n\n********************>>>>>>>>>>>>>>>>>>>\n\n")
    pprint(recipe_item_ids)
    print("\n\n********************>>>>>>>>>>>>>>>>>>>\n\n")
    '''

    if recipes:
        recipes = sorted(recipes, key=lambda r: r['id'])
        for id, recipe in zip(sorted(ids), recipes):
            for parent in recipe['parentRecipeItems']:
                for recipe_item in parent['recipe']['recipeItems']:
                    if recipe_item['subRecipe']:
                        if recipe_item['subRecipe']['id'] == id \
                            and PreparationEnum.CORE_RECIPE.value \
                                not in {prep.get('id') for prep in recipe_item['preparations']}:
                            recipe_item_ids.append(recipe_item['id'])

    # pprint(recipe_item_ids)
    # print("\n\n********************>>>>>>>>>>>>>>>>>>>\n\n")

    return recipe_item_ids
