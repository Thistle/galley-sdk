import logging
from collections import defaultdict
from typing import Any, Dict, Iterable, List, Optional
from galley.common import GALLEY_ERROR_PREFIX, make_request_to_galley, validate_response_data
from galley.enums import LocationEnum, MenuCategoryEnum, PreparationEnum
from galley.types import (
    IngredientConnectionSearch,
    Menu,
    PreparationConnection,
    PreparationConnectionFilter,
    PreparationConnectionPaginationOptions,
    Recipe,
    FilterInput,
    IngredientConnection,
    IngredientConnectionFilter,
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
            'paginationOptions': PaginationOptions,
        }))
    )
    recipeItemConnection = Field(
        RecipeItemConnection,
        args=(ArgDict({
            'filters': RecipeItemConnectionFilter,
            'paginationOptions': RecipeItemConnectionPaginationOptions,
        }))
    )
    ingredientConnection = Field(
        IngredientConnection,
        args=(ArgDict({
            'filters': IngredientConnectionFilter,
            'paginationOptions': PaginationOptions,
        }))
    )
    preparationConnection = Field(
        PreparationConnection,
        args=(ArgDict({
            'filters': PreparationConnectionFilter,
            'paginationOptions': PreparationConnectionPaginationOptions,
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
    query.viewer.recipeConnection.edges.node.__fields__('id', 'externalName', 'name', 'notes', 'description', 'categoryValues', 'files')
    query.viewer.recipeConnection.edges.node.dietaryFlagsWithUsages(location_id=location_id)
    query.viewer.recipeConnection.edges.node.reconciledNutritionals(location_id=location_id)
    query.viewer.recipeConnection.edges.node.recipeItems.__fields__('id', 'recipeId', 'preparations', 'quantity')
    query.viewer.recipeConnection.edges.node.recipeItems.preparations.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.unit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.unit.unitValues.__fields__('value')
    query.viewer.recipeConnection.edges.node.recipeItems.unit.unitValues.unit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.__fields__('id', 'name', 'externalName', 'nutritionalsQuantity')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.nutritionalsUnit.__fields__('id', 'name')
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.reconciledNutritionals(location_id=location_id)
    query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.dietaryFlagsWithUsages(location_id=location_id)
    query.viewer.recipeConnection.edges.node.recipeItems.ingredient.locationVendorItems(location_ids=[location_id])
    query.viewer.recipeConnection.edges.node.recipeItems.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues')
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.ingredient.locationVendorItems(location_ids=[location_id])
    query.viewer.recipeConnection.edges.node.ingredientsWithUsages.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues', 'dietaryFlags')
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


def get_recipe_id_by_name_query(
    name: str,
    page_size: int = DEFAULT_PAGE_SIZE,
    start_index: int = 0
) -> Operation:
    query = Operation(Query)
    query.viewer.recipeConnection(filters=RecipeConnectionFilter(name=name)).__fields__('edges')
    query.viewer.recipeConnection.edges.__fields__('node')
    query.viewer.recipeConnection.edges.node.__fields__('id', 'name')
    return query


def get_menu_query(dates: List[str], location_id: str) -> Operation:
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates, locationId=location_id)).__fields__('id', 'name', 'date', 'location', 'categoryValues', 'menuItems')
    query.viewer.menus.menuItems.__fields__('id', 'recipeId', 'categoryValues', 'recipe', 'volume')
    query.viewer.menus.menuItems.recipe.__fields__('externalName', 'name', 'recipeItems', 'categoryValues', 'files', 'isDish')
    query.viewer.menus.menuItems.recipe.dietaryFlagsWithUsages(location_id=location_id)
    query.viewer.menus.menuItems.recipe.recipeItems.__fields__('subRecipeId', 'preparations')
    query.viewer.menus.menuItems.recipe.recipeItems.preparations.__fields__('id', 'name')
    return query


def get_ops_menu_query(dates: List[str], location_id: str) -> Operation:
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates, locationId=location_id)).__fields__('id', 'name', 'date', 'location', 'categoryValues', 'menuItems')
    query.viewer.menus.menuItems.__fields__('id', 'recipeId', 'categoryValues', 'volume')
    query.viewer.menus.menuItems.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.__fields__('id', 'name', 'categoryValues', 'files')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents(levels=[0, 1, 2, 3])
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.__fields__('id', 'ancestorComponentIds', 'quantity')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.unit.unitValues.__fields__('value')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.unit.unitValues.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.__fields__('preparations', 'quantity')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.preparations.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.unit.__fields__('id', 'name')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.ingredient.locationVendorItems(location_ids=[location_id])
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.ingredient.__fields__('id', 'name', 'externalName', 'categoryValues', 'dietaryFlags')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.__fields__('id', 'name', 'externalName', 'categoryValues', 'recipeInstructions')
    query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.allIngredientsWithUsages(location_id=location_id).ingredient.__fields__('name', 'externalName')
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


