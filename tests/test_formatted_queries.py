from unittest import TestCase, mock
from galley.enums import RecipeCategoryTagTypeEnum
from tests.mock_responses.mock_menu_data import mock_menu
from galley.formatted_queries import (
    RecipeItem,
    calculate_serving_size_weight,
    calculate_servings,
    format_recipe_tree_components_data,
    format_title,
    get_formatted_menu_data,
    get_formatted_recipes_data,
    get_recipe_category_tags
)
from tests.mock_responses import (
    mock_nutrition_data,
    mock_recipe_tree_components,
    mock_recipe_tree_components,
    mock_recipe_category_values,
    mock_recipes_data
)


STANDALONE_NUTRITION = {'addedSugarG': 0,
                        'calciumMg': 3.1684181569284497,
                        'calciumPercentRDI': 0.002,
                        'caloriesKCal': 53.66203631343362,
                        'carbsG': 5.931480844736274,
                        'carbsPercentDRV': 0.022,
                        'cholesterolMg': 0,
                        'cholesterolPercentDRV': None,
                        'copperMg': 0.021694334590068795,
                        'copperPercentRDI': 0.024,
                        'fiberG': 0.25925700237554117,
                        'fiberPercentDRV': 0.009,
                        'folateMcg': 4.662944286512987,
                        'folatePercentRDI': 0.012,
                        'ironMg': 0.08727603182928573,
                        'ironPercentRDI': 0.005,
                        'magnesiumMg': 8.422029852813752,
                        'magnesiumPercentRDI': 0.02,
                        'manganeseMg': 0.07968240957035716,
                        'manganesePercentRDI': 0.035,
                        'niacinMg': 0.6287359687622166,
                        'niacinPercentRDI': 0.039,
                        'pantothenicAcidMg': 0.06062563923716235,
                        'phosphorusMg': 16.6108569332684,
                        'phosphorusPercentRDI': 0.013,
                        'potassiumMg': 35.3618045624374,
                        'potassiumPercentRDI': 0.008,
                        'proteinG': 1.190862966668126,
                        'proteinPercentRDI': 0.024,
                        'riboflavinMg': 0.009900242547519483,
                        'riboflavinPercentRDI': 0.008,
                        'saturatedFatG': 1.1966419313881989,
                        'seleniumMcg': 0.1983239364917749,
                        'seleniumPercentRDI': 0.004,
                        'sodiumMg': 80.1688699548479,
                        'sodiumPercentDRV': 0.035,
                        'sugarG': 4.635864789281829,
                        'sugarPercentDRV': None,
                        'thiaminMg': 0.008514061320616884,
                        'thiaminPercentRDI': 0.007,
                        'totalFatG': 3.2182500200225643,
                        'totalFatPercentDRV': 0.041,
                        'transFatG': 0.0035436903875000004,
                        'vitaminAMcg': 1.449295858309044,
                        'vitaminAPercentRDI': 0.002,
                        'vitaminB12Mcg': 0,
                        'vitaminB12PercentRDI': None,
                        'vitaminB6Mg': 0.022999931273467538,
                        'vitaminB6PercentRDI': 0.014,
                        'vitaminCMg': 1.7259736392050762,
                        'vitaminCPercentRDI': 0.019,
                        'vitaminDMcg': 0,
                        'vitaminDPercentRDI': None,
                        'vitaminEMg': 0.4437743529419914,
                        'vitaminEPercentRDI': 0.03,
                        'vitaminKMcg': 0.046390128709090914,
                        'vitaminKPercentRDI': 0,
                        'zincMg': 0.12343713881647085,
                        'zincPercentRDI': 0.011}


COMBINED_INGREDIENTS_LIST_WITH_USAGES = [('Water', 5.425000000000001),
                                         ('Sprouted Brown Rice', 1.1199999999999999),
                                         ('Coconut Milk (Coconut, Water, Guar Gum)*', 1.1),
                                         ('Cashew', 0.6000000000000001),
                                         ('Golden Raisins', 0.5625),
                                         ('Hemp Seeds', 0.37449999999999994),
                                         ('Pistachio Nuts*', 0.3375),
                                         ('Dried Blueberries*', 0.1875),
                                         ('Maple Syrup*', 0.17500000000000002),
                                         ('Coconut Chips*', 0.15),
                                         ('Lemon Juice', 0.1),
                                         ('Oats', 0.07500000000000001),
                                         ('Vanilla Extract*', 0.028749999974646844),
                                         ('Flax Seed*', 0.024999999977953775),
                                         ('Lemon Zest', 0.018749999983465333),
                                         ('Sea Salt', 0.012687499988811541),
                                         ('Cinnamon', 0.006249999994488444),
                                         ('Cardamom', 0.003749999996693066)]


