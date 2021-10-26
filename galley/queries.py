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
    query.viewer.recipes().__fields__('id', 'externalName', 'instructions', 'notes', 'description')
    # pass query as an argument to make_request_to_galley function.
    raw_data = make_request_to_galley(op=query)
    return validate_response_data(raw_data, 'recipes')


def get_recipe_nutrition_data(recipe_ids: list) -> Optional[List[Dict]]:
    query = Operation(Query)
    query.viewer().recipes(where=FilterInput(id=recipe_ids)).__fields__('id', 'externalName', 'notes', 'description', 'categoryValues', 'reconciledNutritionals')
    raw_data = make_request_to_galley(op=query, variables={'id': recipe_ids})
    return validate_response_data(raw_data, 'recipes')


def get_week_menu_data(name: str) -> Optional[List[Dict]]:
    query = Operation(Query)
    query.viewer().menus(where=FilterInput(name=name)).__fields__('id', 'name', 'date', 'location', 'menuItems')
    raw_data = make_request_to_galley(op=query.__to_graphql__(auto_select_depth=3), variables={'name': name})
    return validate_response_data(raw_data, 'menus')


def get_recipe_ingredients(recipe_id) -> Optional[List[Dict]]:
    query = Operation(Query)
    query.viewer.recipe(id=recipe_id).__fields__('id', 'recipeItems')
    query.viewer.recipe.recipeItems.__fields__('ingredient', 'subRecipe', 'preparations')
    query.viewer.recipe.recipeItems.ingredient.__fields__('externalName', 'categoryValues')
    query.viewer.recipe.recipeItems.ingredient.categoryValues.__fields__('name')
    raw_data = make_request_to_galley(op=query, variables={'id': recipe_id})
    return validate_response_data(raw_data, 'recipe')

# Returns a Dict of main recipe ingredients and ingredients of standalone components
# { ingredients: [], standalone_components: [] }
# Ingredients within each list are de-duped. Packaging 'ingredients' are disregarded.
def get_formatted_recipe_ingredients(recipe_id) -> Optional[Dict]:
    recipe_ingredients_data = get_recipe_ingredients(recipe_id)
    if recipe_ingredients_data:
        recipe_items = recipe_ingredients_data['recipeItems']
        ingredients = []
        standalone_ingredients = []

        for recipe_item in recipe_items:

            # Top Level Ingredient
            if recipe_item['ingredient']:
                category_values = recipe_item['ingredient']['categoryValues']
                is_packaging = next((True for cval in category_values if cval['name'] == FOOD_PACKAGING), False)

                if not is_packaging and recipe_item['ingredient']['externalName'] not in ingredients: 
                    ingredients.append(recipe_item['ingredient']['externalName'])

            # SubRecipe Ingredients
            elif recipe_item['subRecipe']:                    
                is_standalone = False
                item_ingredients = recipe_item['subRecipe']['allIngredients']
                preparations = recipe_item['preparations']
            
                if preparations:
                    is_standalone = next((True for prep in preparations if prep['name'] == STANDALONE), False)                        

                if is_standalone:
                    for ingredient in item_ingredients:
                        if ingredient not in standalone_ingredients:
                            standalone_ingredients.append(ingredient)
                else:        
                    for ingredient in item_ingredients:
                        if ingredient not in ingredients:
                            ingredients.append(ingredient)

        return {'ingredients': ingredients, 'standalone_ingredients': standalone_ingredients}
    else:
        return None
