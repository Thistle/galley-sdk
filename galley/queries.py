import logging
from typing import Dict, List, Optional
from galley.common import GALLEY_ERROR_PREFIX, build_galley_client
from galley.enums import LocationEnum, MenuCategoryEnum, PreparationEnum

from galley_client.get_ops_recipe_item_connection_data import GetOpsRecipeItemConnectionDataViewerRecipeItemConnection


logger = logging.getLogger(__name__)


DEFAULT_PAGE_SIZE = 20


def get_raw_recipes_data(recipe_ids: List[str], location_name: str) -> Optional[List[Dict]]:
    has_next_page = True
    page_size = DEFAULT_PAGE_SIZE
    start_index = 0

    recipes = []

    try:
        location_id = LocationEnum[location_name.upper()].value
    except KeyError:
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Invalid location name: {f'{location_name}'}")

    if recipe_ids is None:
        return []

    client = build_galley_client()

    while has_next_page:
        raw_data = client.get_recipe_data(
            id=recipe_ids,
            locationId=location_id,
            pageSize=page_size,
            startIndex=start_index
        )

        collection = raw_data.viewer.recipeConnection

        for edge in collection.edges:
            recipe = edge.node
            if recipe:
                recipes.append(recipe)

        start_index = collection.pageInfo.endIndex
        has_next_page = collection.pageInfo.hasNextPage or False
    return [recipe.dict() for recipe in recipes]


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

    if is_ops:
        client = build_galley_client(timeout=90) # ops query is slow
        raw_data = client.get_ops_menu_data(date=dates, locationId=location_id)
    else:
        client = build_galley_client()
        raw_data = client.get_menu_data(date=dates, locationId=location_id)

    menus = []
    if raw_data:
        for edge in raw_data.viewer.menuConnection.edges:
            menu = edge.node
            if menu.location.name == location_name:
                category_values = menu.categoryValues
                for category_value in category_values:
                    if (
                        category_value.category.id == MenuCategoryEnum.MENU_TYPE.value
                        and
                        category_value.name == menu_type
                    ):
                        menus.append(menu)
                    else:
                        continue
    return [menu.dict() for menu in menus]


def get_raw_recipe_items_data_via_connection(sub_recipe_ids: List) -> GetOpsRecipeItemConnectionDataViewerRecipeItemConnection:
    client = build_galley_client()
    response = client.get_ops_recipe_item_connection_data(subRecipeIds=sub_recipe_ids)
    return response.viewer.recipeItemConnection


def get_untagged_core_recipe_item_ids_via_connection(ids):
    preparationTag = PreparationEnum.CORE_RECIPE.value
    recipe_item_ids = []
    ids = [id for id in ids if type(id) == str]
    if len(ids) <= 0:
        error = "No valid recipe ids provided. All ids must be a string."
        logger.exception(error)
        raise ValueError(error)
    recipe_item_connection = get_raw_recipe_items_data_via_connection(ids) or {}
    for recipe_item in recipe_item_connection.edges:
        recipe_item = recipe_item.node
        preparations = [preparation.id for preparation in recipe_item.preparations]
        if preparationTag not in preparations:
            recipe_item_ids.append(recipe_item.id)
    return recipe_item_ids