STANDALONE_INGREDIENTS_LIST_WITH_USAGES = [("Water", 0.625),
                                           ("Cashew", 0.6000000000000001),
                                           ("Lemon Juice", 0.1),
                                           ("Maple Syrup*", 0.07500000000000001),
                                           ("Oats", 0.07500000000000001),
                                           ("Lemon Zest", 0.018749999983465333),
                                           ("Vanilla Extract*", 0.018749999983465333),
                                           ("Sea Salt", 0.004687499995866333)]


INGREDIENTS_LIST_WITH_USAGES = [("Water", 4.800000000000001),
                                ("Sprouted Brown Rice", 1.1199999999999999),
                                ("Coconut Milk (Coconut, Water, Guar Gum)*", 1.1),
                                ("Golden Raisins", 0.5625),
                                ("Hemp Seeds", 0.37449999999999994),
                                ("Pistachio Nuts*", 0.3375),
                                ("Dried Blueberries*", 0.1875),
                                ("Coconut Chips*", 0.15),
                                ("Maple Syrup*", 0.1),
                                ("Flax Seed*", 0.024999999977953775),
                                ("Vanilla Extract*", 0.00999999999118151),
                                ("Sea Salt", 0.007999999992945208),
                                ("Cinnamon", 0.006249999994488444),
                                ("Cardamom", 0.003749999996693066)]


INGREDIENTS_LIST_NO_USAGES = [ingredient for ingredient, _ in INGREDIENTS_LIST_WITH_USAGES]
STANDALONE_INGREDIENTS_LIST_NO_USAGES = [ingredient for ingredient, _ in STANDALONE_INGREDIENTS_LIST_WITH_USAGES]
COMBINED_INGREDIENTS_LIST_NO_USAGES = [ingredient for ingredient, _ in COMBINED_INGREDIENTS_LIST_WITH_USAGES]


def formatted_menu(date, onlySellableMenuItems=False):
    formatted_menu = {
        'name': f"{date} 1_2_3",
        'id': 'MENU123ABC',
        'date': f"{date}",
        'location': 'Vacaville',
        'categoryMenuType': 'production',
        'menuItems': [{
            'allergens': [],
            'baseMeal': '',
            'deliveryDate': f"{date}",
            'hasAllergen': False,
            'highlightTags': [],
            'id': 'MENUITEM1ABC',
            'itemCode': 'dv1',
            'mealSlug': 'test-recipe-name-1',
            'recipeId': 'RECIPE1ABC',
            'recipeMealType': 'dinner',
            'recipeMenuPhotoUrl': 'https://cdn.filestackcontent.com/Recipe_1_Menu',
            'recipeName': 'Test Recipe Name 1',
            'recipeProteinType': 'vegan',
        }, {
            'allergens': ['coconut', 'soy'],
            'baseMeal': '',
            'deliveryDate': f"{date}",
            'hasAllergen': True,
            'highlightTags': ['new', 'spicy'],
            'id': 'MENUITEM2DEF',
            'itemCode': 'dv2',
            'mealSlug': 'test-recipe-name-2',
            'recipeId': 'RECIPE2DEF',
            'recipeMealType': 'dinner',
            'recipeMenuPhotoUrl': 'https://cdn.filestackcontent.com/Recipe_2_Menu',
            'recipeName': 'Test Recipe Name 2',
            'recipeProteinType': 'vegan',
        }, {
            'allergens': ['soy'],
            'baseMeal': '',
            'deliveryDate': f"{date}",
            'hasAllergen': True,
            'highlightTags': ['new'],
            'id': 'MENUITEM3GHI',
            'itemCode': 'lm2',
            'mealSlug': 'test-recipe-name-3',
            'recipeId': 'RECIPE3GHI',
            'recipeMealType': 'lunch',
            'recipeMenuPhotoUrl': 'https://cdn.filestackcontent.com/Recipe_3_Menu',
            'recipeName': 'Test Recipe Name 3',
            'recipeProteinType': 'meat',
        }]
    }
    if not onlySellableMenuItems:
        formatted_menu['menuItems'].append({
            'allergens': [],
            'baseMeal': '',
            'deliveryDate': f"{date}",
            'hasAllergen': False,
            'highlightTags': [],
            'id': 'MENUITEM4JKL',
            'itemCode': 'non-sellable soup',
            'mealSlug': None,
            'recipeId': 'RECIPE4JKL',
            'recipeMealType': '',
            'recipeMenuPhotoUrl': None,
            'recipeName': 'Test Recipe Name 4',
            'recipeProteinType': '',
        })
    return formatted_menu


