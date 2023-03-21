import logging
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.enums import LocationEnum
from galley.queries import Query, get_menu_query, get_raw_menu_data, get_raw_recipes_data, recipe_connection_query
from tests.mock_responses.mock_recipes_data import mock_page_info, mock_recipe, mock_recipe_connection
from tests.mock_responses.mock_menu_data import mock_menu
from unittest import TestCase, mock
from sgqlc.operation import Operation, Selection


logger = logging.getLogger(__name__)


def get_argument_from_query_selector(selection: Selection, key: str):
    return selection.__args__.get(key)


class TestQueryRecipes(TestCase):
    def setUp(self) -> None:
        # This string is to test the query we build for recipe matches query provided by galley.
        self.expected_query = '''query {
            viewer {
            recipes {
            id
            externalName
            instructions
            notes
            description
            }
            }
            }'''.replace(' '*12, '')

    def test_recipe_query(self):
        query_operation = Operation(Query)
        query_operation.viewer().recipes().__fields__(
            'id', 'externalName', 'instructions', 'notes', 'description'
        )
        query_str = bytes(query_operation).decode('utf-8')
        self.assertEqual(query_str, self.expected_query)

    def test_recipe_query_failure(self):
        query_operation = Operation(Query)
        query_str = bytes(query_operation).decode('utf-8')
        self.assertNotEqual(query_str, self.expected_query)


class TestQueryWeekMenuData(TestCase):
    def response(self, *menus):
        return ({
            'data': {
                'viewer': {
                    'menus': [m for m in menus if m]
                }
            }
        })

    def test_get_raw_menu_data_should_include_dietaryFlagsWithUsages_with_locationId(self):
        query = get_menu_query(dates=["2021-10-04", "2021-10-07"], location_id=LocationEnum.VACAVILLE.value)
        arg = get_argument_from_query_selector(query.viewer.menus.menuItems.recipe.dietaryFlagsWithUsages, 'location_id')
        self.assertEqual(arg, LocationEnum.VACAVILLE.value)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_successful(self, mock_retrieval_method):
        mock_retrieval_method.side_effect = [
            self.response(mock_menu('2021-11-14')),
            self.response(mock_menu('2021-11-21'), mock_menu('2021-11-21'), mock_menu('2021-11-28')),
            self.response(mock_menu('2021-11-28'), mock_menu('2021-12-05')),
            self.response(mock_menu('2021-12-05')),
        ]

        # one valid menu name
        result1 = get_raw_menu_data(['2021-11-14'], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)
        self.assertEqual(result1, [mock_menu('2021-11-14')])

        # multiple valid menu names
        result2 = get_raw_menu_data(['2021-11-21', '2021-11-21', '2021-11-28'], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)
        self.assertEqual(result2, [mock_menu('2021-11-21'), mock_menu('2021-11-21'), mock_menu('2021-11-28')])

        # one valid menu name and one invalid menu name
        result3 = get_raw_menu_data(['2021-11-28', '2021-12-05'], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)
        self.assertEqual(result3, [mock_menu('2021-11-28')])

        # one invalid menu name
        result4 = get_raw_menu_data(['2021-12-05'], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)
        self.assertEqual(result4, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_validation_failure(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'test': 'test'
                }
            }
        }
        with self.assertRaises(ValueError):
            get_raw_menu_data(['YYYY-MM-DD'], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_exception(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        with self.assertRaises(ValueError):
            get_raw_menu_data([], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_filters_by_location(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'menus': [
                        mock_menu('2021-10-04', DEFAULT_LOCATION),
                        mock_menu('2021-10-04', 'Long Beach'),
                    ]
                }
            }
        }
        result = get_raw_menu_data(['2021-10-04'], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)
        self.assertEqual(result, [mock_menu('2021-10-04', location_name=DEFAULT_LOCATION)])
        self.assertEqual(len(result), 1)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_filter_by_menu_type(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'menus': [
                        mock_menu('2021-10-04', menu_type=DEFAULT_MENU_TYPE),
                        mock_menu('2021-10-04', menu_type='development'),
                    ]
                }
            }
        }
        result = get_raw_menu_data(['2021-10-04'], DEFAULT_LOCATION, DEFAULT_MENU_TYPE)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, [mock_menu('2021-10-04', menu_type=DEFAULT_MENU_TYPE)])