def get_ingredient_id_by_name_query(name: str) -> Operation:
    query = Operation(Query)
    query.viewer.ingredientConnection(filters=IngredientConnectionFilter(name=name)).__fields__('edges')
    query.viewer.ingredientConnection.edges.__fields__('node')
    query.viewer.ingredientConnection.edges.node.__fields__('id', 'name')
    return query


def get_ingredients_by_search_term_query(search_term: str, page_size: int = DEFAULT_PAGE_SIZE, start_index: int = 0) -> Operation:
    query = Operation(Query)
    query.viewer.ingredientConnection(
        filters=IngredientConnectionFilter(search=IngredientConnectionSearch(query=search_term)),
        paginationOptions=PaginationOptions(first=page_size, startIndex=start_index),
    ).__fields__('edges', 'totalCount', 'pageInfo')
    query.viewer.ingredientConnection.edges.__fields__('node')
    query.viewer.ingredientConnection.edges.node.__fields__('id', 'name')
    return query


def get_ingredient_usages_by_ids_query(ids: List[str], page_size: int = DEFAULT_PAGE_SIZE, start_index: int = 0) -> Operation:
    query = Operation(Query)
    query.viewer.ingredientConnection(
        filters=IngredientConnectionFilter(id=ids),
        paginationOptions=PaginationOptions(first=page_size, startIndex=start_index),
    ).__fields__('edges', 'totalCount', 'pageInfo')
    query.viewer.ingredientConnection.edges.__fields__('node')
    query.viewer.ingredientConnection.edges.node.__fields__('id', 'name', 'usagesCount', 'recipeItems')
    query.viewer.ingredientConnection.edges.node.recipeItems.__fields__('id', 'preparations', 'recipe')
    query.viewer.ingredientConnection.edges.node.recipeItems.preparations.__fields__('id', 'name')
    query.viewer.ingredientConnection.edges.node.recipeItems.recipe.__fields__('id', 'name', 'isDish', 'recipeItems')
    query.viewer.ingredientConnection.edges.node.recipeItems.recipe.recipeItems.__fields__('id', 'ingredient', 'subRecipe')
    query.viewer.ingredientConnection.edges.node.recipeItems.recipe.recipeItems.ingredient.__fields__('id', 'name')
    query.viewer.ingredientConnection.edges.node.recipeItems.recipe.recipeItems.subRecipe.__fields__('id', 'name')
    query.viewer
    return query


def get_preparations_by_preparation_ids_query(preparation_ids: List[str]) -> Operation:
    query = Operation(Query)
    query.viewer.preparationConnection(filters=PreparationConnectionFilter(id=preparation_ids)).__fields__('edges', 'totalCount', 'pageInfo')
    query.viewer.preparationConnection.edges.__fields__('node')
    query.viewer.preparationConnection.edges.node.__fields__('id', 'name', 'recipeItemPreparations')
    query.viewer.preparationConnection.edges.node.recipeItemPreparations.__fields__('id', 'recipeItemId', 'preparationId', 'recipeItem')
    query.viewer.preparationConnection.edges.node.recipeItemPreparations.recipeItem.__fields__('id', 'ingredient', 'recipeId', 'subRecipeId')
    query.viewer.preparationConnection.edges.node.recipeItemPreparations.recipeItem.ingredient.__fields__('id', 'name')
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


def get_ingredient_ids_by_name(ingredient_names: List[str]) -> List[str]:
    ingredient_ids = []
    for name in ingredient_names:
        query = get_ingredient_id_by_name_query(name=name)
        ingredient_connection = validate_response_data(
                make_request_to_galley(
                    op=query,
                    variables={'name': name}),
                'ingredientConnection')

        if ingredient_connection and len(ingredient_connection.get('edges', [])) > 0:
            for edge in ingredient_connection.get('edges', []):
                id = edge.get('node', {}).get('id', '')
                if id:
                    ingredient_ids.append(id)
        else:
            logger.warning(f"No ingredient found with the name {name}")
    return ingredient_ids


