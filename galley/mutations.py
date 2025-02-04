from sgqlc.operation import Operation
from sgqlc.types import Field, Type
from typing import List
from galley.common import make_request_to_galley, validate_response_data
from galley.queries import get_ingredient_ids_by_name, get_ingredient_usages_by_ingredient_ids, get_recipe_item_preparations_by_preparation_ids
from galley.types import (
    BulkMenusInput,
    DeleteRecipeItemPreparationInput,
    DeleteRecipeItemPreparationPayload,
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
    deleteRecipeItemPreparation = Field(DeleteRecipeItemPreparationPayload, args={'input': DeleteRecipeItemPreparationInput})


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


def delete_recipe_item_preparation(recipe_item_preparation_id: str):
    mutation = Operation(Mutation)
    delete_input = DeleteRecipeItemPreparationInput(
        recipeItemPreparationId=recipe_item_preparation_id
    )
    mutation.deleteRecipeItemPreparation(input=delete_input)
    response = make_request_to_galley(op=mutation)
    return validate_response_data(response)


def bulk_add_preparation_to_ingredient_recipe_items(
    ingredient_ids: List[str],
    preparation_id: str,
    exclude_preparations: List[str] = [],
    dry_run: bool = True,
):
    ingredient_usages = get_ingredient_usages_by_ingredient_ids(ingredient_ids)
    recipe_item_ids = [
        usage["id"]
        for ingredient_id, usages in ingredient_usages.items()
        for usage in usages
        if (
            not (preparations := [p["id"] for p in usage["preparations"]]) or
            not (
                preparation_id in preparations or
                any(exclusion in preparations for exclusion in exclude_preparations)
            )
        )
    ]

    if not recipe_item_ids:
        logger.warning("No recipe items found to update.")
        return None

    logger.warning(f"Adding {len(recipe_item_ids)} ingredient recipe item preparations.")

    if not dry_run:
        return bulk_update_recipe_item_data(
            {
                "ids": recipe_item_ids,
                "attrs": {
                    "preparationIds": [preparation_id]
                },
            }
        )
    return


def delete_ingredient_usage_preparations_by_preparation_ids(
    preparation_ids: List[str],
    include_ingredient_ids: List[str] = [],
    exclude_ingredient_ids: List[str] = [],
    dry_run: bool = True,
) -> None:
    delete_bin = []
    recipe_item_preparations = get_recipe_item_preparations_by_preparation_ids(preparation_ids)

    if not recipe_item_preparations:
        logger.warning("No recipe item preparations found to delete.")
        return None

    if include_ingredient_ids:
        delete_bin = [
            recipe_item_preparation
            for recipe_item_preparation in recipe_item_preparations
            if (
                (ingredient := recipe_item_preparation["recipeItem"]["ingredient"])
                and ingredient["id"] in include_ingredient_ids
            )
        ]
    elif exclude_ingredient_ids:
        delete_bin = [
            recipe_item_preparation
            for recipe_item_preparation in recipe_item_preparations
            if (
                (ingredient := recipe_item_preparation["recipeItem"]["ingredient"])
                and ingredient["id"] not in exclude_ingredient_ids
            )
        ]
    else:
        delete_bin = [
            recipe_item_preparation
            for recipe_item_preparation in recipe_item_preparations
            if recipe_item_preparation["recipeItem"]["ingredient"]
        ]

    logger.warning(f"Deleting {(total := len(delete_bin))} ingredient recipe item preparations.")

    if not dry_run:
        delete_count = 0
        while delete_bin:
            for _ in range(50):

                if not delete_bin:
                    break

                item = delete_bin.pop()
                try:
                    delete_recipe_item_preparation(recipe_item_preparation_id=item["id"])
                    delete_count += 1
                except Exception as e:
                    logger.error(
                        f'Failure to delete preparation {item["preparationId"]} from '
                        f'ingredient {item["recipeItem"]["ingredient"]["id"]} within '
                        f'recipe {item["recipeItem"]["recipeId"]}: {e}'
                    )
                    continue
            logger.warning(f"Deleted {delete_count} of {total} recipe item preparations.")
    return


# def swap_ingredient_usage_preparations_by_ingredients(
#     preparation_id_to_remove: str,
#     preparation_id_to_add_in: str,
#     ingredient_ids: List[str] = [],
#     ingredient_names: List[str] = [],
# ) -> None:
#     if ingredient_names:
#         ingredient_ids.extend([
#             ingredient
#             for ingredient in get_ingredient_ids_by_name(
#                 ingredient_names=ingredient_names
#             )
#         ])
#     ingredient_ids = list(set(ingredient_ids))
#     ingredient_usages = get_ingredient_usages_by_ingredient_ids(ingredient_ids)
#     from pprint import pprint
#     pprint(ingredient_usages)
#     filtered_recipe_item_preparations = {
#         usage["id"]: set(filter(
#             lambda u: (
#                 preparations := [p["id"] for p in u["preparations"]] and
#                 preparation_id_to_remove in preparations and
#                 preparation_id_to_add_in not in preparations
#             ),
#             usage["preparations"]
#         ))
#         for ingredient_id, usages in ingredient_usages.items()
#         for usage in usages
#     }

#     if not filtered_recipe_item_preparations:
#         logger.warning("No recipe items found to update.")
#         return None

#     for recipe_item_id, usage in filtered_recipe_item_preparations.items():
#         preparation_ids = (
#             set([p["id"] for p in usage["preparations"]]) -
#             set([preparation_id_to_remove]) |
#             set([preparation_id_to_add_in])
#         )
#         print(recipe_item_id, preparation_ids)
#         # bulk_update_recipe_item_data(
#         # {
#         #     "ids": [recipe_item_id],
#         #     "attrs": {
#         #         "preparationIds": [preparation_ids]
#         #     },
#         # }
#         # )
#     return
