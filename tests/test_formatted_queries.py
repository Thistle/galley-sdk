from unittest import mock, TestCase

from galley.formatted_queries import get_formatted_recipes_data, ingredients_from_recipe_items, \
    get_formatted_menu_data, format_recipe_tree_components_data

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


class TestFormattedRecipeTreeComponents(TestCase):
    def test_weight_from_recipe_tree_components_with_pkg_and_standalone(self):
        expected_result = 829.22
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_data)
        self.assertEqual(result['weight'], expected_result)

    def test_weight_from_recipe_tree_components_successful_no_pkg_no_standalone(self):
        expected_result = 1382.04
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_data_no_pkg_no_standalone)
        self.assertEqual(result['weight'], expected_result)

    def test_weight_from_recipe_tree_components_empty(self):
        result = format_recipe_tree_components_data([])
        self.assertEqual(result['weight'], 0)

    def test_standalone_recipes_from_recipe_tree_components(self):
        self.maxDiff = None
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_data_standalone_recipe_item)
        expected = {
            'standaloneRecipeId': 'cmVjaXBlOjE3MDM5NA==',
            'standaloneRecipeName': 'Peanut Coconut Sauce',
            'standaloneNutrition': {
                "addedSugarG": 0,
                "calciumMg": 3.1684181569284497,
                "calciumPercentRDI": 0.002,
                "caloriesKCal": 53.66203631343362,
                "carbsG": 5.931480844736274,
                "carbsPercentDRV": 0.022,
                "cholesterolMg": 0,
                "cholesterolPercentDRV": None,
                "copperMg": 0.021694334590068795,
                "copperPercentRDI": 0.024,
                "fiberG": 0.25925700237554117,
                "fiberPercentDRV": 0.009,
                "folateMcg": 4.662944286512987,
                "folatePercentRDI": 0.012,
                "ironMg": 0.08727603182928573,
                "ironPercentRDI": 0.005,
                "magnesiumMg": 8.422029852813752,
                "magnesiumPercentRDI": 0.02,
                "manganeseMg": 0.07968240957035716,
                "manganesePercentRDI": 0.035,
                "niacinMg": 0.6287359687622166,
                "niacinPercentRDI": 0.039,
                "pantothenicAcidMg": 0.06062563923716235,
                "phosphorusMg": 16.6108569332684,
                "phosphorusPercentRDI": 0.013,
                "potassiumMg": 35.3618045624374,
                "potassiumPercentRDI": 0.008,
                "proteinG": 1.190862966668126,
                "proteinPercentRDI": 0.024,
                "riboflavinMg": 0.009900242547519483,
                "riboflavinPercentRDI": 0.008,
                "saturatedFatG": 1.1966419313881989,
                "seleniumMcg": 0.1983239364917749,
                "seleniumPercentRDI": 0.004,
                "sodiumMg": 80.1688699548479,
                "sodiumPercentDRV": 0.035,
                "sugarG": 4.635864789281829,
                "sugarPercentDRV": None,
                "thiaminMg": 0.008514061320616884,
                "thiaminPercentRDI": 0.007,
                "totalFatG": 3.2182500200225643,
                "totalFatPercentDRV": 0.041,
                "transFatG": 0.0035436903875000004,
                "vitaminAMcg": 1.449295858309044,
                "vitaminAPercentRDI": 0.002,
                "vitaminB12Mcg": 0,
                "vitaminB12PercentRDI": None,
                "vitaminB6Mg": 0.022999931273467538,
                "vitaminB6PercentRDI": 0.014,
                "vitaminCMg": 1.7259736392050762,
                "vitaminCPercentRDI": 0.019,
                "vitaminDMcg": 0,
                "vitaminDPercentRDI": None,
                "vitaminEMg": 0.4437743529419914,
                "vitaminEPercentRDI": 0.03,
                "vitaminKMcg": 0.046390128709090914,
                "vitaminKPercentRDI": 0,
                "zincMg": 0.12343713881647085,
                "zincPercentRDI": 0.011
                },
            'standaloneIngredients': [
                "Coconut Aminos (Coconut Tree Sap, Sea Salt)",
                "Lime Juice",
                "Coconut Milk (Coconut, Water, Guar Gum)",
                "Peanut Butter (Dry Roasted Peanuts)",
                "Water",
                "Sambal (Red Chile Peppers, Vinegar, Salt)",
                "Garlic"
            ],
            'standaloneWeight': 70.87,
            'weight': 156.49
        }
        self.assertEqual(result, expected)


class TestGetFormattedRecipesData(TestCase):

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_successful(self, mock_retrieval_method):
        self.maxDiff = None
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
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'ingredients': [
                    'Unique 1',
                    'Duplicate 1',
                    'Duplicate 2',
                    'Duplicate 3',
                    'Unique 2',
                    'Unique 4'
                ],
                'weight': 829.22,
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': None,
                'standaloneRecipeName': None,
                'standaloneWeight': None,
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
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'ingredients': [
                    'Unique 1',
                    'Duplicate 1',
                    'Duplicate 2',
                    'Duplicate 3',
                    'Unique 2',
                    'Unique 4'
                ],
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': None,
                'standaloneRecipeName': None,
                'standaloneWeight': None,
                'weight': 829.22
            }
        ]

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': mock_recipes_data.mock_recipe_connection(['1', '2'])                    
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
                    'recipeConnection': []
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
                    'recipeConnection': None
                }
            }
        }
        result = get_formatted_recipes_data(['1', '2'])
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_with_standalone(self, mock_retrieval_method):
        self.maxDiff = None
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': 
                        mock_recipes_data.mock_recipe_connection_with_standalone(['1'])                    
                }
            }
        }
        result = get_formatted_recipes_data(['1'])
        formatted_recipe = result[0]
        self.assertEqual(formatted_recipe['standaloneRecipeName'], 'Peanut Coconut Sauce')
        self.assertEqual(formatted_recipe['standaloneRecipeId'], 'cmVjaXBlOjE3MDM5NA==')
        self.assertEqual(formatted_recipe['standaloneWeight'], 70.87)


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
                'id': 'MENUITEM1ABC',
                'itemCode': 'dv1',
                'recipeId': 'RECIPE1ABC',
                'standaloneRecipeId': 'SUBRECIPEID456'
            }, {
                'id': 'MENUITEM2DEF',
                'itemCode': 'dv2',
                'recipeId': 'RECIPE2DEF',
                'standaloneRecipeId': None
            }, {
                'id': 'MENUITEM3GHI',
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
