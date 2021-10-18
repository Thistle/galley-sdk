from typing import Any, Dict, Optional, List
from sgqlc.operation import Operation
from sgqlc.types import Field, Type, ArgDict

from galley.common import make_request_to_galley, validate_response_data
from galley.types import Recipe, Menu, MenuNameInput
import logging

logger = logging.getLogger(__name__)


class Viewer(Type):
    recipes = Field(Recipe)
    recipe = Field(Recipe, args={'id': str})
    menus = Field(Menu, args=(ArgDict({'where': MenuNameInput})))


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
                        'name': str,
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
    query.viewer().recipes().__fields__('id', 'name', 'instructions', 'notes', 'description')
    # pass query as an argument to make_request_to_galley function.
    raw_data = make_request_to_galley(op=query)
    return validate_response_data(raw_data, 'recipes')


def get_recipe_nutrition_data(recipe_id) -> Optional[List[Dict]]:
    query = Operation(Query)
    query.viewer().recipe(id=recipe_id).__fields__('id', 'name', 'calculatedNutritionals')
    raw_data = make_request_to_galley(op=query, variables={'id': recipe_id})
    return validate_response_data(raw_data, 'recipe')


def get_week_menu_data(name):
    query = Operation(Query)
    query.viewer().menus(where=MenuNameInput(name=name)).__fields__('id', 'name', 'date', 'location', 'menuItems')
    raw_data = make_request_to_galley(op=query.__to_graphql__(auto_select_depth=3), variables={'name': name})
    return validate_response_data(raw_data, 'menus')