# this is the pattern going forward for testing queries
class TestRecipeConnectionQuery(TestCase):
    def test_recipe_connection_query_should_include_reconciledNutritionals_with_locationId_on_node(self):
        LOCATION_ID = 'test'
        query = recipe_connection_query(
            recipe_ids=['test-recipe-id'],
            location_id=LOCATION_ID
        )
        location_id_value = get_argument_from_query_selector(query.viewer.recipeConnection.edges.node.reconciledNutritionals, 'location_id')
        self.assertEqual(location_id_value, LOCATION_ID)

    def test_recipe_connection_query_should_include_reconciledNutritionals_with_locationId_on_recipeItems_subRecipe(self):
        LOCATION_ID = 'test'
        query = recipe_connection_query(
            recipe_ids=['test-recipe-id'],
            location_id=LOCATION_ID
        )
        location_id_value = get_argument_from_query_selector(query.viewer.recipeConnection.edges.node.recipeItems.subRecipe.reconciledNutritionals, 'location_id')
        self.assertEqual(location_id_value, LOCATION_ID)

    def test_recipe_connection_query_should_include_dietaryFlagsWithUsages_with_locationId(self):
        LOCATION_ID = 'test'
        query = recipe_connection_query(
            recipe_ids=['test-recipe-id'],
            location_id=LOCATION_ID
        )
        location_id_value = get_argument_from_query_selector(query.viewer.recipeConnection.edges.node.dietaryFlagsWithUsages, 'location_id')
        self.assertEqual(location_id_value, LOCATION_ID)

    def test_recipe_connection_query_should_include_locationVendorItems_with_locationIds_on_recipeItem(self):
        LOCATION_ID = 'test'
        query = recipe_connection_query(
            recipe_ids=['test-recipe-id'],
            location_id=LOCATION_ID
        )
        location_id_value = get_argument_from_query_selector(query.viewer.recipeConnection.edges.node.recipeItems.ingredient.locationVendorItems, 'location_ids')
        self.assertEqual(location_id_value, [LOCATION_ID])

    def test_recipe_connection_query_should_include_locationVendorItems_with_locationIds_on_ingredientsWithUsages(self):
        LOCATION_ID = 'test'
        query = recipe_connection_query(
            recipe_ids=['test-recipe-id'],
            location_id=LOCATION_ID
        )
        location_id_value = get_argument_from_query_selector(query.viewer.recipeConnection.edges.node.ingredientsWithUsages.ingredient.locationVendorItems, 'location_ids')
        self.assertEqual(location_id_value, [LOCATION_ID])


class TestQueryGetRawRecipesData(TestCase):
    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_data_successful(self, mock_retrieval_method):
        recipe_connection_data = mock_recipe_connection(['1'])
        expected_recipe_data = [mock_recipe('1')]
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': recipe_connection_data
                }
            }
        }
        result = get_raw_recipes_data(recipe_ids=['1'], location_name=DEFAULT_LOCATION)
        self.assertEqual(result, expected_recipe_data)

    def test_should_throw_error_if_location_is_not_ours(self):
        with self.assertRaises(ValueError):
            get_raw_recipes_data(recipe_ids=[], location_name="TestLocation")

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_edges_empty(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': []
                    },
                    'pageInfo': mock_page_info()
                }
            }
        }
        result = get_raw_recipes_data(recipe_ids=['Fake'], location_name=DEFAULT_LOCATION)
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_node_empty(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': {}
                        }]
                    },
                    'pageInfo': mock_page_info()
                }
            }
        }
        result = get_raw_recipes_data(recipe_ids=['Fake'], location_name=DEFAULT_LOCATION)
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_data_missing(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': None
                }
            }
        }
        result = get_raw_recipes_data(recipe_ids=['Fake'], location_name=DEFAULT_LOCATION)
        self.assertEqual(result, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_multiple_pages(self, mock_retrieval_method):
        # Mocking 2 pages with with a 2 recipe limit
        page_1 = mock_recipe_connection(
            ['1', '2'],
            has_previous_page=False,
            has_next_page=True,
            start_index=0,
            end_index=2
        )
        page_2 = mock_recipe_connection(
            ['3'],
            has_previous_page=True,
            has_next_page=False,
            start_index=2,
            end_index=3
        )
        expected_recipe_data = list(map(mock_recipe, ['1', '2', '3']))
        mock_retrieval_method.side_effect = [
            {
                'data': {
                    'viewer': {
                        'recipeConnection': page_1
                    }
                }
            },
            {
                'data': {
                    'viewer': {
                        'recipeConnection': page_2
                    }
                }
            }
        ]
        result = get_raw_recipes_data(recipe_ids=['1', '2', '3'], location_name=DEFAULT_LOCATION)
        self.assertEqual(mock_retrieval_method.call_count, 2)
        self.assertEqual(result, expected_recipe_data)
