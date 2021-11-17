from typing import Any, Dict, Optional, List
from sgqlc.operation import Operation
from sgqlc.types import Field, Type, ArgDict

from galley.common import make_request_to_galley, validate_response_data
from galley.types import Recipe, Menu, FilterInput, MenuFilterInput
import logging

from enum import Enum

logger = logging.getLogger(__name__)

FOOD_PACKAGING = 'food pkg'
STANDALONE = 'standalone'

class MenuCategoryEnum(Enum):
    """
    Enum for categories, for item type menu <category name>: <category id>
    """
    MENU_TYPE = 'Y2F0ZWdvcnk6MjQ2NQ=='

class MenuCategoryValueEnum(Enum):
    """
    Enum for category values, <category value name>: <category value id>
    """
    PRODUCTION = 'Y2F0ZWdvcnlWYWx1ZToxNTQ2NA=='

class Viewer(Type):
    recipes = Field(Recipe, args=(ArgDict({'where': FilterInput})))
    recipe = Field(Recipe, args={'id': str})
    menus = Field(Menu, args=(ArgDict({'where': MenuFilterInput})))


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


def get_week_menu_data(dates: List[str],
                       location_name: Optional[str]="Vacaville",
                       menu_type: Optional[str]="production"
                       ) -> Optional[List[Dict]]:
    """
    Returns a list of dictionaries containing the menu data for the week.
    if there is no menu data for the week, returns None.

    :param date: The date for which the menu is to be fetched. In the form
    :param location_name: The name of the location for which the menu is to be
    fetched. ex. "Vacaville"
    :param menu_type: The type of menu to be fetched. ex. "production",
    "development"
    """
    query = Operation(Query)
    query.viewer.menus(where=MenuFilterInput(date=dates)).__fields__(
        'id', 'name', 'date', 'location', 'menuItems', 'categoryValues'
    )
    query.viewer.menus.menuItems.__fields__('recipeId', 'categoryValues',
                                            'recipe')
    query.viewer.menus.menuItems.categoryValues.__fields__('category',
                                                           'name')
    query.viewer.menus.menuItems.categoryValues.category.__fields__('name')
    query.viewer.menus.menuItems.recipe.__fields__('externalName',
                                                   'recipeItems')
    query.viewer.menus.menuItems.recipe.recipeItems.__fields__('subRecipeId',
                                                               'preparations')
    query.viewer.menus.menuItems.recipe.recipeItems.preparations\
                                                   .__fields__('name')

    validated_response_data = validate_response_data(
                make_request_to_galley(
                    op=query.__to_graphql__(auto_select_depth=3),
                    variables={'date': dates}),
                'menus')

    response = []
    if validated_response_data:
        for menu in validated_response_data:
            if menu['location']['name'] == location_name:
                categoryValues = menu['categoryValues']
                for categoryValue in categoryValues:
                    if (categoryValue['category']['id'] == MenuCategoryEnum.
                       MENU_TYPE.value and categoryValue['id'] ==
                       MenuCategoryValueEnum.PRODUCTION.value):
                        response.append(menu)
                    else:
                        continue
    return response


def get_raw_menu_data(names: List[str]) -> Optional[List[Dict]]:
    query = get_menu_data_for_date(names=names) # type: Operation
    raw_data = make_request_to_galley(op=query.__to_graphql__(auto_select_depth=3), variables={'name': names})
    return validate_response_data(raw_data, 'menus')
