import logging
from unittest import TestCase, mock
from galley.enums import LocationEnum
from galley.queries import (get_ops_menu_query,
                            get_ops_recipe_item_connection_query,
                            get_raw_recipe_items_data_via_connection)
from tests.test_queries import get_argument_from_query_selector


logger = logging.getLogger(__name__)


class TestOpsMenuDataQuery(TestCase):
    def test_get_ops_menu_query_should_include_locationVendorItems_with_locationId(self):
        query = get_ops_menu_query(dates=["2022-03-28"], location_id=LocationEnum.VACAVILLE.value)
        arg = get_argument_from_query_selector(
            query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.ingredient.locationVendorItems,
            'location_ids'
        )
        self.assertEqual(arg, [LocationEnum.VACAVILLE.value])

    def test_get_ops_menu_query_should_include_dietaryFlagsWithUsages_with_locationId(self):
        query = get_ops_menu_query(dates=["2022-03-28"], location_id=LocationEnum.VACAVILLE.value)
        arg = get_argument_from_query_selector(
            query.viewer.menus.menuItems.recipe.recipeTreeComponents.recipeItem.subRecipe.dietaryFlagsWithUsages,
            'location_id'
        )
        self.assertEqual(arg, LocationEnum.VACAVILLE.value)


class TestOpsRecipeItemConnectionQuery(TestCase):
    def setUp(self) -> None:
        self.data = {
            'WRONGID==': None,
            'cmVjaXBlOjE3NjQxNA==': {'edges': [{'node': {'id': 'cmVjaXBlSXRlbToxMTUwNDY5', 'recipeId': 'cmVjaXBlOjE3NjQyMw==', 'preparations': [{'id': 'cHJlcGFyYXRpb246MzEzNjk=', 'name': 'Core Recipe'}]}}, {'node': {'id': 'cmVjaXBlSXRlbToxMTUwNDE3', 'recipeId': 'cmVjaXBlOjE3NjQxMw==', 'preparations': [{'id': 'cHJlcGFyYXRpb246MzEzNjk=', 'name': 'Core Recipe'}]}}]},
            'cmVjaXBlOjIwMjI5NA==': {'edges': [{'node': {'id': 'cmVjaXBlSXRlbToxMjkwMjAw', 'recipeId': 'cmVjaXBlOjIwMjMwNQ==', 'preparations': []}}, {'node': {'id': 'cmVjaXBlSXRlbToxMjkwMTgx', 'recipeId': 'cmVjaXBlOjIwMjMwMA==', 'preparations': []}}]},
        }

        self.expected_query = '''query {
            viewer {
            recipeItemConnection(filters: {subRecipeIds: ["cmVjaXBlOjIwMjI5NA=="]}) {
            edges {
            node {
            id
            recipeId
            preparations {
            id
            name
            }
            }
            }
            }
            }
            }'''.replace(' '*12, '')

    def response(self, *data):
        return ({
            'data': {
                'viewer': {
                    'recipeItemConnection': data
                }
            }
        })

    def test_get_ops_recipe_item_connection_query(self):
        query = get_ops_recipe_item_connection_query(sub_recipe_ids=["cmVjaXBlOjIwMjI5NA=="])
        query_str = bytes(query).decode('utf-8')
        self.maxDiff = None
        self.assertEqual(query_str, self.expected_query)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipe_items_data_via_connection_successful(self, mock_retrieval_method):
        mock_retrieval_method.side_effect = [
            self.response(self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['cmVjaXBlOjE3NjQxNA=='], self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['WRONGID=='], self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['WRONGID==']),
        ]

        self.maxDiff = None

        # one valid menu name
        result1 = get_raw_recipe_items_data_via_connection(["cmVjaXBlOjIwMjI5NA=="])
        self.assertEqual(result1, (self.data["cmVjaXBlOjIwMjI5NA=="],))

        # multiple valid menu names
        result2 = get_raw_recipe_items_data_via_connection(['cmVjaXBlOjIwMjI5NA==', 'cmVjaXBlOjE3NjQxNA=='])
        self.assertEqual(result2, (self.data['cmVjaXBlOjE3NjQxNA=='],
                                   self.data['cmVjaXBlOjIwMjI5NA==']))

        # one valid menu name and one invalid menu name
        result3 = get_raw_recipe_items_data_via_connection(['WRONGID==', 'cmVjaXBlOjE3NjQxNA=='])
        self.assertEqual(result3, (None, self.data['cmVjaXBlOjIwMjI5NA=='],))

        # one invalid menu name
        result4 = get_raw_recipe_items_data_via_connection(['WRONGID=='])
        self.assertEqual(result4, (None,))
