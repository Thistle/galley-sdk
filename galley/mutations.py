from sgqlc.operation import Operation
from sgqlc.types import Field, Type
from typing import Dict, List, Optional, Union, Any
from galley.common import make_request_to_galley, validate_response_data
from galley.queries import get_untagged_core_recipe_item_ids_via_connection
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

    # apply filter to ensure that only untagged recipe items are selected for tagging
    recipe_item_ids = get_untagged_core_recipe_item_ids_via_connection(args["ids"])
    payload = {
        "ids": recipe_item_ids,
        "attrs": args["attrs"],
    }
    mutation = build_bulk_update_recipe_item_query(payload)
    response = make_request_to_galley(op=mutation)

    from pprint import pprint
    pprint(response)

    valid_response = validate_response_data(response)

    if valid_response is None:
        raise ValueError("Error running migration. Invalid response returned.")

    return valid_response
