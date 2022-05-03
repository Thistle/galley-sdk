from unittest import TestCase, mock

from galley.formatted_queries import (
    get_category_menu_type,
    get_meal_code
)
from galley.formatted_ops_queries import get_formatted_ops_menu_data

from tests.mock_responses.mock_ops_menu_data import (
    mock_ops_menu,
    mock_recipeTreeComponents,
    mock_formatted_primaryRecipeComponents,
)


def formatted_ops_menu(date, location_name='Vacaville', menu_type='production'):
    formatted_ops_menu = {
        'name': f'{date} 1_2_3',
        'id': 'MENU123ABC-OPS',
        'date': f'{date}',
        'location': location_name,
        'categoryMenuType': menu_type,
        'menuItems': [{
            'mealCode': 'lm1',
            'recipeId': 'RECIPE1ABC-OPS',
            'recipeName': 'Test Recipe Name 1',
            'mealContainer': 'ts48',
            'platePhotoUrl': 'https://cdn.filestackcontent.com/2X5ivrEYQvuEh30DyYot',
            'totalCount': 923,
            'primaryRecipeComponents': mock_formatted_primaryRecipeComponents,

        }, {
            'mealCode': 'lv2',
            'recipeId': 'RECIPE2DEF-OPS',
            'recipeName': 'Test Recipe Name 2',
            'mealContainer': 'ts32',
            'platePhotoUrl': 'https://cdn.filestackcontent.com/IQM3KcAkRye81xuN5JY4',
            'totalCount': 1228,
            'primaryRecipeComponents': mock_formatted_primaryRecipeComponents,

        }, {
            'mealCode': 'dv3',
            'recipeId': 'RECIPE3GHI-OPS',
            'recipeName': 'Test Recipe Name 3',
            'mealContainer': 'ts32',
            'platePhotoUrl': None,
            'totalCount': 549,
            'primaryRecipeComponents': mock_formatted_primaryRecipeComponents,

        }]
    }
    return formatted_ops_menu


class TestMealCodeFromMenuItemCategoryValues(TestCase):
    def test_get_meal_code_successful(self):
        expected_result = 'lv2'
        result = get_meal_code(mock_ops_menu('2022-03-28')['menuItems'][1]['categoryValues'])
        self.assertEqual(result, expected_result)

    def test_get_meal_code_empty(self):
        result = get_meal_code([])
        self.assertEqual(result, '')


class TestGetMenuTypeFromMenuCategoryValues(TestCase):
    def test_get_category_menu_type_successful(self):
        expected_result = 'production'
        result = get_category_menu_type(mock_ops_menu('2022-03-28')['categoryValues'])
        self.assertEqual(result, expected_result)

    def test_get_category_menu_type_empty(self):
        result = get_category_menu_type([])
        self.assertEqual(result, '')


class TestGetFormattedOpsMenuData(TestCase):
    def response(self, *menus):
        return ({
            'data': {
                'viewer': {
                    'menus': [m for m in menus if m]
                }
            }
        })

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_successful_for_one_valid_menu(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_ops_menu('2022-03-28'))
        result = get_formatted_ops_menu_data(['2022-03-28'])
        self.assertEqual(result, [formatted_ops_menu('2022-03-28')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_successful_for_multiple_valid_menus(self, mock_retrieval_method):
        self.maxDiff = None
        mock_retrieval_method.return_value = self.response(mock_ops_menu('2022-03-28'), mock_ops_menu('2022-04-04'), mock_ops_menu('2022-04-18'))
        result = get_formatted_ops_menu_data(['2022-03-28', '2022-04-04', '2022-04-18'])
        self.assertEqual(result, [formatted_ops_menu('2022-03-28'), formatted_ops_menu('2022-04-04'), formatted_ops_menu('2022-04-18')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_formatted_ops_menu_data([])
        self.assertEqual(result, None)

    @mock.patch('galley.formatted_ops_queries.get_raw_menu_data')
    def test_get_formatted_ops_menu_data_args_defaults(self, mock_gromd):
        dates = ['2022-03-28', '2022-04-04']
        get_formatted_ops_menu_data(dates)
        mock_gromd.assert_called_with(dates, 'Vacaville', 'production', is_ops=True)
        get_formatted_ops_menu_data(dates, 'Montana', 'staging')
        mock_gromd.assert_called_with(dates, 'Montana', 'staging', is_ops=True)