class TestIngredientsFromRecipeItems(TestCase):
    def test_get_ingredient_usage_successful(self):
        self.maxDiff = None
        recipe_item = RecipeItem(ingredient = {"name": "spinach, baby, SEND TO PLATE",
                                               "externalName": "Baby Spinach*",
                                               "categoryValues": []},
                                 unit_values = [{ "value": 85.0485693, "unit": { "id": "dW5pdDox", "name": "g" } },
                                                { "value": 3, "unit": { "id": "dW5pdDoz", "name": "oz" } },
                                                { "value": 0.1874999998346533, "unit": { "id": "dW5pdDo0", "name": "lb" } }])
        result = recipe_item.get_ingredients_usages()
        self.assertEqual(result, { 'Baby Spinach*': 3 })

    def test_get_subrecipe_ingredients_usages_successful(self):
        self.maxDiff = None
        unit_values =  mock_recipe_tree_components.mock_recipe_tree_components_data_with_multiple_servings_of_standalone[0]['quantityUnitValues']
        subrecipe = mock_recipe_tree_components.mock_recipe_tree_components_data_with_multiple_servings_of_standalone[0]['recipeItem']['subRecipe']
        recipe_item = RecipeItem(unit_values=unit_values,
                                 subrecipe=subrecipe)
        result = recipe_item.get_ingredients_usages()
        self.assertEqual(result, {'Cardamom': 0.003749999996693066,
                                  'Cinnamon': 0.006249999994488444,
                                  'Coconut Milk (Coconut, Water, Guar Gum)*': 1.1,
                                  'Flax Seed*': 0.024999999977953775,
                                  'Hemp Seeds': 0.112,
                                  'Maple Syrup*': 0.1,
                                  'Sea Salt': 0.007999999992945208,
                                  'Sprouted Brown Rice': 1.1199999999999999,
                                  'Vanilla Extract*': 0.00999999999118151,
                                  'Water': 4.800000000000001})

    def test_get_ingredient_usages_null(self):
        recipe_item = RecipeItem(ingredient=None, subrecipe=None)
        result = recipe_item.get_ingredients_usages()
        self.assertEqual(result, {})

    def test_get_ingredient_usages_empty(self):
        recipe_item = RecipeItem(ingredient={}, subrecipe={})
        result = recipe_item.get_ingredients_usages()
        self.assertEqual(result, {})


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
        expected_net_weight = 213
        expected_gross_weight = 291
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data)
        self.assertEqual(result['netWeight'], expected_net_weight)
        self.assertEqual(result['grossWeight'], expected_gross_weight)

    def test_weight_from_recipe_tree_components_successful_no_pkg_no_standalone(self):
        expected_result = 255
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_no_pkg_no_standalone)
        self.assertEqual(result['netWeight'], expected_result)
        self.assertEqual(result['grossWeight'], expected_result)

    def test_weight_from_recipe_tree_components_empty(self):
        result = format_recipe_tree_components_data([])
        self.assertEqual(result['netWeight'], 0)
        self.assertEqual(result['grossWeight'], 0)

    def test_format_recipe_tree_components_data_with_more_than_one_serving_of_standalone_component(self):
        self.maxDiff = None
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_with_multiple_servings_of_standalone)
        expected_formatted_standalone = {
            'ingredients': INGREDIENTS_LIST_WITH_USAGES,
            'netWeight': 213,
            'grossWeight': 291,
            'hasStandalone': True,
            'standaloneRecipeId': 'cmVjaXBlOjE3NDI3NQ==',
            'standaloneRecipeName': 'Vanilla Cashew Cream',
            'standaloneNutrition': STANDALONE_NUTRITION,
            'standaloneIngredients': STANDALONE_INGREDIENTS_LIST_WITH_USAGES,
            'standaloneNetWeight': 43,
            'standaloneSuggestedServing': "0.75 oz",
            'standaloneServingSizeWeight': 21,
            'standaloneServings': 2.0,
        }
        self.assertEqual(result, expected_formatted_standalone)

    def test_format_recipe_tree_components_data_with_one_serving_of_standalone_component(self):
        self.maxDiff = None
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_with_one_serving_of_standalone)
        expected = {
            'ingredients': INGREDIENTS_LIST_WITH_USAGES,
            'netWeight': 213,
            'grossWeight': 291,
            'hasStandalone': True,
            'standaloneRecipeId': 'cmVjaXBlOjE3NDI3NQ==',
            'standaloneRecipeName': 'Vanilla Cashew Cream',
            'standaloneNutrition': STANDALONE_NUTRITION,
            'standaloneIngredients': STANDALONE_INGREDIENTS_LIST_WITH_USAGES,
            'standaloneNetWeight': 43,
            'standaloneSuggestedServing': "1.5 oz",
            'standaloneServingSizeWeight': 43,
            'standaloneServings': 1.0
        }
        self.assertEqual(result, expected)

    def test_format_recipe_tree_components_data_with_standalone_missing_nutritionals_quantity_data(self):
        self.maxDiff = None
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data_with_standalone_missing_nutritionals_quantity_data)
        expected = {
            'ingredients': INGREDIENTS_LIST_WITH_USAGES,
            'netWeight': 213,
            'grossWeight': 291,
            'hasStandalone': True,
            'standaloneRecipeId': 'cmVjaXBlOjE3NDI3NQ==',
            'standaloneRecipeName': 'Vanilla Cashew Cream',
            'standaloneNutrition': STANDALONE_NUTRITION,
            'standaloneIngredients': STANDALONE_INGREDIENTS_LIST_WITH_USAGES,
            'standaloneNetWeight': 43,
            'standaloneSuggestedServing': None,
            'standaloneServingSizeWeight': None,
            'standaloneServings': None
        }
        self.assertEqual(result, expected)


