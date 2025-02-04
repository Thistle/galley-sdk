import csv
import logging

from typing import Any, Dict, List, Optional, Tuple
from galley.enums import LocationEnum
from galley.queries import (
    get_ingredient_usages_by_name,
    get_recipe_ids_by_name,
    get_raw_recipes_data
)


logger = logging.getLogger(__name__)


# This script finds usages of given ingredients that might be processed
# by a different team than Kitchen (e.g. Production in Burlington)
def get_candidate_usages_for_custom_preparation(ingredient_names: List[str]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    usages_by_ingredient_id = get_ingredient_usages_by_name(ingredient_names=ingredient_names)

    included_usages = []
    excluded_usages = []
    for ingredient_id, ingredient_usages in usages_by_ingredient_id.items():
        for usage in ingredient_usages:
            ingredient_name = usage.get('ingredient_name')
            recipe = usage.get('recipe', {})

            usage_data = {
                'ingredient_id': ingredient_id,
                'ingredient_name': ingredient_name,
                'recipe_item_id': usage.get('id'),
                'recipe_id': recipe.get('id'),
                'recipe_name': recipe.get('name'),
                'recipe_link': f'https://app.galleysolutions.com/recipes/{recipe.get("id")}',
            }

            # Include if the ingredient is at the top level of a sellable recipe or BASE recipe
            if recipe.get('isDish', False) or 'BASE' in recipe.get('name', ''):
                usage_data['note'] = 'Top level usage'
                included_usages.append(usage_data)
                continue

            recipe_items = recipe.get('recipeItems', [])

            # Include if the ingredient is the only recipeItem in the recipe
            if len(recipe_items) == 1:
                usage_data['note'] = 'Single ingredient recipe'
                included_usages.append(usage_data)
                continue

            # Include if this recipe includes only a small number of
            # ingredients and no subrecipes
            if len(recipe_items) < 5:
                includes_subrecipe = False
                for item in recipe_items:
                    if item.get('subRecipe'):
                        includes_subrecipe = True
                        break

                if not includes_subrecipe:
                    usage_data['note'] = 'Sparse recipe'
                    included_usages.append(usage_data)
                    continue

            excluded_usages.append(usage)
    return included_usages, excluded_usages

# Generic List[Dict] -> csv script
def generate_csv_from_dict_list(data_list: List[Dict[str, Any]], filename: str) -> None:
    if len(data_list) == 0:
        logger.info("No csv generated, no data provided")
        return

    file = open(filename, 'w')
    field_names = data_list[0].keys()

    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()

    for data in data_list:
        writer.writerow(data)

# This script generates a csv of ingredient usages potentially processed by a
# team other than Kitchn
def generate_csv_for_ingredient_usage_candidates(ingredient_names: List[str]) -> None:
    included_usages, excluded_usages = get_candidate_usages_for_custom_preparation(ingredient_names)
    generate_csv_from_dict_list(included_usages, 'preparation_candidates.csv')


# This script retrieves relevant data from a recipe to determine if
# it might be processed by a different team than Kitchen
def get_candidate_recipes_from_recipe_names(recipe_names: List[str]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]] :
    included_recipes = []
    excluded_recipes = []

    recipe_ids = get_recipe_ids_by_name(recipe_names)
    recipe_data = get_raw_recipes_data(recipe_ids=recipe_ids, location_name="burlington")

    for recipe in recipe_data:
        recipe_items = recipe.get('recipeItems', [])
        includes_subrecipe = False
        ingredients = ""
        recipe_item_ids = []
        for item in recipe_items:
            if item.get('subRecipe'):
                includes_subrecipe = True
                break
            else:
                ingredients += f"{item.get('ingredient', {}).get('name')} | "
                recipe_item_ids.append(item.get('id'))

        if includes_subrecipe:
            excluded_recipes.append(recipe)
            logger.info(f"Skipped recipe {recipe.get('id')}, {recipe.get('name')} due to subrecipe presence")
        else:
            included_recipes.append({
                'recipe_id': recipe.get('id'),
                'recipe_name': recipe.get('name'),
                'recipe_item_ids': ','.join(recipe_item_ids),
                'ingredients': ingredients,
                'recipe_link': f'https://app.galleysolutions.com/recipes/{recipe.get("id")}'
            })

    return included_recipes, excluded_recipes


# Generates a csv of relevant recipe data to determine whether a recipe
# could be processed by a team other than Kitchen
def generate_csv_for_recipe_candidates(recipe_names: List[str]) -> None:
    included_recipes, excluded_recipes = get_candidate_recipes_from_recipe_names(recipe_names)
    generate_csv_from_dict_list(included_recipes, 'recipe_candidates.csv')
