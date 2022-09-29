from unittest import TestCase, mock

from galley.enums import RecipeCategoryTagTypeEnum
from galley.formatted_queries import (
    calculate_serving_size_weight,
    calculate_servings,
    format_recipe_tree_components_data,
    format_title,
    get_formatted_menu_data,
    get_formatted_recipes_data,
    get_ingredients_usages,
    get_recipe_category_tags
)

from tests.mock_responses import (
    mock_nutrition_data,
    mock_all_ingredients_with_usages_data,
    mock_recipe_tree_components,
    mock_recipe_tree_components,
    mock_recipe_category_values,
    mock_recipes_data
)
from tests.mock_responses.mock_menu_data import mock_menu


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
    def test_get_ingredient_usages_successful(self):
        self.maxDiff = None
        expected_result = {
            'Peanut Butter (Dry Roasted Peanuts)': 0.3333333,
            'Cabbage': 1,
            'Rainbow Carrots*': 1,
            'Coconut Aminos (Coconut Tree Sap, Sea Salt)*': 0.6,
            'Lime Juice': 0.4,
            'Lemon Zest': 0.1083333,
            'Coconut Milk (Coconut, Water, Guar Gum)*': 0.3333333,
            'Toasted Sesame Oil': 0.05,
            'Quinoa': 1.5625,
            'Sea Salt': 0.0136201,
            'Sambal (Red Chile Peppers, Vinegar, Salt)': 0.0833333,
            'Sesame Seed*': 0.025,
            'Black Pepper': 0.003125,
            'Water': 1.8333333,
            'Granulated Garlic': 0.025,
            'Carrot': 0.0273973,
            'Cucumber': 1.1111111,
            'Chicken': 3.2876712,
            'Snap Peas': 1,
            'Garlic': 0.0833333 + 0.0136986,
            'Baby Spinach*': 2.5,
            'Onions': 0.0273973,
            'Celery*': 0.0273973,
            'Poaching Liquid': 0.2
        }
        result = get_ingredients_usages(mock_all_ingredients_with_usages_data.mock_data)
        self.assertEqual(result, expected_result)

    def test_get_ingredient_usages_null(self):
        result = get_formatted_recipes_data(None)
        self.assertEqual(result, [])

    def test_get_ingredient_usages_empty(self):
        result = get_ingredients_usages([])
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
        expected_net_weight = 829
        expected_gross_weight = 1382
        result = format_recipe_tree_components_data(
            mock_recipe_tree_components.mock_recipe_tree_components_data)
        self.assertEqual(result['netWeight'], expected_net_weight)
        self.assertEqual(result['grossWeight'], expected_gross_weight)

    def test_weight_from_recipe_tree_components_successful_no_pkg_no_standalone(self):
        expected_result = 1382
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
        expected = {
            'standaloneRecipeId': 'cmVjaXBlOjE3MDM5NA==',
            'standaloneRecipeName': 'Peanut Coconut Sauce',
            'standaloneNutrition': {
                'addedSugarG': 0,
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
                'zincPercentRDI': 0.011
                },
            'standaloneIngredients': {
                'Coconut Aminos (Coconut Tree Sap, Sea Salt)*': 0.6,
                'Coconut Milk (Coconut, Water, Guar Gum)*': 0.3333333,
                'Garlic': 0.0833333,
                'Lime Juice': 0.4,
                'Peanut Butter (Dry Roasted Peanuts)': 0.3333333,
                'Sambal (Red Chile Peppers, Vinegar, Salt)': 0.0833333,
                'Water': 0.1666667
            },
            'standaloneNetWeight': 71,
            'standaloneSuggestedServing': "1 oz",
            'standaloneServingSizeWeight': 28,
            'standaloneServings': 2.5,
            'netWeight': 156,
            'grossWeight': 227,
            'hasStandalone': True
        }
        self.assertEqual(result, expected)

    def test_format_recipe_tree_components_data_with_one_serving_of_standalone_component(self):
        self.maxDiff = None
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
            'standaloneIngredients': {
                'Coconut Aminos (Coconut Tree Sap, Sea Salt)*': 0.6,
                'Coconut Milk (Coconut, Water, Guar Gum)*': 0.3333333,
                'Garlic': 0.0833333,
                'Lime Juice': 0.4,
                'Peanut Butter (Dry Roasted Peanuts)': 0.3333333,
                'Sambal (Red Chile Peppers, Vinegar, Salt)': 0.0833333,
                'Water': 0.1666667
            },
            'standaloneNetWeight': 43,
            'standaloneSuggestedServing': "1.5 oz",
            'standaloneServingSizeWeight': 43,
            'standaloneServings': 1.0,
            'netWeight': 156,
            'grossWeight': 199,
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
            'standaloneIngredients': {
                'Coconut Aminos (Coconut Tree Sap, Sea Salt)*': 0.6,
                'Coconut Milk (Coconut, Water, Guar Gum)*': 0.3333333,
                'Garlic': 0.0833333,
                'Lime Juice': 0.4,
                'Peanut Butter (Dry Roasted Peanuts)': 0.3333333,
                'Sambal (Red Chile Peppers, Vinegar, Salt)': 0.0833333,
                'Water': 0.1666667
            },
            'standaloneNetWeight': 43,
            'standaloneSuggestedServing': None,
            'standaloneServingSizeWeight': None,
            'standaloneServings': None,
            'netWeight': 156,
            'grossWeight': 199,
            'hasStandalone': True
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
                'ingredients': [
                    'Chicken',
                    'Baby Spinach*',
                    'Water',
                    'Quinoa',
                    'Cucumber',
                    'Cabbage',
                    'Rainbow Carrots*',
                    'Snap Peas',
                    'Coconut Aminos (Coconut Tree Sap, Sea Salt)*',
                    'Lime Juice',
                    'Peanut Butter (Dry Roasted Peanuts)',
                    'Coconut Milk (Coconut, Water, Guar Gum)*',
                    'Poaching Liquid',
                    'Lemon Zest',
                    'Garlic',
                    'Sambal (Red Chile Peppers, Vinegar, Salt)',
                    'Toasted Sesame Oil',
                    'Carrot',
                    'Onions',
                    'Celery*',
                    'Sesame Seed*',
                    'Granulated Garlic',
                    'Sea Salt',
                    'Black Pepper'
                ],
                'netWeight': 829,
                'grossWeight': 1382,
                'hasStandalone': True,
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': 'standalone1',
                'standaloneRecipeName': 'Standalone 1',
                'standaloneNetWeight': 276,
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
                'ingredients': [
                    'Chicken',
                    'Baby Spinach*',
                    'Water',
                    'Quinoa',
                    'Cucumber',
                    'Cabbage',
                    'Rainbow Carrots*',
                    'Snap Peas',
                    'Coconut Aminos (Coconut Tree Sap, Sea Salt)*',
                    'Lime Juice',
                    'Peanut Butter (Dry Roasted Peanuts)',
                    'Coconut Milk (Coconut, Water, Guar Gum)*',
                    'Poaching Liquid',
                    'Lemon Zest',
                    'Garlic',
                    'Sambal (Red Chile Peppers, Vinegar, Salt)',
                    'Toasted Sesame Oil',
                    'Carrot',
                    'Onions',
                    'Celery*',
                    'Sesame Seed*',
                    'Granulated Garlic',
                    'Sea Salt',
                    'Black Pepper'
                ],
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': 'standalone1',
                'standaloneRecipeName': 'Standalone 1',
                'standaloneNetWeight': 276,
                'standaloneSuggestedServing': None,
                'standaloneServingSizeWeight': None,
                'standaloneServings': None,
                'netWeight': 829,
                'grossWeight': 1382,
                'hasStandalone': True,
                'hasAllergen': False,
                'allergens': []
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
        self.assertEqual(formatted_recipe['standaloneNetWeight'], 71)
        self.assertEqual(formatted_recipe['standaloneSuggestedServing'], "1 oz")
        self.assertEqual(formatted_recipe['standaloneServingSizeWeight'], 28)
        self.assertEqual(formatted_recipe['standaloneServings'], 2.5)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_with_allergen_successful(
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
                'ingredients': [
                    'Chicken',
                    'Baby Spinach*',
                    'Water',
                    'Quinoa',
                    'Cucumber',
                    'Cabbage',
                    'Rainbow Carrots*',
                    'Snap Peas',
                    'Coconut Aminos (Coconut Tree Sap, Sea Salt)*',
                    'Lime Juice',
                    'Peanut Butter (Dry Roasted Peanuts)',
                    'Coconut Milk (Coconut, Water, Guar Gum)*',
                    'Poaching Liquid',
                    'Lemon Zest',
                    'Garlic',
                    'Sambal (Red Chile Peppers, Vinegar, Salt)',
                    'Toasted Sesame Oil',
                    'Carrot',
                    'Onions',
                    'Celery*',
                    'Sesame Seed*',
                    'Granulated Garlic',
                    'Sea Salt',
                    'Black Pepper'
                ],
                'netWeight': 829,
                'grossWeight': 1382,
                'hasStandalone': True,
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': 'standalone1',
                'standaloneRecipeName': 'Standalone 1',
                'standaloneNetWeight': 276,
                'standaloneSuggestedServing': None,
                'standaloneServingSizeWeight': None,
                'standaloneServings': None,
                'hasAllergen': True,
                'allergens': ['soy']
            }
        ]

        mock_recipe_data = mock_recipes_data.mock_recipe_connection(['1'])
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
                'ingredients': [
                    'Chicken',
                    'Baby Spinach*',
                    'Water',
                    'Quinoa',
                    'Cucumber',
                    'Cabbage',
                    'Rainbow Carrots*',
                    'Snap Peas',
                    'Coconut Aminos (Coconut Tree Sap, Sea Salt)*',
                    'Lime Juice',
                    'Peanut Butter (Dry Roasted Peanuts)',
                    'Coconut Milk (Coconut, Water, Guar Gum)*',
                    'Poaching Liquid',
                    'Lemon Zest',
                    'Garlic',
                    'Sambal (Red Chile Peppers, Vinegar, Salt)',
                    'Toasted Sesame Oil',
                    'Carrot',
                    'Onions',
                    'Celery*',
                    'Sesame Seed*',
                    'Granulated Garlic',
                    'Sea Salt',
                    'Black Pepper'
                ],
                'netWeight': 829,
                'grossWeight': 1382,
                'hasStandalone': True,
                'standaloneIngredients': None,
                'standaloneNutrition': None,
                'standaloneRecipeId': 'standalone1',
                'standaloneRecipeName': 'Standalone 1',
                'standaloneNetWeight': 276,
                'standaloneSuggestedServing': None,
                'standaloneServingSizeWeight': None,
                'standaloneServings': None,
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

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_menu_data_base_meal_title_format(self, mock_retrieval_method):
        self.assertEqual(format_title("beet-poke"), "Beet-Poke")
        self.assertEqual(format_title("persephone's salad"), "Persephone's Salad")
        self.assertEqual(
            format_title("brussel sprout & asian pear 'fried' rice"),
            "Brussel Sprout & Asian Pear 'Fried' Rice"
        )
        self.assertEqual(
            format_title('beetroot quinoa & sun "cheese" salad'),
            'Beetroot Quinoa & Sun "Cheese" Salad'
        )