class TestGetRecipeCategoryTags(TestCase):

    def test_get_recipe_category_tags_with_all_tags_populated(self):
        recipe_category_values = mock_recipe_category_values.mock_data
        expected_result = {
            'proteinType': 'vegan',
            'mealContainer': 'ts48',
            'mealType': 'dinner',
            'proteinAddOn': 'high-protein-legume',
            'baseMealSlug': 'base-salad',
            'baseMeal': 'Base Salad Name',
            'highlightTags': ['new', 'spicy'],
            'displayNutritionOnWebsite': True
        }

        result = get_recipe_category_tags(recipe_category_values)
        self.assertEqual(result, expected_result)

    def test_get_recipe_category_tags_with_no_tags_populated(self):
        recipe_category_values = []
        expected_result = {
            'highlightTags': [],
            'displayNutritionOnWebsite': True
        }

        result = get_recipe_category_tags(recipe_category_values)
        self.assertEqual(result, expected_result)

    def test_get_recipe_category_tags_with_just_one_highlight_tag(self):
        recipe_category_values = mock_recipe_category_values.mock_data
        # mock data contains two highlight tags- remove one of them
        recipe_category_values.pop(recipe_category_values.index({
            'name': 'spicy',
            'category': {
                'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_TWO_TAG.value,
                'itemType': 'recipe',
                'name': 'highlight_2'
            }
        }))
        expected_result = {
            'proteinType': 'vegan',
            'mealContainer': 'ts48',
            'mealType': 'dinner',
            'proteinAddOn': 'high-protein-legume',
            'baseMealSlug': 'base-salad',
            'baseMeal': 'Base Salad Name',
            'highlightTags': ['new'],
            'displayNutritionOnWebsite': True
        }

        result = get_recipe_category_tags(recipe_category_values)
        self.assertEqual(result, expected_result)

    def test_get_recipe_category_tags_when_display_nutrition_on_website_is_false(self):
        recipe_category_values = [
            {
                'name': 'true',
                'category': {
                    'id': RecipeCategoryTagTypeEnum.NO_NUTRITION_ON_WEBSITE_TAG.value,
                    'itemType': 'recipe',
                    'name': 'no nutrition on website'
                }
            },
        ]
        expected_result = {
            'highlightTags': [],
            'displayNutritionOnWebsite': False
        }

        result = get_recipe_category_tags(recipe_category_values)
        self.assertEqual(result, expected_result)

