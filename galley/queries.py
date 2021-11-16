from typing import Any, Dict, Optional, List
from sgqlc.operation import Operation
from sgqlc.types import Field, Type, ArgDict

from galley.common import make_request_to_galley, validate_response_data
from galley.types import Recipe, Menu, FilterInput
import logging

logger = logging.getLogger(__name__)


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


def recipes_data_query(recipe_ids: List[str]) -> Optional[Operation]:
    query = Operation(Query)
    query.viewer.recipes(where=FilterInput(id=recipe_ids)).__fields__(
        'id', 'externalName', 'notes', 'description', 'categoryValues', 'reconciledNutritionals', 'recipeItems'
    )
    query.viewer.recipe.recipeItems.__fields__('ingredient', 'subRecipe', 'preparations')
    query.viewer.recipe.recipeItems.ingredient.__fields__('externalName', 'categoryValues')
    query.viewer.recipe.recipeItems.ingredient.categoryValues.__fields__('name')
    return query


def get_raw_recipes_data(recipe_ids: List[str]) -> Optional[List[Dict]]:
    query = recipes_data_query(recipe_ids=recipe_ids)
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


def get_formatted_menu_data(names: list) -> Optional[List[Dict]]:
    menus = get_week_menu_data(names)
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


# Returns the subRecipeId if any 'standalone' item exists within recipeItems, else returns None
# It is assumed that there is a max of ONE standalone item within the list of recipeItems, if any.
def get_standalone(recipe_items):
    for recipe_item in recipe_items:
        preparations = recipe_item.get('preparations', [])
        is_standalone = any(prep['name'] == 'standalone' for prep in preparations)

        if is_standalone:
            return recipe_item.get('subRecipeId')
    return None
