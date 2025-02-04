from typing import List

from galley.enums import PreparationEnum
from galley.mutations import bulk_add_preparation_to_ingredient_recipe_items
from galley.queries import get_ingredient_ids_by_name, get_ingredient_ids_by_search_term


def bulk_add_plating_preparation_to_send_to_plate_ingredient_usages(
    exclude_ingredient_ids: List[str] = [],
    exclude_ingredient_names: List[str] = [],
    dry_run: bool = True,
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
        preparation_id=PreparationEnum.PLATING_STATION.value,
        exclude_preparations=[
            PreparationEnum.WASH_STATION.value,
            PreparationEnum.BINNING_STATION.value,
        ],
        dry_run=dry_run,
    )
