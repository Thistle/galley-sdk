from unittest import mock, TestCase

from galley.formatted_queries import get_formatted_recipes_data, ingredients_from_recipe_items

from tests.mock_responses import mock_nutrition_data, mock_recipes_data, mock_recipe_items


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


class TestGetFormattedRecipesData(TestCase):

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_successful(self, mock_retrieval_method):
        expected_result = [
            {
                'id': '1',
                'externalName': 'Test Recipe 1',
                'notes': 'Some notes about recipe 1',
                'description': 'Details about recipe 1',
                'protein': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'isPerishable': True,
                'ingredients': [
                    'Unique 1',
                    'Duplicate 1',                    
                    'Duplicate 2',
                    'Duplicate 3',
                    'Unique 2',
                    'Unique 4'
                ],
                'nutrition': mock_nutrition_data.mock_data            
            },
            {
                'id': '2',
                'externalName': 'Test Recipe 2',
                'notes': 'Some notes about recipe 2',
                'description': 'Details about recipe 2',
                'protein': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'isPerishable': True,
                'ingredients': [
                    'Unique 1',
                    'Duplicate 1',
                    'Duplicate 2',
                    'Duplicate 3',
                    'Unique 2',
                    'Unique 4'
                ],
                'nutrition': mock_nutrition_data.mock_data            
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

        result = get_formatted_recipes_data(['1'])
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

        result = get_formatted_recipes_data(['1'])
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

        result = get_formatted_recipes_data(['1'])
        self.assertEqual(result, [])
