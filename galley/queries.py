from typing import Any, Dict, Optional, List
from sgqlc.operation import Operation
from sgqlc.types import Field, Type, ArgDict

from galley.common import make_request_to_galley, validate_response_data
from galley.types import Recipe, Menu, FilterInput
import logging

logger = logging.getLogger(__name__)

FOOD_PACKAGING = 'food pkg'
STANDALONE = 'standalone'


class Viewer(Type):
    recipes = Field(Recipe, args=(ArgDict({'where': FilterInput})))
    recipe = Field(Recipe, args={'id': str})
    menus = Field(Menu, args=(ArgDict({'where': FilterInput})))


# This is graphql root for querying data according to sgqlc lib. So this class name has to be Query.
class Query(Type):
    viewer = Field(Viewer)

    @staticmethod
    def recipe_data_struct() -> Dict:
        return {
            'data': {
                'viewer': {
                    'recipes': [{
                        'id': str,
                        'externalName': str,
                        'instructions': Any,
                        'notes': Any,
                        'description': Any
                    }]
                }
            }
        }


# RECIPE QUERIES

def get_recipe_data() -> Optional[List[Dict]]:
    # Initiate a query
    query = Operation(Query)
    # Call sub-type you need to build the query.
    query.viewer.recipes.__fields__(
        'id', 'externalName', 'instructions', 'notes', 'description'
    )
    # pass query as an argument to make_request_to_galley function.
    raw_data = make_request_to_galley(op=query)
    return validate_response_data(raw_data, 'recipes')


def get_recipe_nutrition_data(recipe_ids: list) -> Optional[List[Dict]]:
    query = Operation(Query)
    query.viewer.recipes(where=FilterInput(id=recipe_ids)).__fields__(
        'id', 'externalName', 'notes', 'description', 'categoryValues', 'reconciledNutritionals'
    )
    raw_data = make_request_to_galley(op=query, variables={'id': recipe_ids})
    return validate_response_data(raw_data, 'recipes')


def get_week_menu_data(names: list) -> Optional[List[Dict]]:
    query = Operation(Query)
    query.viewer.menus(where=FilterInput(name=names)).__fields__(
        'id', 'name', 'date', 'location', 'menuItems'
    )
    query.viewer.menus.menuItems.__fields__('recipeId', 'categoryValues', 'recipe')
    query.viewer.menus.menuItems.recipe.__fields__('externalName', 'recipeItems')
    query.viewer.menus.menuItems.recipe.recipeItems.__fields__('subRecipeId', 'preparations')
    query.viewer.menus.menuItems.recipe.recipeItems.preparations.__fields__('name')
    raw_data = make_request_to_galley(op=query.__to_graphql__(auto_select_depth=3), variables={'name': names})
    return validate_response_data(raw_data, 'menus')


def get_recipe_ingredients(recipe_id) -> Optional[Dict]:
    query = Operation(Query)
    query.viewer.recipe(id=recipe_id).__fields__('id', 'recipeItems')
    query.viewer.recipe.recipeItems.__fields__('ingredient', 'subRecipe', 'preparations')
    query.viewer.recipe.recipeItems.ingredient.__fields__('externalName', 'categoryValues')
    query.viewer.recipe.recipeItems.ingredient.categoryValues.__fields__('name')
    raw_data = make_request_to_galley(op=query, variables={'id': recipe_id})
    return validate_response_data(raw_data, 'recipe')


# Returns a Dict of main recipe ingredients and ingredients of standalone components
# { 'main_ingredients': [], 'standalone_components': [] }
# Ingredients within each list are de-duped. Packaging 'ingredients' are disregarded.
def get_formatted_recipe_ingredients(recipe_id) -> Optional[Dict]:
    recipe_ingredients_data = get_recipe_ingredients(recipe_id)
    if recipe_ingredients_data:
        recipe_items = recipe_ingredients_data.get('recipeItems', [])
        main_ingredients = []
        standalone_ingredients = []

        for recipe_item in recipe_items:
            ingredient_object = recipe_item.get('ingredient')
            sub_recipe = recipe_item.get('subRecipe')
            preparations = recipe_item.get('preparations', [])

            # Top Level Ingredient
            if ingredient_object:
                category_values = ingredient_object.get('categoryValues', [])
                is_packaging = any(cat_val.get('name') == FOOD_PACKAGING for cat_val in category_values)

                external_name = ingredient_object.get('externalName')
                if not is_packaging and external_name not in main_ingredients:
                    main_ingredients.append(external_name)

            # SubRecipe Ingredients
            elif sub_recipe:
                is_standalone = False
                item_ingredients = sub_recipe.get('allIngredients')

                if preparations:
                    is_standalone = any(prep.get('name') == STANDALONE for prep in preparations)

                if is_standalone:
                    for ingredient in item_ingredients:
                        if ingredient not in standalone_ingredients:
                            standalone_ingredients.append(ingredient)
                else:
                    for ingredient in item_ingredients:
                        if ingredient not in main_ingredients:
                            main_ingredients.append(ingredient)

        return {'ingredients': main_ingredients, 'standalone_ingredients': standalone_ingredients}
    else:
        return None
