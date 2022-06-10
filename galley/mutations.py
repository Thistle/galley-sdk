from sgqlc.operation import Operation
from sgqlc.types import Field, Type
from typing import Dict, List, Optional, Union, Any
from galley.common import make_request_to_galley, validate_response_data
from galley.queries import get_recipe_item_ids
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


def build_update_mutation_query(args):
    ids = []
    if args["ids"] is not None and len(args["ids"]) > 0:
        ids = {idx for idx in args["ids"] if type(idx).__name__ == "str"}
        if len(ids) <= 0:
            raise ValueError("non valid ID provided, all IDs must be strings")

    mutation = Operation(Mutation)
    bulk_input = BulkUpdateRecipeItemsInput(
        ids=ids,
        attrs=RecipeItemInput(args["attrs"])
    )
    mutation.bulkUpdateRecipeItems(input=bulk_input)
    return mutation


def update_recipe_item_data(args):
    if "attrs" not in args.keys() or args["attrs"] is None:
        raise ValueError("attrs property not provided")

    if "ids" not in args.keys() or args["ids"] is None or len(args["ids"]) <= 0:
        raise ValueError("recipe item id list not provided")

    recipe_item_ids = get_recipe_item_ids(args["ids"])
    payload = {
        "ids": recipe_item_ids,
        "attrs": args["attrs"],
    }
    mutation = build_update_mutation_query(payload)
    response = make_request_to_galley(op=mutation)
    return validate_response_data(response)
