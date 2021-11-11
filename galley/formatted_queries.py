from typing import Dict, Optional, List

from galley.queries import get_raw_recipes_data


def ingredients_from_recipe_items(recipe_items: list) -> Optional[List]:
    ingredients = []

    for recipe_item in recipe_items:
        ingredient_object = recipe_item.get('ingredient')
        sub_recipe = recipe_item.get('subRecipe')
        preparations = recipe_item.get('preparations', [])

        # Top Level Ingredient
        if ingredient_object:
            category_values = ingredient_object.get('categoryValues', [])
            is_packaging = any(cat_val.get('name') == 'food pkg' for cat_val in category_values)

            external_name = ingredient_object.get('externalName')
            if not is_packaging and external_name not in ingredients:
                ingredients.append(external_name)

        # SubRecipe Ingredients
        elif sub_recipe:
            is_standalone = False
            item_ingredients = sub_recipe.get('allIngredients')

            if preparations:
                is_standalone = any(prep.get('name') == 'standalone' for prep in preparations)

            if not is_standalone:                    
                for ingredient in item_ingredients:
                    if ingredient not in ingredients:
                        ingredients.append(ingredient)
    
    return ingredients

def get_formatted_recipes_data(recipe_ids: list) -> Optional[List[Dict]]:
    recipes_data = get_raw_recipes_data(recipe_ids=recipe_ids) or []
    formatted_recipes = []
    
    for recipe in recipes_data:
        formatted_recipe = {}
        formatted_recipe['id'] = recipe.get('id')
        formatted_recipe['externalName'] = recipe.get('externalName')
        formatted_recipe['notes'] = recipe.get('notes')
        formatted_recipe['description'] = recipe.get('description')
        formatted_recipe['nutrition'] = recipe.get('reconciledNutritionals', {})

        recipe_category_values = recipe.get('categoryValues', [])
        for recipe_category_value in recipe_category_values:
            category_name = recipe_category_value.get('category', {}).get('name')
            category_value = recipe_category_value.get('name')
            if category_name == 'protein type':
                formatted_recipe['protein'] = category_value
            elif category_name == 'meal type':
                formatted_recipe['mealType'] = category_value
            elif category_name == 'meal container':
                formatted_recipe['mealContainer'] = category_value
            
            # TODO ENG-823: Confirm whether all recipes will have an 'is perishable' tag
            # or whether we should set a default value.
            elif category_name == 'is perishable':
                formatted_recipe['isPerishable'] = category_value == 'true'

        recipe_items = recipe.get('recipeItems', [])
        formatted_recipe['ingredients'] = ingredients_from_recipe_items(recipe_items=recipe_items)
        
        formatted_recipes.append(formatted_recipe)

    return formatted_recipes