class TestGetFormattedRecipesData(TestCase):
    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_successful(self, mock_retrieval_method):
        self.maxDiff = None
        expected_result = [
            {
                'id': '1',
                'externalName': 'Test Recipe 1',
                'version': 'dmVyc2lvbjozNjQ0NTY1',
                'notes': 'Some notes about recipe 1',
                'description': 'Details about recipe 1',
                'menuPhotoUrl': 'https://cdn.filestackcontent.com/MENU1',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'baseMeal': 'Base Salad Name',
                'highlightTags': ['new', 'spicy'],
                'displayNutritionOnWebsite': True,
                'ingredients': COMBINED_INGREDIENTS_LIST_NO_USAGES,
                'netWeight': 255,
                'grossWeight': 255,
                'hasStandalone': False,
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': None,
                'standaloneRecipeName': None,
                'standaloneNetWeight': None,
                'standaloneSuggestedServing': None,
                'standaloneServingSizeWeight': None,
                'standaloneServings': None,
                'hasAllergen': False,
                'allergens': []
            },
            {
                'id': '2',
                'externalName': 'Test Recipe 2',
                'notes': 'Some notes about recipe 2',
                'version': 'dmVyc2lvbjozNjQ0NTY1',
                'description': 'Details about recipe 2',
                'menuPhotoUrl': 'https://cdn.filestackcontent.com/MENU2',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'baseMeal': 'Base Salad Name',
                'highlightTags': ['new', 'spicy'],
                'displayNutritionOnWebsite': True,
                'ingredients': COMBINED_INGREDIENTS_LIST_NO_USAGES,
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': None,
                'standaloneRecipeName': None,
                'standaloneNetWeight': None,
                'standaloneSuggestedServing': None,
                'standaloneServingSizeWeight': None,
                'standaloneServings': None,
                'netWeight': 255,
                'grossWeight': 255,
                'hasStandalone': False,
                'hasAllergen': False,
                'allergens': []
            }
        ]

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': mock_recipes_data.mock_recipe_connection_with_no_standalone(['1', '2'])
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
    def test_get_formatted_recipes_data_no_standalone(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection':
                        mock_recipes_data.mock_recipe_connection_with_no_standalone(['1'])
                }
            }
        }
        result = get_formatted_recipes_data(["1"])
        formatted_recipe = result[0]
        self.assertEqual(formatted_recipe['ingredients'], COMBINED_INGREDIENTS_LIST_NO_USAGES)
        self.assertEqual(formatted_recipe['hasStandalone'], False)
        self.assertEqual(formatted_recipe['standaloneRecipeName'], None)
        self.assertEqual(formatted_recipe['standaloneRecipeId'], None)
        self.assertEqual(formatted_recipe['standaloneNetWeight'], None)
        self.assertEqual(formatted_recipe['standaloneSuggestedServing'], None)
        self.assertEqual(formatted_recipe['standaloneServingSizeWeight'], None)
        self.assertEqual(formatted_recipe['standaloneServings'], None)
        self.assertEqual(formatted_recipe['standaloneIngredients'], None)

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
        self.assertEqual(formatted_recipe['ingredients'], INGREDIENTS_LIST_NO_USAGES)
        self.assertEqual(formatted_recipe['hasStandalone'], True)
        self.assertEqual(formatted_recipe['standaloneRecipeName'], 'Vanilla Cashew Cream')
        self.assertEqual(formatted_recipe['standaloneRecipeId'], 'cmVjaXBlOjE3NDI3NQ==')
        self.assertEqual(formatted_recipe['standaloneNetWeight'], 43)
        self.assertEqual(formatted_recipe['standaloneSuggestedServing'], "0.75 oz")
        self.assertEqual(formatted_recipe['standaloneServingSizeWeight'], 21)
        self.assertEqual(formatted_recipe['standaloneServings'], 2.0)
        self.assertEqual(formatted_recipe['standaloneIngredients'], STANDALONE_INGREDIENTS_LIST_NO_USAGES)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_no_standalone_with_ingredient_usages_format_option(self, mock_retrieval_method):
        self.maxDiff = None
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection':
                        mock_recipes_data.mock_recipe_connection_with_no_standalone(['1'])
                }
            }
        }
        result = get_formatted_recipes_data(["1"], includeIngredientUsages=True)
        formatted_recipe = result[0]
        self.assertEqual(formatted_recipe['ingredients'], COMBINED_INGREDIENTS_LIST_WITH_USAGES)
        self.assertEqual(formatted_recipe['hasStandalone'], False)
        self.assertEqual(formatted_recipe['standaloneRecipeName'], None)
        self.assertEqual(formatted_recipe['standaloneRecipeId'], None)
        self.assertEqual(formatted_recipe['standaloneNetWeight'], None)
        self.assertEqual(formatted_recipe['standaloneSuggestedServing'], None)
        self.assertEqual(formatted_recipe['standaloneServingSizeWeight'], None)
        self.assertEqual(formatted_recipe['standaloneServings'], None)
        self.assertEqual(formatted_recipe['standaloneIngredients'], None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_with_standalone_and_ingredient_usages_format_option(self, mock_retrieval_method):
        self.maxDiff = None
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection':
                        mock_recipes_data.mock_recipe_connection_with_standalone(['1'])
                }
            }
        }
        result = get_formatted_recipes_data(["1"], includeIngredientUsages=True)
        formatted_recipe = result[0]
        self.assertEqual(formatted_recipe['ingredients'], INGREDIENTS_LIST_WITH_USAGES)
        self.assertEqual(formatted_recipe['hasStandalone'], True)
        self.assertEqual(formatted_recipe['standaloneRecipeName'], 'Vanilla Cashew Cream')
        self.assertEqual(formatted_recipe['standaloneRecipeId'], 'cmVjaXBlOjE3NDI3NQ==')
        self.assertEqual(formatted_recipe['standaloneNetWeight'], 43)
        self.assertEqual(formatted_recipe['standaloneSuggestedServing'], "0.75 oz")
        self.assertEqual(formatted_recipe['standaloneServingSizeWeight'], 21)
        self.assertEqual(formatted_recipe['standaloneServings'], 2.0)
        self.assertEqual(formatted_recipe['standaloneIngredients'], STANDALONE_INGREDIENTS_LIST_WITH_USAGES)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_with_allergen_and_standalone_successful(
        self, mock_retrieval_method
    ):
        self.maxDiff = None
        expected_result = [
            {
                'id': '1',
                'externalName': 'Test Recipe 1',
                'version': 'dmVyc2lvbjozNjQ0NTY1',
                'notes': 'Some notes about recipe 1',
                'description': 'Details about recipe 1',
                'menuPhotoUrl': 'https://cdn.filestackcontent.com/MENU1',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'baseMeal': 'Base Salad Name',
                'highlightTags': ['new', 'spicy'],
                'displayNutritionOnWebsite': True,
                'ingredients': INGREDIENTS_LIST_NO_USAGES,
                'netWeight': 213,
                'grossWeight': 291,
                'hasStandalone': True,
                'standaloneIngredients': STANDALONE_INGREDIENTS_LIST_NO_USAGES,
                'standaloneNutrition': STANDALONE_NUTRITION,
                'standaloneRecipeId': 'cmVjaXBlOjE3NDI3NQ==',
                'standaloneRecipeName': 'Vanilla Cashew Cream',
                'standaloneNetWeight': 43,
                'standaloneSuggestedServing': '0.75 oz',
                'standaloneServingSizeWeight': 21,
                'standaloneServings': 2.0,
                'hasAllergen': True,
                'allergens': ['soy']
            }
        ]

        mock_recipe_data = mock_recipes_data.mock_recipe_connection_with_standalone(['1'])
        mock_recipe_data['edges'][0]['node']['dietaryFlagsWithUsages'] = [{
            'dietaryFlag': {
                'id': 'ZGlldGFyeUZsYWc6Ng==',
                'name': 'soy beans'
            }
        }]

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': mock_recipe_data
                }
            }
        }
        result = get_formatted_recipes_data(['1'])
        self.assertEqual(result, expected_result)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_with_non_supported_allergen_successful(
        self, mock_retrieval_method
    ):
        self.maxDiff = None
        expected_result = [
            {
                'id': '1',
                'externalName': 'Test Recipe 1',
                'version': 'dmVyc2lvbjozNjQ0NTY1',
                'notes': 'Some notes about recipe 1',
                'description': 'Details about recipe 1',
                'menuPhotoUrl': 'https://cdn.filestackcontent.com/MENU1',
                'nutrition': mock_nutrition_data.mock_data,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'baseMeal': 'Base Salad Name',
                'highlightTags': ['new', 'spicy'],
                'displayNutritionOnWebsite': True,
                'ingredients': INGREDIENTS_LIST_NO_USAGES,
                'netWeight': 213,
                'grossWeight': 291,
                'hasStandalone': True,
                'standaloneIngredients': STANDALONE_INGREDIENTS_LIST_NO_USAGES,
                'standaloneNutrition': STANDALONE_NUTRITION,
                'standaloneRecipeId': 'cmVjaXBlOjE3NDI3NQ==',
                'standaloneRecipeName': 'Vanilla Cashew Cream',
                'standaloneNetWeight': 43,
                'standaloneSuggestedServing': '1.5 oz',
                'standaloneServingSizeWeight': 43,
                'standaloneServings': 1.0,
                'hasAllergen': False,
                'allergens': []
            }
        ]

        mock_recipe_data = mock_recipes_data.mock_recipe_connection(['1'])
        mock_recipe_data['edges'][0]['node']['dietaryFlagsWithUsages'] = [{
            'dietaryFlag': {
                'id': 'ZGlldGFyeUZsYWc6MTc=',
                'name': 'sulphites'
            }
        }]

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': mock_recipe_data
                }
            }
        }
        result = get_formatted_recipes_data(['1'])
        self.assertEqual(result, expected_result)


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
    def test_get_formatted_menu_data_successful_for_one_valid_menu(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_menu('2021-11-14'))
        result = get_formatted_menu_data(['2021-11-14'])
        self.assertEqual(result, [formatted_menu('2021-11-14')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_successful_for_multiple_valid_menus(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_menu('2021-11-21'), mock_menu('2021-11-21'), mock_menu('2021-11-28'))
        result = get_formatted_menu_data(['2021-11-21', '2021-11-21', '2021-11-28'])
        self.assertEqual(result, [formatted_menu('2021-11-21'), formatted_menu('2021-11-21'), formatted_menu('2021-11-28')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_successful_for_one_valid_and_one_invalid_menu(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_menu('2021-11-28'), mock_menu('2021-12-05'))
        result = get_formatted_menu_data(['2021-11-28', '2021-12-05'])
        self.assertEqual(result, [formatted_menu('2021-11-28')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_successful_for_one_invalid_menu(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_menu('2021-12-05'))
        result = get_formatted_menu_data(['2021-12-05'])
        self.assertEqual(result, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_excludes_nonsellable_menu_items(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_menu('2021-11-14'))
        result = get_formatted_menu_data(['2021-11-14'], onlySellableMenuItems=True)
        self.assertEqual(result, [formatted_menu('2021-11-14', onlySellableMenuItems=True)])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_exception(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        with self.assertRaises(ValueError):
            get_formatted_menu_data([])

    @mock.patch('galley.formatted_queries.get_raw_menu_data')
    def test_get_formatted_menu_data_args_defaults(self, mock_grmd):
        dates = ['2021-11-14', '2021-10-04']
        get_formatted_menu_data(dates)
        mock_grmd.assert_called_with(dates, 'Vacaville', 'production')
        get_formatted_menu_data(dates, 'Montana', 'staging')
        mock_grmd.assert_called_with(dates, 'Montana', 'staging')

    def test_get_formatted_menu_data_base_meal_title_format(self):
        self.assertEqual(format_title("beet-poke"), "Beet-Poke")
        self.assertEqual(format_title("persephone's salad"), "Persephone's Salad")
        self.assertEqual(format_title("brussel sprout & asian pear 'fried' rice"),
                         "Brussel Sprout & Asian Pear 'Fried' Rice")
        self.assertEqual(format_title("beetroot quinoa & sun 'cheese' salad"),
                         "Beetroot Quinoa & Sun 'Cheese' Salad")