def get_recipe_ids_by_name(recipe_names):
    recipe_ids = []
    for name in recipe_names:
        query = get_recipe_id_by_name_query(
            name=name
        )
        recipe_connection = validate_response_data(
            make_request_to_galley(
                op=query,
                variables={'name': name}),
            'recipeConnection')

        if recipe_connection and len(recipe_connection.get('edges', [])) > 0:
            for edge in recipe_connection.get('edges', []):
                id = edge.get('node', {}).get('id', '')
                if id:
                    recipe_ids.append(id)
        else:
            logger.warning(f"No recipe found with the name {name}")
    return recipe_ids


def get_ingredient_connection_by_ingredient_ids(ingredient_ids, start_index = 0):
    query = get_ingredient_usages_by_ids_query(ingredient_ids, start_index=start_index)
    ingredient_connection = validate_response_data(
        make_request_to_galley(
            op=query,
            variables={'id': ingredient_ids}
        ),
        'ingredientConnection'
    )
    return ingredient_connection


def get_ingredient_usages_by_name(ingredient_names: List[str]):
    ingredient_ids = get_ingredient_ids_by_name(ingredient_names)
    return get_ingredient_usages_by_ingredient_ids(ingredient_ids=ingredient_ids)


def get_ingredient_connection_by_search_term(search_term, start_index = 0):
    query = get_ingredients_by_search_term_query(
        search_term=search_term,
        start_index=start_index,
    )
    ingredient_connection = validate_response_data(
        make_request_to_galley(
            op=query,
            variables={
                'search': {
                    'query': search_term
                }
            }
        ),
        'ingredientConnection'
    )
    return ingredient_connection


def get_ingredient_usages_by_ingredient_ids(ingredient_ids, start_index = 0, ingredient_usages = {}):
    if not ingredient_usages:
        ingredient_usages = defaultdict(list)

    ingredient_connection = get_ingredient_connection_by_ingredient_ids(
        ingredient_ids=ingredient_ids, start_index=start_index
    )

    if ingredient_connection:
        for edge in ingredient_connection.get("edges", []):
            for nri in edge.get("node", {}).get("recipeItems", []):
                nri["ingredient_name"] = edge.get("node", {}).get("name")
                ingredient_usages[edge.get("node", {}).get("id")].append(nri)

        if ingredient_connection.get('pageInfo', {}).get('hasNextPage'):
            return get_ingredient_usages_by_ingredient_ids(
                ingredient_ids=ingredient_ids,
                start_index=ingredient_connection.get('pageInfo', {}).get('endIndex'),
                ingredient_usages=ingredient_usages,
            )
    return ingredient_usages


def get_ingredient_ids_by_search_term(search_term, start_index = 0, ingredient_ids = []):
    ingredient_connection = get_ingredient_connection_by_search_term(
        search_term=search_term,
        start_index=start_index,
    )

    if ingredient_connection:
        ingredient_ids.extend(
            [edge.get("node", {}).get("id") for edge in ingredient_connection.get("edges", [])]
        )

        if ingredient_connection.get('pageInfo', {}).get('hasNextPage'):
            return get_ingredient_ids_by_search_term(
                search_term=search_term,
                start_index=ingredient_connection.get('pageInfo', {}).get('endIndex'),
                ingredient_ids=ingredient_ids,
            )
    return ingredient_ids


def get_preparation_connection_by_preparation_ids(preparation_ids):
    query = get_preparations_by_preparation_ids_query(preparation_ids)
    preparation_connection = validate_response_data(
        make_request_to_galley(
            op=query,
            variables={'id': preparation_ids}
        ),
        'preparationConnection'
    )
    return preparation_connection


def get_recipe_item_preparations_by_preparation_ids(preparation_ids):
    preparation_connection = get_preparation_connection_by_preparation_ids(preparation_ids)
    return [
        node
        for edge in preparation_connection.get("edges", [])
        for node in edge.get("node", {}).get("recipeItemPreparations", [])
    ]
