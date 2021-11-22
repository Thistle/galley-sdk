from unittest import mock, TestCase

from galley.formatted_queries import get_formatted_recipes_data, ingredients_from_recipe_items, \
    get_formatted_menu_data, weight_from_recipe_tree_components

from tests.mock_responses import mock_nutrition_data, mock_recipes_data, mock_recipe_items, mock_recipe_tree_components
from tests.mock_responses.mock_menu_data import mock_menu


class TestIngredientsFromRecipeItems(TestCase):
    def test_ingredients_from_recipes_successful(self):
        expected_result = [
            'Unique 1',
            'Duplicate 1',
            'Duplicate 2',
            'Duplicate 3',
            'Unique 2',
            'Unique 4'
        ]
        result = ingredients_from_recipe_items(mock_recipe_items.mock_data)
        self.assertEqual(result, expected_result)

    def test_ingredients_from_recipes_null(self):
        result = get_formatted_recipes_data(None)
        self.assertEqual(result, [])

    def test_ingredients_from_recipes_empty(self):
        result = ingredients_from_recipe_items([])
        self.assertEqual(result, [])

class TestWeightFromRecipeTreeComponents(TestCase):
    def test_weight_from_recipe_tree_components_with_pkg_and_standalone(self):
        expected_result = 829.22
        result = weight_from_recipe_tree_components(mock_recipe_tree_components.mock_data)
        self.assertEqual(result, expected_result)

    def test_weight_from_recipe_tree_components_successful_no_pkg_no_standalone(self):
        expected_result = 1382.04
        result = weight_from_recipe_tree_components(mock_recipe_tree_components.mock_data_no_pkg_no_standalone)
        self.assertEqual(result, expected_result)

    def test_weight_from_recipe_tree_components_empty(self):
        result = weight_from_recipe_tree_components([])
        self.assertEqual(result, 0)


class TestGetFormattedRecipesData(TestCase):
    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_successful(self, mock_retrieval_method):
        expected_result = [
            {
                'id': '1',
                'externalName': 'Test Recipe 1',
                'notes': 'Some notes about recipe 1',
                'description': 'Details about recipe 1',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'ingredients': [
                    'Unique 1',
                    'Duplicate 1',
                    'Duplicate 2',
                    'Duplicate 3',
                    'Unique 2',
                    'Unique 4'
                ],
                'weight': 829.22
            },
            {
                'id': '2',
                'externalName': 'Test Recipe 2',
                'notes': 'Some notes about recipe 2',
                'description': 'Details about recipe 2',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'ingredients': [
                    'Unique 1',
                    'Duplicate 1',
                    'Duplicate 2',
                    'Duplicate 3',
                    'Unique 2',
                    'Unique 4'
                ],
                'weight': 829.22
            }
        ]

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipes': [
                        mock_recipes_data.mock_recipe('1'),
                        mock_recipes_data.mock_recipe('2')
                    ]
                }
            }
        }
        result = get_formatted_recipes_data(['1', '2'])
        self.assertEqual(result, expected_result)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_empty(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipes': []
                }
            }
        }
        result = get_formatted_recipes_data(['1', '2'])
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_missing(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipes': None
                }
            }
        }
        result = get_formatted_recipes_data(['1', '2'])
        self.assertEqual(result, [])


class TestGetFormattedMenuData(TestCase):
    def response(self, *menus):
        return ({
            'data': {
                'viewer': {
                    'menus': [m for m in menus if m]
                }
            }
        })

    def formatted_menu(self, date):
            return ({
                'name': f"{date} 1_2_3",
                'id': 'MENU123ABC',
                'date': f"{date}",
                'location': 'Vacaville',
                'categoryMenuType': 'production',
                'menuItems': [{
                    'itemCode': 'dv1',
                    'recipeId': 'RECIPE1ABC',
                    'standaloneRecipeId': 'SUBRECIPEID456'
                }, {
                    'itemCode': 'dv2',
                    'recipeId': 'RECIPE2DEF',
                    'standaloneRecipeId': None
                }, {
                    'itemCode': 'lm2',
                    'recipeId': 'RECIPE3GHI',
                    'standaloneRecipeId': 'SUBRECIPEID321'
                }]
            })

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_successful(self, mock_retrieval_method):
        mock_retrieval_method.side_effect = [
            self.response(mock_menu('2021-11-14')),
            self.response(mock_menu('2021-11-21'), mock_menu('2021-11-21'),
                          mock_menu('2021-11-28')),
            self.response(mock_menu('2021-11-28'), mock_menu('2021-12-05')),
            self.response(mock_menu('2021-12-05')),
        ]

        # one valid menu name
        result1 = get_formatted_menu_data(['2021-11-14'])
        self.assertEqual(result1, [self.formatted_menu('2021-11-14')])

        # multiple valid menu names
        result2 = get_formatted_menu_data(['2021-11-21', '2021-11-21',
                                           '2021-11-28'])
        self.assertEqual(result2, [self.formatted_menu('2021-11-21'),
                                   self.formatted_menu('2021-11-21'),
                                   self.formatted_menu('2021-11-28')])

        # one valid menu name and one invalid menu name
        result3 = get_formatted_menu_data(['2021-11-28', '2021-12-05'])
        self.assertEqual(result3, [self.formatted_menu('2021-11-28')])

        # one invalid menu name
        result4 = get_formatted_menu_data(['2021-12-05'])
        self.assertEqual(result4, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_formatted_menu_data([])
        self.assertEqual(result, None)
    
    @mock.patch('galley.formatted_queries.get_raw_menu_data')
    def test_get_formatted_menu_data_args_defaults(self, mock_grmd):
        dates = ['2021-11-14', '2021-10-04']
        get_formatted_menu_data(dates)
        mock_grmd.assert_called_with(dates, 'Vacaville', 'production')
        get_formatted_menu_data(dates, 'Montana', 'staging')
        mock_grmd.assert_called_with(dates, 'Montana', 'staging')
