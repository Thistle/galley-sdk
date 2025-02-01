from sgqlc.operation import Operation
from sgqlc.types import Field, Type
from typing import List
from galley.common import make_request_to_galley, validate_response_data
from galley.queries import get_ingredient_ids_by_name, get_ingredient_ids_by_search_term, get_ingredient_usages_by_ingredient_ids
from galley.types import (
    BulkMenusInput,
    MenuInput,
    MenuItemInput,
    MenuPayload,
    UnitInput,
    BulkUpdateRecipeItemsPayload,
    BulkUpdateRecipeItemsInput,
    RecipeItemInput
)
from galley.enums import PreparationEnum
import logging

logger = logging.getLogger(__name__)

GALLEY_ERROR_PREFIX = "(GalleyError)"


# This is graphql root for mutating data according to sgqlc lib. So this class name has to be Mutation.
class Mutation(Type):
    bulkUpsertMenus = Field(MenuPayload, args={'input': BulkMenusInput})
    bulkUpdateRecipeItems = Field(BulkUpdateRecipeItemsPayload, args={'input': BulkUpdateRecipeItemsInput})


# MENU MUTATIONS
UNIT_NAME_WHITELIST = ['each']
def build_unit_input(item):
    if 'unit_name' in item.keys() and \
        item['unit_name'] is not None and \
        item['unit_name'] in UNIT_NAME_WHITELIST:

        name = item['unit_name']
    else:
        name = 'each'
    return UnitInput(name=name)


def build_menu_item_inputs(items):
    menu_item_inputs = []
    for item in items:
        unit_input = build_unit_input(item)
        menuItemInput = MenuItemInput(
            id=item['id'],
            volume=item['volume'],
            unit=unit_input
        )
        menu_item_inputs.append(menuItemInput)
    return menu_item_inputs


def build_menu_inputs(menus):
    menu_inputs = []
    for menu in menus:
        if 'menu_id' not in menu.keys() or menu['menu_id'] is None:
            raise ValueError("menu_id is required for successful requests")

        menu_input = MenuInput(id=menu['menu_id'])
        menu_input.menuItems = build_menu_item_inputs(menu['menu_items'])
        menu_inputs.append(menu_input)
    return menu_inputs


def build_upsert_mutation_query(args):
    mutation = Operation(Mutation)
    bulk_input = BulkMenusInput()
    bulk_input.menus = build_menu_inputs(args)
    mutation.bulkUpsertMenus(input=bulk_input)
    return mutation


# args = [
# {
#   menu_id: '',
#       menu_items: [
#           {
#               id: '',
#               volume: float,
#               unit_name: ''
#           },
#           {id: '', ....}
# ]
def upsert_menu_data(args):
    mutation = build_upsert_mutation_query(args)
    response = make_request_to_galley(op=mutation)
    return validate_response_data(response)


def build_bulk_update_recipe_item_query(args):
    ids = []
    if args.get("ids"):
        ids = [id for id in args["ids"] if type(id) == str]
        if len(ids) <= 0:
            msg = f"{GALLEY_ERROR_PREFIX} No valid IDs provided. \
                    All IDs must be strings."
            logger.exception(msg)
            raise ValueError(msg)

    mutation = Operation(Mutation)
    bulk_input = BulkUpdateRecipeItemsInput(
        ids=ids,
        attrs=RecipeItemInput(args["attrs"])
    )
    mutation.bulkUpdateRecipeItems(input=bulk_input)
    return mutation


def bulk_update_recipe_item_data(args):
    if not args.get("attrs"):
        msg = f"{GALLEY_ERROR_PREFIX} attrs property not provided"
        logger.exception(msg)
        raise ValueError(msg)

    if not args.get("ids"):
        msg = f"{GALLEY_ERROR_PREFIX} Recipe item id list not provided"
        logger.exception(msg)
        raise ValueError(msg)

    payload = {
        "ids": args["ids"],
        "attrs": args["attrs"],
    }
    mutation = build_bulk_update_recipe_item_query(payload)
    response = make_request_to_galley(op=mutation)
    valid_response = validate_response_data(response)

    if valid_response is None:
        raise ValueError("Error running migration. Invalid response returned.")
    return valid_response


def bulk_add_preparation_to_ingredient_recipe_items(
    ingredient_ids: List[str], preparation_id: str, exclude_preparations: List[str] = []
):
    ingredient_connection = get_ingredient_usages_by_ingredient_ids(ingredient_ids)
    recipe_item_ids = [
        usage["id"]
        for node in [edge["node"] for edge in ingredient_connection.get("edges", [])]
        for item in node.get("recipeItems", [])
        for usage in item["recipe"]["recipeItems"]
        if usage["ingredient"]
            and usage["ingredient"]["id"] == node.get("id")
            and (
                not (preparations := [p["id"] for p in usage["preparations"]]) or
                not any(exclusion in preparations for exclusion in exclude_preparations)
            )
    ]

    if not recipe_item_ids:
        logger.info("No recipe items found to update.")
        return None

    return bulk_update_recipe_item_data(
        {
            "ids": recipe_item_ids,
            "attrs": {
                "preparationIds": [preparation_id]
            },
        }
    )


def bulk_add_deliver_to_production_preparation_to_send_to_plate_ingredient_usages(
    exclude_ingredient_names: List[str] = [], exclude_ingredient_ids: List[str] = []
):
    if exclude_ingredient_names:
        exclude_ingredient_ids.extend([
            ingredient
            for ingredient in get_ingredient_ids_by_name(
                ingredient_names=exclude_ingredient_names
            )
        ])
    ingredient_ids = list(
        set(get_ingredient_ids_by_search_term(search_term="SEND TO PLATE")) -
        set(exclude_ingredient_ids)
    )
    return bulk_add_preparation_to_ingredient_recipe_items(
        ingredient_ids=ingredient_ids,
        preparation_id=PreparationEnum.DELIVER_TO_PRODUCTION.value,
        exclude_preparations=[
            PreparationEnum.DELIVER_TO_WASH.value,
            PreparationEnum.DELIVER_TO_PRODUCTION.value,
        ],
    )
