import logging
from typing import Any, Dict, Iterable, List, Optional
from galley.common import GALLEY_ERROR_PREFIX, make_request_to_galley, validate_response_data
from galley.enums import LocationEnum, MenuCategoryEnum, PreparationEnum
from galley.types import (
    Menu,
    Recipe,
    FilterInput,
    MenuFilterInput,
    RecipeConnection,
    PaginationOptions,
    RecipeItemConnection,
    RecipeConnectionFilter,
    RecipeItemConnectionFilter,
    RecipeItemConnectionPaginationOptions
)
from sgqlc.operation import Operation
from sgqlc.types import ArgDict, Field, Type


logger = logging.getLogger(__name__)


DEFAULT_PAGE_SIZE = 20


class Viewer(Type):
    recipeConnection = Field(
        RecipeConnection,
        args=(ArgDict({
            'filters': RecipeConnectionFilter,
            'paginationOptions': PaginationOptions
        }))
    )
    recipeItemConnection = Field(
        RecipeItemConnection,
        args=(ArgDict({
            'filters': RecipeItemConnectionFilter,
            'paginationOptions': RecipeItemConnectionPaginationOptions
        }))
    )
    recipes = Field(Recipe, args=(ArgDict({'where': FilterInput})))
    recipe = Field(Recipe, args=(ArgDict({'id': str})))
    menus = Field(Menu, args=(ArgDict({'where': MenuFilterInput})))


# This is graphql root for querying data according
# to sgqlc lib, so this class name has to be Query
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
    location_id: str,
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
    query.viewer.recipeConnection.totalCount()
    query.viewer.recipeConnection.edges.node.__fields__('id', 'externalName', 'name', 'notes', 'description', 'media', 'categoryValues')
    query.viewer.recipeConnection.edges.node.dietaryFlagsWithUsages(location_id=location_id)
    query.viewer.recipeConnection.edges.node.reconciledNutritionals(location_id=location_id)
    query.viewer.recipeConnection.edges.node.recipeItems.__fields__('recipeId', 'preparations', 'quantity')
    query.viewer.recipeConnection.edges.node.recipeItems.unit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.unit.unitValues.__fields__('value')
    query.viewer.recipeConnection.edges.node.recipeItems.unit.unitValues.unit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.__fields__('id', 'name', 'externalName', 'nutritionalsQuantity')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.nutritionalsUnit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.reconciledNutritionals(location_id=location_id)
    query.viewer.recipeConnection.edges.node.recipeItems.ingredient.locationVendorItems(location_ids=[location_id])
    query.viewer.recipeConnection.edges.node.recipeItems.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues')
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.ingredient.locationVendorItems(location_ids=[location_id])
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues')
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.usages.__fields__('ancestorRecipes', 'quantity')
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.usages.unit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.usages.unit.unitValues.__fields__('value')
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.usages.unit.unitValues.unit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.versionConnection(paginationOptions=PaginationOptions(orderBy='createdAt', sortDirection="desc", first=1)).edges.node
    return query


def get_raw_recipes_data(recipe_ids: List[str], location_name: str) -> Optional[List[Dict]]:
    has_next_page = True
    page_size = DEFAULT_PAGE_SIZE
    start_index = 0

    raw_recipes_data = []

    try:
        location_id = LocationEnum[location_name.upper()].value
    except KeyError:
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Invalid location name: {f'{location_name}'}")

    if recipe_ids is None:
        return []

    while has_next_page:
        query = recipe_connection_query(recipe_ids=recipe_ids, location_id=location_id, page_size=page_size, start_index=start_index)
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


def get_menu_query(dates: List[str], location_id: str) -> Operation:
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates, locationId=location_id)).__fields__('id', 'name', 'date', 'location', 'categoryValues', 'menuItems')
    query.viewer.menus.menuItems.__fields__('id', 'recipeId', 'categoryValues', 'recipe')
    query.viewer.menus.menuItems.recipe.__fields__('externalName', 'name', 'recipeItems', 'categoryValues', 'media', 'isDish')
    query.viewer.menus.menuItems.recipe.dietaryFlagsWithUsages(location_id=location_id)
    query.viewer.menus.menuItems.recipe.media.__fields__('altText', 'caption', 'sourceUrl')
    query.viewer.menus.menuItems.recipe.recipeItems.__fields__('subRecipeId', 'preparations')
    query.viewer.menus.menuItems.recipe.recipeItems.preparations.__fields__('id', 'name')
    return query


def get_ops_menu_query(dates: List[str], location_id: str) -> Operation:
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates, locationId=location_id)).__fields__('id', 'name', 'date', 'location', 'categoryValues', 'menuItems')
    query.viewer.menus.menuItems.__fields__('id', 'recipeId', 'categoryValues', 'volume')
    query.viewer.menus.menuItems.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.__fields__('id', 'name', 'categoryValues', 'files')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.__fields__('id', 'ancestorComponentIds', 'quantity')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.unit.unitValues.__fields__('value')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.unit.unitValues.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.__fields__('preparations', 'quantity')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.ingredient.locationVendorItems(location_ids=[location_id])
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues', 'dietaryFlags')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.__fields__('id', 'name', 'externalName', 'categoryValues', 'recipeInstructions')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.dietaryFlagsWithUsages(location_id=location_id)
    return query


def get_raw_menu_data(
    dates: List[str],
    location_name: str,
    menu_type: str,
    is_ops: bool = False,
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
    try:
        location_id = LocationEnum[location_name.upper()].value
    except KeyError:
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Invalid location name: {f'{location_name}'}")

    query = get_menu_query(dates=dates, location_id=location_id)

    if is_ops:
        query = get_ops_menu_query(dates=dates, location_id=location_id)

    validated_response_data = validate_response_data(
        make_request_to_galley(
            op=query.__to_graphql__(auto_select_depth=3),
            variables={'date': dates}
        ),
        'menus'
    )

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


def get_ops_recipe_item_connection_query(sub_recipe_ids: List[str]) -> Operation:
    query = Operation(Query)
    query.viewer.recipeItemConnection(filters=RecipeItemConnectionFilter(subRecipeIds=sub_recipe_ids)).__fields__('edges')
    query.viewer.recipeItemConnection.edges.__fields__('node')
    query.viewer.recipeItemConnection.edges.node.__fields__('id', 'recipeId', 'preparations')
    query.viewer.recipeItemConnection.edges.node.preparations.__fields__('id', 'name')
    return query


def get_raw_recipe_items_data_via_connection(sub_recipe_ids: List) -> Iterable[List[Dict]]:
    query = get_ops_recipe_item_connection_query(sub_recipe_ids=sub_recipe_ids)
    validated_response_data = validate_response_data(
            make_request_to_galley(
                op=query.__to_graphql__(auto_select_depth=3),
                variables={'subRecipeIds': sub_recipe_ids}),
            'recipeItemConnection')
    return validated_response_data


def get_untagged_core_recipe_item_ids_via_connection(ids):
    preparationTag = PreparationEnum.CORE_RECIPE.value
    recipe_item_ids = []
    ids = [id for id in ids if type(id) == str]
    if len(ids) <= 0:
        error = "No valid recipe ids provided. All ids must be a string."
        logger.exception(error)
        raise ValueError(error)
    recipe_item_connection = get_raw_recipe_items_data_via_connection(ids) or {}
    for recipe_item in recipe_item_connection.get("edges", []):
        recipe_item = recipe_item["node"]
        preparations = [preparation["id"] for preparation in recipe_item["preparations"]]
        if preparationTag not in preparations:
            recipe_item_ids.append(recipe_item["id"])
    return recipe_item_ids
