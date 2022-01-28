from unittest import TestCase, mock

from galley.formatted_queries import (format_recipe_tree_components_data,
                                      get_formatted_menu_data,
                                      get_formatted_recipes_data,
                                      ingredients_from_recipe_items,
                                      calculate_servings,
                                      calculate_serving_size_weight)

from tests.mock_responses import (mock_nutrition_data, mock_recipe_items,
                                  mock_recipe_tree_components,
                                  mock_recipes_data)
from tests.mock_responses.mock_menu_data import mock_menu


def formatted_menu(date):
    return ({
        'name': f"{date} 1_2_3",
        'id': 'MENU123ABC',
        'date': f"{date}",
        'location': 'Vacaville',
        'categoryMenuType': 'production',
        'menuItems': [{
            'baseMeal': '',
            'id': 'MENUITEM1ABC',
            'itemCode': 'dv1',
            'mealSlug': 'test-recipe-name-1',
            'recipeId': 'RECIPE1ABC',
            'recipeMealType': 'dinner',
            'recipeMenuPhotoUrl': None,
            'recipeName': 'Test Recipe Name 1',
            'recipeProteinType': 'vegan',
            'standaloneRecipeId': 'SUBRECIPEID456'
        }, {
            'baseMeal': '',
            'id': 'MENUITEM2DEF',
            'itemCode': 'dv2',
            'mealSlug': 'test-recipe-name-2',
            'recipeId': 'RECIPE2DEF',
            'recipeMealType': 'dinner',
            'recipeMenuPhotoUrl': None,
            'recipeName': 'Test Recipe Name 2',
            'recipeProteinType': 'vegan',
            'standaloneRecipeId': None
        }, {
            'baseMeal': '',
            'id': 'MENUITEM3GHI',
            'itemCode': 'lm2',
            'mealSlug': 'test-recipe-name-3',
            'recipeId': 'RECIPE3GHI',
            'recipeMealType': 'lunch',
            'recipeMenuPhotoUrl': None,
            'recipeName': 'Test Recipe Name 3',
            'recipeProteinType': 'meat',
            'standaloneRecipeId': 'SUBRECIPEID321'
        }]
    })


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


class TestCalculateServings(TestCase):
    def test_calculate_servings_sucessful_with_expected_data(self):
        expected_result = 2.5
        result = calculate_servings(2.5, 1.0)
        self.assertEqual(result, expected_result)

    def test_calculate_servings_returns_None_if_usage_quantity_missing(self):
        expected_result = None
        result = calculate_servings(None, 1.0)
        self.assertEqual(result, expected_result)

    def test_calculate_servings_returns_None_if_nutritionals_quantity_missing(self):
        expected_result = None
        result = calculate_servings(2.5, None)
        self.assertEqual(result, expected_result)


class TestCalculateServingSizeWeight(TestCase):
    def test_calculate_serving_size_weight_sucessful_with_expected_data(self):
        expected_result = 50
        result = calculate_serving_size_weight(100, 2.0)
        self.assertEqual(result, expected_result)

    def test_calculate_serving_size_weight_returns_None_if_weight_missing(self):
        expected_result = None
        result = calculate_serving_size_weight(None, 2.0)
        self.assertEqual(result, expected_result)

    def test_calculate_serving_size_weight_returns_None_if_number_of_servings_missing(self):
        expected_result = None
        result = calculate_serving_size_weight(100, None)
        self.assertEqual(result, expected_result)


