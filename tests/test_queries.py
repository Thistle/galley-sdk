from unittest import mock, TestCase
from sgqlc.operation import Operation

from galley.queries import Query, get_recipe_data, get_recipe_nutrition_data, \
    get_week_menu_data, get_recipe_ingredients, get_formatted_recipe_ingredients
from galley.types import FilterInput

import logging

logger = logging.getLogger(__name__)


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
        query_operation.viewer().recipes().__fields__('id', 'externalName', 'instructions', 'notes', 'description')
        query_str = bytes(query_operation).decode('utf-8')
        self.assertEqual(query_str, self.expected_query)

    def test_recipe_query_failure(self):
        query_operation = Operation(Query)
        query_str = bytes(query_operation).decode('utf-8')
        self.assertNotEqual(query_str, self.expected_query)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_recipe_data_successful(self, mock_retrieval_method):
        recipes = [
            {
                'id': '10000',
                'externalName': 'test recipe 1',
                'instructions': 'testing',
                'notes': 'testing notes',
                'description': 'test'
            },
            {
                'id': '10000',
                'externalName': 'test recipe 1',
                'instructions': None,
                'notes': None,
                'description': None
            }
        ]

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipes': recipes
                }
            }
        }

        result = get_recipe_data()
        self.assertEqual(result, recipes)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_recipe_data_validation_failure(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'test': 'test'
                }
            }
        }

        result = get_recipe_data()
        self.assertEqual(result, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_recipe_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_recipe_data()
        self.assertEqual(result, None)


class TestQueryRecipeNutritionData(TestCase):
    def setUp(self) -> None:
        self.expected_query = '''query {
            viewer {
            recipes(where: {id: ["cmVjaXBlOjE2NzEwOQ==", "cmVjaXBlOjE2OTEyMg==", "cmVjaXBlOjE2NTY5MA=="]}) {
            id
            externalName
            notes
            description
            categoryValues {
            name
            category {
            name
            itemType
            }
            }
            reconciledNutritionals {
            addedSugarG
            calciumMg
            calciumPercentRDI
            caloriesKCal
            carbsG
            carbsPercentDRV
            cholesterolMg
            cholesterolPercentDRV
            copperMg
            copperPercentRDI
            fiberG
            fiberPercentDRV
            folateMcg
            folatePercentRDI
            ironMg
            ironPercentRDI
            magnesiumMg
            magnesiumPercentRDI
            manganeseMg
            manganesePercentRDI
            niacinMg
            niacinPercentRDI
            pantothenicAcidMg
            phosphorusMg
            phosphorusPercentRDI
            potassiumMg
            potassiumPercentRDI
            proteinG
            proteinPercentRDI
            riboflavinMg
            riboflavinPercentRDI
            saturatedFatG
            seleniumMcg
            seleniumPercentRDI
            sodiumMg
            sodiumPercentDRV
            sugarG
            sugarPercentDRV
            thiaminMg
            thiaminPercentRDI
            totalFatG
            totalFatPercentDRV
            transFatG
            vitaminAMcg
            vitaminAPercentRDI
            vitaminB12Mcg
            vitaminB12PercentRDI
            vitaminB6Mg
            vitaminB6PercentRDI
            vitaminCMg
            vitaminCPercentRDI
            vitaminDMcg
            vitaminDPercentRDI
            vitaminEMg
            vitaminEPercentRDI
            vitaminKMcg
            vitaminKPercentRDI
            zincMg
            zincPercentRDI
            }
            }
            }
            }'''.replace(' '*12, '')

    def test_nutrition_query(self):
        query_operation = Operation(Query)
        query_operation.viewer().recipes(where=FilterInput(id=["cmVjaXBlOjE2NzEwOQ==", "cmVjaXBlOjE2OTEyMg==", "cmVjaXBlOjE2NTY5MA=="])).__fields__('id', 'externalName', 'notes', 'description', 'categoryValues', 'reconciledNutritionals')
        query_str = bytes(query_operation).decode('utf-8')
        self.assertEqual(query_str, self.expected_query)

    def test_nutrition_query_failure(self):
        query_operation = Operation(Query)
        query_str = bytes(query_operation).decode('utf-8')
        self.assertNotEqual(query_str, self.expected_query)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_recipe_nutrition_data_successful(self, mock_retrieval_method):
        def recipe(ID):
            return ({
                'id': ID,
                'externalName': f'Test Recipe {ID}',
                'notes': f'Some notes about recipe {ID}.',
                'description': f'Details about recipe {ID}.',
                'categoryValues': [
                    {
                        'name': 'vegan',
                        'category': {
                            'itemType': 'recipe',
                            'name': 'protein'
                        }
                    },
                    {
                        'name': 'TS48',
                        'category': {
                            'itemType': 'recipe',
                            'name': 'meal container'
                        }
                    },
                    {
                        'name': 'Dinner',
                        'category': {
                            'itemType': 'recipe',
                            'name': 'meal type'
                        }
                    },
                    {
                        'name': 'true',
                        'category': {
                            'itemType': 'recipe',
                            'name': 'is perishable'
                        }
                    }
                ],
                'reconciledNutritionals': {
                    'addedSugarG': 0,
                    'calciumMg': 111.98919574121712,
                    'calciumPercentRDI': 0.086,
                    'caloriesKCal': 432.85693190562375,
                    'carbsG': 36.45962786638635,
                    'carbsPercentDRV': 0.133,
                    'cholesterolMg': 0,
                    'cholesterolPercentDRV': None,
                    'copperMg': 0.5571680986811711,
                    'copperPercentRDI': 0.619,
                    'fiberG': 8.935359363694342,
                    'fiberPercentDRV': 0.319,
                    'folateMcg': 66.74783312756712,
                    'folatePercentRDI': 0.167,
                    'ironMg': 7.189047392673014,
                    'ironPercentRDI': 0.399,
                    'magnesiumMg': 129.71436209264868,
                    'magnesiumPercentRDI': 0.309,
                    'manganeseMg': 1.5268803227284646,
                    'manganesePercentRDI': 0.664,
                    'niacinMg': 2.591144920835429,
                    'niacinPercentRDI': 0.162,
                    'pantothenicAcidMg': 0.4216704338299461,
                    'phosphorusMg': 296.94409573351317,
                    'phosphorusPercentRDI': 0.238,
                    'potassiumMg': 358.1749624292856,
                    'potassiumPercentRDI': 0.076,
                    'proteinG': 9.484336690248725,
                    'proteinPercentRDI': 0.19,
                    'riboflavinMg': 0.25357865086256715,
                    'riboflavinPercentRDI': 0.195,
                    'saturatedFatG': 4.504105090278564,
                    'seleniumMcg': 25.00140713878487,
                    'seleniumPercentRDI': 0.455,
                    'sodiumMg': 259.10792677825793,
                    'sodiumPercentDRV': 0.113,
                    'sugarG': 11.64282088688695,
                    'sugarPercentDRV': None,
                    'thiaminMg': 0.22938643609988163,
                    'thiaminPercentRDI': 0.191,
                    'totalFatG': 29.331998228140108,
                    'totalFatPercentDRV': 0.376,
                    'transFatG': 0.013683867180513159,
                    'vitaminAMcg': 1.3704756299447372,
                    'vitaminAPercentRDI': 0.002,
                    'vitaminB12Mcg': 0,
                    'vitaminB12PercentRDI': None,
                    'vitaminB6Mg': 0.18718518681601845,
                    'vitaminB6PercentRDI': 0.11,
                    'vitaminCMg': 6.507446518274343,
                    'vitaminCPercentRDI': 0.072,
                    'vitaminDMcg': 0,
                    'vitaminDPercentRDI': None,
                    'vitaminEMg': 9.111428556325356,
                    'vitaminEPercentRDI': 0.607,
                    'vitaminKMcg': 0.9909650409871054,
                    'vitaminKPercentRDI': 0.008,
                    'zincMg': 1.961309534232711,
                    'zincPercentRDI': 0.178
                }
            }) if ID is not '2' else []

        def response(*recipes):
            return ({
                'data': {
                    'viewer': {
                        'recipes': [r for r in recipes if r]
                    }
                }
            })

        mock_retrieval_method.side_effect = [
            response(recipe('1')),
            response(recipe('1'), recipe('3'), recipe('4')),
            response(recipe('4')),
            response(recipe('2')),
        ]

        # test only one valid input id
        result1 = get_recipe_nutrition_data(['1'])
        self.assertEqual(result1, [recipe('1')])

        # test multiple valid input ids
        result2 = get_recipe_nutrition_data(['1', '3', '4'])
        self.assertEqual(result2, [recipe('1'), recipe('3'), recipe('4')])

        # test one valid input id and one invalid input id
        result3 = get_recipe_nutrition_data(['2', '4'])
        self.assertEqual(result3, [recipe('4')])

        # test only one invalid input string
        result4 = get_recipe_nutrition_data(['2'])
        self.assertEqual(result4, recipe('2'))

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_recipe_nutrition_data_validation_failure(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'test': 'test'
                }
            }
        }

        result = get_recipe_nutrition_data(['1'])
        self.assertEqual(result, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_nutrition_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_recipe_nutrition_data(['2'])
        self.assertEqual(result, None)


class TestQueryWeekMenuData(TestCase):
    def setUp(self) -> None:
        self.expected_query = '''query {
            viewer {
            menus(where: {name: "2021-10-04 1_2_3"}) {
            id
            name
            date
            location {
            name
            }
            menuItems {
            recipeId
            categoryValues {
            name
            category {
            name
            itemType
            }
            }
            }
            }
            }
            }'''.replace(' '*12, '')

    def test_week_menu_data_query(self):
        query_operation = Operation(Query)
        query_operation.viewer().menus(where=FilterInput(name="2021-10-04 1_2_3")).__fields__('id', 'name', 'date', 'location', 'menuItems')
        query_str = query_operation.__to_graphql__(auto_select_depth=3)
        self.assertEqual(query_str.replace(' ', ''), self.expected_query.replace(' ', ''))

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_week_menu_data_successful(self, mock_retrieval_method):
        menus = [
            {
                'name': 'YYYY-MM-DD 1_2_3',
                'id': 'MENU123ABC',
                'date': 'YYYY-MM-DD',
                'location': {
                    'name': 'Vacaville'
                },
                'menuItems': [
                    {
                        'recipeId': 'RECIPE123ABC',
                        'categoryValues': [{
                            'name': 'dv1',
                            'category': {
                                'itemType': 'menuItem',
                                'name': 'menu item type'
                            }
                        }],
                    },
                    {
                        'recipeId': 'RECIPE456DEF',
                        'categoryValues': [{
                            'name': 'dv2',
                            'category': {
                                'itemType': 'menuItem',
                                'name': 'menu item type'
                            }
                        }],
                    },
                ]
            },
        ]

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'menus': menus
                }
            }
        }

        result = get_week_menu_data('YYYY-MM-DD 1_2_3')
        self.assertEqual(result, menus)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_week_menu_data_validation_failure(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'test': 'test'
                }
            }
        }

        result = get_week_menu_data('YYYY-MM-DD 1_2_3')
        self.assertEqual(result, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_recipe_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_week_menu_data('')
        self.assertEqual(result, None)


class TestQueryRecipeIngredients(TestCase):

    def setUp(self) -> None:
        self.recipe = {
            'id': '1',
            'recipeItems': [
            {
                'ingredient': None,
                'subRecipe': {
                'allIngredients': [
                    'Unique 1',
                    'Unique 2',
                    'Duplicate 1',
                    'Duplicate 2',
                    'Duplicate 3'
                ]
                },
                'preparations': []
            },
            {
                'ingredient': None,
                'subRecipe': {
                'allIngredients': [
                    'Unique 3',
                    'Duplicate 1',
                    'Duplicate 2'                    
                ]
                },
                'preparations': []
            },
            {
                'ingredient': None,
                'subRecipe': {
                'allIngredients': [
                    'Unique 4',                               
                    'Duplicate 2',
                    'Duplicate 3'
                ]
                },
                'preparations': [
                {
                    'name': '2 oz RAM'                    
                },
                {
                    'name': 'standalone'                
                }
                ]
            },
            {
                'ingredient': {
                'externalName': 'Unique 5',
                'categoryValues': [
                    {
                    'name': 'send to plate',
                    'category': {
                        'itemType': 'ingredient'
                    }
                    },
                    {
                    'name': None,           # Test empty categoryValue['name']
                    'category': {
                        'itemType': None    # Test empty category['itemType']
                    }
                    }
                ]
                },
                'subRecipe': None,
                'preparations': [                    
                {
                    'name': None            # Test empty preparations['name']
                }
                ]
            },
            {
                'ingredient': {
                'externalName': '32 oz Meal Boxes',
                'categoryValues': [
                    {
                    'name': 'food pkg',
                    'category': {
                        'itemType': 'ingredient'
                    }
                    }
                ]
                },
                'subRecipe': None,
                'preparations': []
            },
            
            # Test empty recipeItem
            {
                'ingredient': None,
                'subRecipe': None,
                'preparations': []
            }
            ]
        }


    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_recipe_ingredients_successful(self, mock_retrieval_method):        
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipe': self.recipe
                }
            }
        }

        result = get_recipe_ingredients('1')
        self.assertEqual(result, self.recipe)


    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_recipe_ingredients_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_recipe_ingredients('2')
        self.assertEqual(result, None)


    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipe_ingredients_successful(self, mock_retrieval_method):
        expected_result = { 
            'ingredients': [
                'Unique 1',
                'Unique 2',
                'Duplicate 1',
                'Duplicate 2',
                'Duplicate 3',
                'Unique 3',
                'Unique 5'
            ],
            'standalone_ingredients': [
                'Unique 4',                               
                'Duplicate 2',
                'Duplicate 3'
            ]
        }
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipe': self.recipe
                }
            }
        }

        result = get_formatted_recipe_ingredients('1')
        self.assertEqual(result, expected_result)
    

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipe_ingredients_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_formatted_recipe_ingredients('2')
        self.assertEqual(result, None)
    
    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipe_ingredients_no_ingredients(self, mock_retrieval_method):
        expected_result = { 'ingredients': [], 'standalone_ingredients': [] }
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipe': {
                        'id': '3',
                        'recipeItems': []
                    }
                }
            }
        }

        result = get_formatted_recipe_ingredients('3')
        self.assertEqual(result, expected_result)
