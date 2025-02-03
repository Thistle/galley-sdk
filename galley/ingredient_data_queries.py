import csv

from galley.enums import LocationEnum
from galley.queries import (
    get_ingredient_usages_by_name,
    get_recipe_ids_by_name,
    get_raw_recipes_data
)

def get_candidate_usages_for_custom_preparation(ingredient_names):
    ingredient_connections = get_ingredient_usages_by_name(ingredient_names)
    included_usages = []
    excluded_usages = []
    for ingredient in ingredient_connections.get('edges', []):
        ingredient_name = ingredient.get('node', {}).get('name')
        ingredient_id = ingredient.get('node', {}).get('id')
        for usage in ingredient.get('node', {}).get('recipeItems', []):
            recipe = usage.get('recipe', {})

            # Include if the ingredient is at the top level of a sellable recipe
            if recipe.get('isDish', False):
                included_usages.append({
                    'ingredient_id': ingredient_id,
                    'ingredient_name': ingredient_name,
                    'recipe_id': recipe.get('id'),
                    'recipe_name': recipe.get('name'),
                    'recipe_link': f'https://app.galleysolutions.com/recipes/{recipe.get("id")}',
                    'note': 'Top level usage'
                })
                continue

            recipe_items = recipe.get('recipeItems', [])

            # Include if the ingredient is the only recipeItem in the recipe
            if len(recipe_items) == 1:
                included_usages.append({
                    'ingredient_id': ingredient_id,
                    'ingredient_name': ingredient_name,
                    'recipe_id': recipe.get('id'),
                    'recipe_name': recipe.get('name'),
                    'recipe_link': f'https://app.galleysolutions.com/recipes/{recipe.get("id")}',
                    'note': 'Single ingredient recipe'
                })

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
                    included_usages.append({
                        'ingredient_id': ingredient_id,
                        'ingredient_name': ingredient_name,
                        'recipe_id': recipe.get('id'),
                        'recipe_name': recipe.get('name'),
                        'recipe_link': f'https://app.galleysolutions.com/recipes/{recipe.get("id")}',
                        'note': 'Sparse recipe'
                    })
                    continue

            excluded_usages.append(usage)
    return included_usages, excluded_usages

def generate_csv_for_ingredient_usage_candidates(ingredient_names):
    included_usages, excluded_usages = get_candidate_usages_for_custom_preparation(ingredient_names)

    if len(included_usages) == 0 :
        return

    usage_candidate_file = open('preparation_candidates.csv', 'w')

    fieldnames = included_usages[0].keys()

    writer = csv.DictWriter(usage_candidate_file, fieldnames=fieldnames)
    writer.writeheader()

    for usage in included_usages:
        writer.writerow(usage)

def get_candidate_recipes_from_recipe_names(recipe_names):
    included_recipes = []
    excluded_recipes = []

    recipe_ids = get_recipe_ids_by_name(recipe_names)
    recipe_data = get_raw_recipes_data(recipe_ids=recipe_ids, location_name="burlington")

    for recipe in recipe_data:
        recipe_items = recipe.get('recipeItems', [])
        includes_subrecipe = False
        ingredients = ""
        for item in recipe_items:
            if item.get('subRecipe'):
                includes_subrecipe = True
                break
            else:
                ingredients += f"{item.get('ingredient', {}).get('name')} | "

        if includes_subrecipe:
            excluded_recipes.append(recipe)
            logger.info(f"Skipped recipe {recipe.get('id')}, {recipe.get('name')} due to subrecipe presence")
        else:
            included_recipes.append({
                'recipe_id': recipe.get('id'),
                'recipe_name': recipe.get('name'),
                'ingredients': ingredients,
                'recipe_link': f'https://app.galleysolutions.com/recipes/{recipe.get("id")}'
            })

    return included_recipes, excluded_recipes

def generate_csv_for_recipe_candidates(recipe_names):

    included_recipes, excluded_recipes = get_candidate_recipes_from_recipe_names(recipe_names)

    if len(included_recipes) == 0 :
        return

    recipe_candidate_file = open('recipe_candidates.csv', 'w')

    fieldnames = included_recipes[0].keys()

    writer = csv.DictWriter(recipe_candidate_file, fieldnames=fieldnames)
    writer.writeheader()

    for recipe in included_recipes:
        writer.writerow(recipe)