class TestFormattedRecipeTreeComponents(TestCase):
    def test_weight_from_recipe_tree_components_with_pkg_and_standalone(self):
        expected_result = 829
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data)
        self.assertEqual(result['weight'], expected_result)

    def test_weight_from_recipe_tree_components_successful_no_pkg_no_standalone(self):
        expected_result = 1382
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_no_pkg_no_standalone)
        self.assertEqual(result['weight'], expected_result)

    def test_weight_from_recipe_tree_components_empty(self):
        result = format_recipe_tree_components_data([])
        self.assertEqual(result['weight'], 0)

    def test_format_recipe_tree_components_data_with_more_than_one_serving_of_standalone_component(self):
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_with_multiple_servings_of_standalone)
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
            'standaloneWeight': 71,
            'standaloneSuggestedServing': "1 oz",
            'standaloneServingSizeWeight': 28,
            'standaloneServings': 2.5,
            'weight': 156,
            'hasStandalone': True
        }
        self.assertEqual(result, expected)

    def test_format_recipe_tree_components_data_with_one_serving_of_standalone_component(self):
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_with_one_serving_of_standalone)
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
            'standaloneWeight': 43,
            'standaloneSuggestedServing': "1.5 oz",
            'standaloneServingSizeWeight': 43,
            'standaloneServings': 1.0,
            'weight': 156,
            'hasStandalone': True
        }
        self.assertEqual(result, expected)

    def test_format_recipe_tree_components_data_with_standalone_missing_nutritionals_quantity_data(self):
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_with_standalone_missing_nutritionals_quantity_data)
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
            'standaloneWeight': 43,
            'standaloneSuggestedServing': None,
            'standaloneServingSizeWeight': None,
            'standaloneServings': None,
            'weight': 156,
            'hasStandalone': True
        }
        self.assertEqual(result, expected)

class TestGetFormattedRecipesData(TestCase):

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_successful(self, mock_retrieval_method):
        expected_result = [
            {
                'id': '1',
                'externalName': 'Test Recipe 1',
                'notes': 'Some notes about recipe 1',
                'description': 'Details about recipe 1',
                'lifestylePhotoUrl': 'https://cdn.filestackcontent.com/LIFESTYLE1',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'baseMeal': 'Base Salad Name',
                'ingredients': [
                    'Unique 1',
                    'Duplicate 1',
                    'Duplicate 2',
                    'Duplicate 3',
                    'Unique 2',
                    'Unique 4'
                ],
                'weight': 829,
                'hasStandalone': False,
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': None,
                'standaloneRecipeName': None,
                'standaloneWeight': None,
                'standaloneSuggestedServing': None,
                'standaloneServingSizeWeight': None,
                'standaloneServings': None
            },
            {
                'id': '2',
                'externalName': 'Test Recipe 2',
                'notes': 'Some notes about recipe 2',
                'description': 'Details about recipe 2',
                'lifestylePhotoUrl': 'https://cdn.filestackcontent.com/LIFESTYLE2',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'baseMeal': 'Base Salad Name',
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
                'standaloneSuggestedServing': None,
                'standaloneServingSizeWeight': None,
                'standaloneServings': None,
                'weight': 829,
                'hasStandalone': False
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
        self.assertEqual(formatted_recipe['hasStandalone'], True)
        self.assertEqual(formatted_recipe['standaloneRecipeName'], 'Peanut Coconut Sauce')
        self.assertEqual(formatted_recipe['standaloneRecipeId'], 'cmVjaXBlOjE3MDM5NA==')
        self.assertEqual(formatted_recipe['standaloneWeight'], 71)
        self.assertEqual(formatted_recipe['standaloneSuggestedServing'], "1 oz")
        self.assertEqual(formatted_recipe['standaloneServingSizeWeight'], 28)
        self.assertEqual(formatted_recipe['standaloneServings'], 2.5)


class TestGetFormattedMenuData(TestCase):
    def response(self, *menus):
        return ({
            'data': {
                'viewer': {
                    'menus': [m for m in menus if m]
                }
            }
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
        self.assertEqual(result1, [formatted_menu('2021-11-14')])

        # multiple valid menu names
        result2 = get_formatted_menu_data(['2021-11-21', '2021-11-21',
                                           '2021-11-28'])
        self.assertEqual(result2, [formatted_menu('2021-11-21'),
                                   formatted_menu('2021-11-21'),
                                   formatted_menu('2021-11-28')])

        # one valid menu name and one invalid menu name
        result3 = get_formatted_menu_data(['2021-11-28', '2021-12-05'])
        self.assertEqual(result3, [formatted_menu('2021-11-28')])

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
