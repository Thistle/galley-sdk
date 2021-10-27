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
    query.viewer().recipes().__fields__('id', 'externalName', 'instructions', 'notes', 'description')
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
