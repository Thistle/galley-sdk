import csv
import logging

from collections import defaultdict
from typing import List, Dict

from galley.enums import PreparationEnum
from galley.mutations import bulk_add_preparation_to_ingredient_recipe_items, bulk_update_recipe_item_data
from galley.queries import get_ingredient_ids_by_name, get_ingredient_ids_by_search_term

logger = logging.getLogger(__name__)


def bulk_add_plating_preparation_to_send_to_plate_ingredient_usages(
    exclude_ingredient_ids: List[str] = [],
    exclude_ingredient_names: List[str] = [],
    dry_run: bool = True,
) -> None:
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
        preparation_id=PreparationEnum.PLATING_STATION.value,
        exclude_preparations=[
            PreparationEnum.WASH_STATION.value,
            PreparationEnum.BINNING_STATION.value,
        ],
        dry_run=dry_run,
    )


def add_preparations_to_recipe_items_from_dict(recipe_items_by_prep: Dict[str, List], dry_run=True) -> None:
    for prep_id, recipe_item_ids in recipe_items_by_prep.items():
        logger.warning(f"Adding preparation {PreparationEnum(prep_id).name} ({prep_id}) to {len(recipe_item_ids)} recipe_items")
        logger.warning(f"recipe_item ids: {recipe_item_ids}")

        if not dry_run:
            bulk_update_recipe_item_data(
                {
                    "ids": recipe_item_ids,
                    "attrs": {
                        "preparationIds": [prep_id]
                    },
                }
            )



def add_preparations_to_recipe_items_from_ingredient_csv(filename: str, dry_run=True) -> None:
    recipe_items = []

    with open(filename, 'r') as data:
        records = csv.DictReader(data)
        for row in records:
            recipe_items.append(row)

    items_by_prep = defaultdict(list)

    for item in recipe_items:
        if item.get('preparation') in PreparationEnum._member_names_:
            prep_id = PreparationEnum[item.get('preparation')].value
            if prep_id:
                items_by_prep[prep_id].append(item.get('recipe_item_id'))

    add_preparations_to_recipe_items_from_dict(recipe_items_by_prep=items_by_prep, dry_run=dry_run)


def add_preparations_to_recipe_items_from_recipe_csv(filename: str, dry_run=True) -> None:
    recipes = []

    with open(filename, 'r') as data:
        records = csv.DictReader(data)
        for row in records:
            recipes.append(row)

    items_by_prep = defaultdict(list)

    for recipe in recipes:
        if recipe.get('preparation') in PreparationEnum._member_names_:
            prep_id = PreparationEnum[recipe.get('preparation')].value
            if prep_id:
                items_by_prep[prep_id].extend(recipe.get('recipe_item_ids').split(','))

    add_preparations_to_recipe_items_from_dict(recipe_items_by_prep=items_by_prep, dry_run=dry_run)


