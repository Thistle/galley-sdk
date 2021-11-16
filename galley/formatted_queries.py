from typing import Dict, Optional, List

from galley.queries import get_raw_recipes_data, get_raw_menu_data
from galley.pagination import paginate_results

FOOD_PACKAGING = 'food pkg'
STANDALONE = 'standalone'


def ingredients_from_recipe_items(recipe_items: List[Dict]) -> Optional[List]:
    ingredients = []

    for recipe_item in recipe_items:
        ingredient_object = recipe_item.get('ingredient')
        sub_recipe = recipe_item.get('subRecipe')
        preparations = recipe_item.get('preparations', [])

        # Top Level Ingredient
        if ingredient_object:
            category_values = ingredient_object.get('categoryValues', [])
            is_packaging = any(cat_val.get('name') == FOOD_PACKAGING for cat_val in category_values)

            external_name = ingredient_object.get('externalName')
            if not is_packaging and external_name not in ingredients:
                ingredients.append(external_name)

        # SubRecipe Ingredients
        elif sub_recipe:
            is_standalone = False
            item_ingredients = sub_recipe.get('allIngredients')

            if preparations:
                is_standalone = any(prep.get('name') == STANDALONE for prep in preparations)

            if not is_standalone:
                for ingredient in item_ingredients:
                    if ingredient not in ingredients:
                        ingredients.append(ingredient)
    return ingredients


# Returns the subRecipeId if any 'standalone' item exists within recipeItems, else returns None
# It is assumed that there is a max of ONE standalone item within the list of recipeItems, if any.
def get_standalone(recipe_items):
    for recipe_item in recipe_items:
        preparations = recipe_item.get('preparations', [])
        is_standalone = any(prep['name'] == STANDALONE for prep in preparations)

        if is_standalone:
            return recipe_item.get('subRecipeId')
    return None


# DATA TRANSFORMATION FUNCTIONS

@paginate_results()
def get_formatted_recipes_data(recipe_ids: List[str]) -> Optional[List[Dict]]:
    recipes_data = get_raw_recipes_data(recipe_ids=recipe_ids) or []
    formatted_recipes = []

    for recipe in recipes_data:
        formatted_recipe = {
            'id': recipe.get('id'),
            'externalName': recipe.get('externalName'),
            'notes': recipe.get('notes'),
            'description': recipe.get('description'),
            'nutrition': recipe.get('reconciledNutritionals', {})
        }

        recipe_category_values = recipe.get('categoryValues', [])
        for recipe_category_value in recipe_category_values:
            category_name = recipe_category_value.get('category', {}).get('name')
            category_value = recipe_category_value.get('name')
            if category_name == 'protein type':
                formatted_recipe['proteinType'] = category_value
            elif category_name == 'meal type':
                formatted_recipe['mealType'] = category_value
            elif category_name == 'meal container':
                formatted_recipe['mealContainer'] = category_value

        recipe_items = recipe.get('recipeItems', [])
        formatted_recipe['ingredients'] = ingredients_from_recipe_items(recipe_items=recipe_items)

        formatted_recipes.append(formatted_recipe)
    return formatted_recipes


@paginate_results()
def get_formatted_menu_data(names: list) -> Optional[List[Dict]]:
    menus = get_raw_menu_data(names)
    formatted_menus = []

    if not menus:
        return None

    for menu in menus:
        formatted_menu = ({
            'name': menu.get('name'),
            'id': menu.get('id'),
            'date': menu.get('date'),
            'location': menu['location'].get('name'),
            'menuItems': []
        }) # type: Dict

        menu_items = menu.get('menuItems', [])
        for menu_item in menu_items:
            recipe_items = menu_item.get('recipe', {}).get('recipeItems', [])

            formatted_menu['menuItems'].append({
                'itemCode': next((cv.get('name') for cv in menu_item['categoryValues']), None),
                'recipeId': menu_item.get('recipeId'),
                'standaloneRecipeId': get_standalone(recipe_items)
            })

        formatted_menus.append(formatted_menu)
    return formatted_menus
