from copy import deepcopy
from unittest import TestCase, mock
from galley.enums import IngredientCategoryValueEnum, PreparationEnum, RecipeCategoryTagTypeEnum, UnitEnum
from tests.mock_responses.mock_menu_data import mock_menu
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.formatted_queries import (
    RecipeItem,
    calculate_serving_size_weight,
    calculate_servings,
    format_title,
    get_ingredient_name,
    get_formatted_menu_data,
    get_formatted_recipes_data,
    get_recipe_category_tags,
    get_recipe_ingredients_and_standalone_data,
    get_recipe_weights
)
from tests.mock_responses.mock_recipes_data import mock_recipe
from tests.mock_responses.mock_nutrition_data import MOCK_RECONCILED_NUTRITIONALS, MOCK_STANDALONE_RECONCILED_NUTRITIONALS
from tests.mock_responses.mock_recipe_category_values import MOCK_RECIPE_CATEGORY_VALUES
from tests.mock_responses.mock_recipe_items_ingredients_with_usages import (
    MOCK_RECIPE_ITEMS,
    SELLABLE_RECIPE_ID,
    SELLABLE_RECIPE_NAME,
    STANDALONE_RECIPE_ID,
    STANDALONE_RECIPE_NAME,
    MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES
)


BASE_INGREDIENTS = ['Buckwheat Groats',
                    'Spring Mix Lettuce*, Kale* or Seasonal Greens*§',
                    'Kidney Beans*',
                    'Rainbow Carrots*',
                    'Red Beets',
                    'Dried Cherries*',
                    'Hemp Seeds',
                    'Pumpkin Seed',
                    'Sunflower Seeds',
                    'Extra Virgin Olive Oil',
                    'Parsley',
                    'Sea Salt',
                    'Rice Bran Oil',
                    'Garlic Powder',
                    'Chili Powder',
                    'Cumin']


STANDALONE_INGREDIENTS = ['Rice Bran Oil',
                          'Aquafaba (Chickpeas, Water)*',
                          'Champagne Vinegar',
                          'Maple Syrup*',
                          'Dijon Mustard (Water, Mustard Seeds, Vinegar, Salt)',
                          'Garlic',
                          'Apple Cider Vinegar',
                          'Garbanzo Beans (Garbanzo Beans, Water, Salt)',
                          'Sea Salt',
                          'Poppy Seeds*',
                          'Black Pepper']


def formatted_menu(date, onlySellableMenuItems=False):
    formatted_menu = {
        'name': f"{date} 1_2_3",
        'id': 'MENU123ABC',
        'date': f"{date}",
        'location': DEFAULT_LOCATION,
        'categoryMenuType': DEFAULT_MENU_TYPE,
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
        data = {
            "ingredient": {
                "name": "spinach, baby, SEND TO PLATE",
                "externalName": "Baby Spinach*",
                "categoryValues": []
            },
            "quantity": 3,
            "unit": {
                "id": "dW5pdDoz",
                "name": "oz",
                "unitValues": [
                    {"value": 28, "unit": {"id": "dW5pdDox", "name": "g"}},
                    {"value": 1, "unit": {"id": "dW5pdDoz", "name": "oz"}},
                    {"value": 0.18, "unit": {"id": "dW5pdDo0", "name": "lb"}}
                ]
            }
        }
        recipe_item = RecipeItem(data)
        result = recipe_item.mass()
        self.assertEqual(result, 84)

    def test_get_ingredients_with_usages_successful(self):
        self.maxDiff = None
        result = get_recipe_ingredients_and_standalone_data(
            MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES
        )
        self.assertEqual(result['ingredients'], ['Buckwheat Groats',
                                                 'Spring Mix Lettuce*, Kale* or Seasonal Greens*§',
                                                 'Kidney Beans*',
                                                 'Rainbow Carrots*',
                                                 'Red Beets',
                                                 'Dried Cherries*',
                                                 'Hemp Seeds',
                                                 'Pumpkin Seed',
                                                 'Sunflower Seeds',
                                                 'Extra Virgin Olive Oil',
                                                 'Parsley',
                                                 'Sea Salt',
                                                 'Rice Bran Oil',
                                                 'Garlic Powder',
                                                 'Chili Powder',
                                                 'Cumin'])

    def test_get_ingredient_usages_empty(self):
        recipe = {'recipeItems': [], 'ingredientsWithUsages': []}
        result = get_recipe_ingredients_and_standalone_data(recipe)
        self.assertEqual(result['ingredients'], [])


class TestIngredientExternalName(TestCase):
    def test_should_return_name_if_no_external_name(self):
        NAME = 'name'
        ingredient = {
            'name': NAME,
            'externalName': None
        }
        result = get_ingredient_name(ingredient)
        self.assertEqual(result, NAME)

    def test_should_return_none_if_no_external_name_or_name(self):
        ingredient = {
            'name': None,
            'externalName': None
        }
        result = get_ingredient_name(ingredient)
        self.assertEqual(result, None)

    def test_should_return_external_name_if_no_ingredientListStr(self):
        NAME = 'cloved, garlic'
        EXTERNAL_NAME = 'Garlic'
        ingredient = {
            'name': NAME,
            'externalName': EXTERNAL_NAME,
            'locationVendorItems': [{
                'vendorItems': [{
                    "name": NAME,
                    "priority": 0,
                    "ingredientListStr": None
                }]
            }]
        }
        result = get_ingredient_name(ingredient)
        self.assertEqual(result, EXTERNAL_NAME)

    def test_should_return_external_name_plus_ingredientListStr_if_ingredientListStr(self):
        NAME = 'cloved, garlic'
        EXTERNAL_NAME = 'Garlic'
        INGREDIENT_STRING = 'Stuff, Water'
        ingredient = {
            'name': NAME,
            'externalName': EXTERNAL_NAME,
            'locationVendorItems': [{
                'vendorItems': [{
                    "name": NAME,
                    "priority": 0,
                    'ingredientListStr': INGREDIENT_STRING
                }]
            }]
        }
        result = get_ingredient_name(ingredient)
        self.assertEqual(result, f'{EXTERNAL_NAME} ({INGREDIENT_STRING})')

    def test_should_return_name_plus_ingredientListStr_if_name_and_ingredientListStr_and_no_externalName(self):
        NAME = 'cloved, garlic'
        VENDOR_NAME = 'seasoned garlic'
        INGREDIENT_STRING = 'Stuff, Water'
        ingredient = {
            'name': NAME,
            'externalName': None,
            'locationVendorItems': [{
                'vendorItems': [{
                    "name": VENDOR_NAME,
                    "priority": 0,
                    'ingredientListStr': INGREDIENT_STRING
                }]
            }]
        }
        result = get_ingredient_name(ingredient)
        self.assertEqual(result,  f'{NAME} ({INGREDIENT_STRING})')

    def test_should_return_ingredientListStr_of_vendorItem_with_priority(self):
        NAME = 'cloved, garlic'
        EXTERNAL_NAME = 'Garlic'
        INGREDIENT_STRING = 'Stuff, Water'
        PRIORITY_INGREDIENT_STRING = 'Priority Stuff, Water'
        ingredient = {
            'name': NAME,
            'externalName':  EXTERNAL_NAME,
            'locationVendorItems': [{
                'vendorItems': [{
                    'priority': 1,
                    'ingredientListStr': INGREDIENT_STRING
                },{
                    'priority': 0,
                    'ingredientListStr': PRIORITY_INGREDIENT_STRING
                }]
            }]
        }
        result = get_ingredient_name(ingredient)
        self.assertEqual(result, f'{EXTERNAL_NAME} ({PRIORITY_INGREDIENT_STRING})')


class TestRecipeItemLabelName(TestCase):
    def test_returns_none_if_not_a_label(self):
        data = {
            'ingredient': {
                'categoryValues': [{
                    'id': 'NotALabelId'
                }]
            }
        }
        recipe_item = RecipeItem(data)
        self.assertEqual(recipe_item.get_label_name(), None)

    def test_returns_none_if_is_a_label_but_no_external_name_or_name(self):
        data = {
            'ingredient': {
                'categoryValues': [{
                    'id': IngredientCategoryValueEnum.LABEL.value
                }]
            }
        }
        recipe_item = RecipeItem(data)
        self.assertEqual(recipe_item.get_label_name(), None)

    def test_returns_external_name_if_exists_and_is_a_label(self):
        NAME = 'meal label'
        EXTERNAL_NAME = 'Meat Meal Label'
        data = {
            'ingredient': {
                'name': NAME,
                'externalName': EXTERNAL_NAME,
                'categoryValues': [{
                    'id': IngredientCategoryValueEnum.LABEL.value
                }],
            }
        }
        recipe_item = RecipeItem(data)
        self.assertEqual(recipe_item.get_label_name(), EXTERNAL_NAME)

    def test_returns_name_if_external_name_does_not_exist_and_is_a_label(self):
        NAME = 'meal label'
        data = {
            'ingredient': {
                'name': NAME,
                'externalName': None,
                'categoryValues': [{
                    'id': IngredientCategoryValueEnum.LABEL.value
                }],
            }
        }
        recipe_item = RecipeItem(data)
        self.assertEqual(recipe_item.get_label_name(), NAME)


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
    def test_weights_with_pkg_and_standalone(self):
        result = get_recipe_weights(MOCK_RECIPE_ITEMS)
        self.assertEqual(result['netWeight'], 435)
        self.assertEqual(result['grossWeight'], 557)

    def test_weight_from_recipe_items_successful_no_pkg_no_standalone(self):
        result = get_recipe_weights(MOCK_RECIPE_ITEMS[:3])
        self.assertEqual(result['netWeight'], 435)
        self.assertEqual(result['grossWeight'], 435)

    def test_weight_from_recipe_items_empty(self):
        result = get_recipe_weights([])
        self.assertEqual(result['netWeight'], 0)
        self.assertEqual(result['grossWeight'], 0)

    def test_format_data_with_standalone_component(self):
        self.maxDiff = None
        weights = get_recipe_weights(MOCK_RECIPE_ITEMS)
        ingredients_and_standalone_data = get_recipe_ingredients_and_standalone_data(
            MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES
        )
        result = weights | ingredients_and_standalone_data
        expected = {
            'ingredients': BASE_INGREDIENTS,
            'netWeight': 435,
            'grossWeight': 557,
            'hasStandalone': True,
            'labelName': "Vegan Meal Label",
            'standaloneRecipeId': STANDALONE_RECIPE_ID,
            'standaloneRecipeName': STANDALONE_RECIPE_NAME,
            'standaloneNutrition': MOCK_STANDALONE_RECONCILED_NUTRITIONALS,
            'standaloneIngredients': STANDALONE_INGREDIENTS,
            'standaloneNetWeight': 57,
            'standaloneSuggestedServing': "1 oz",
            'standaloneServingSizeWeight': 28,
            'standaloneServings': 2.0,
        }
        self.assertEqual(result, expected)

    def test_format_recipe_tree_components_data_with_standalone_missing_nutritionals_quantity_data(self):
        recipeItems = deepcopy(MOCK_RECIPE_ITEMS)
        ingredientsWithUsages = deepcopy(MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES['ingredientsWithUsages'])
        recipeItems[3]['subRecipe']['nutritionalsQuantity'] = None
        recipeItems[3]['subRecipe']['nutritionalsUnit'] = None
        data = {'recipeItems': recipeItems, 'ingredientsWithUsages': ingredientsWithUsages}

        weights = get_recipe_weights(recipeItems)
        ingredients_and_standalone_data = get_recipe_ingredients_and_standalone_data(data)
        result = weights | ingredients_and_standalone_data
        expected = {
            'ingredients': BASE_INGREDIENTS,
            'netWeight': 435,
            'grossWeight': 557,
            'hasStandalone': True,
            'labelName': "Vegan Meal Label",
            'standaloneRecipeId': STANDALONE_RECIPE_ID,
            'standaloneRecipeName': STANDALONE_RECIPE_NAME,
            'standaloneNutrition': MOCK_STANDALONE_RECONCILED_NUTRITIONALS,
            'standaloneIngredients': STANDALONE_INGREDIENTS,
            'standaloneNetWeight': 57,
            'standaloneSuggestedServing': None,
            'standaloneServingSizeWeight': None,
            'standaloneServings': None,
        }
        self.assertEqual(result, expected)


class TestGetRecipeCategoryTags(TestCase):
    def test_get_recipe_category_tags_with_all_tags_populated(self):
        recipe_category_values = MOCK_RECIPE_CATEGORY_VALUES
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
        expected_result = {
            'highlightTags': [],
            'displayNutritionOnWebsite': True
        }

        result = get_recipe_category_tags(MOCK_RECIPE_ITEMS)
        self.assertEqual(result, expected_result)

    def test_get_recipe_category_tags_with_just_one_highlight_tag(self):
        recipe_category_values = MOCK_RECIPE_CATEGORY_VALUES
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
    def test_get_formatted_recipe_data_with_standalone_successful(self, mock_retrieval_method):
        self.maxDiff = None
        expected_result = [
            {
                'id': SELLABLE_RECIPE_ID,
                'externalName': SELLABLE_RECIPE_NAME,
                'version': 'dmVyc2lvbjozNjQ0NTY1',
                'notes': f'Some notes about recipe {SELLABLE_RECIPE_ID}',
                'description': f'Details about recipe {SELLABLE_RECIPE_ID}',
                'labelName': 'Vegan Meal Label',
                'menuPhotoUrl': f'https://cdn.filestackcontent.com/MENU{SELLABLE_RECIPE_ID}',
                'nutrition': MOCK_RECONCILED_NUTRITIONALS,
                'proteinType': 'vegan',
                'mealContainer': 'ts48',
                'mealType': 'dinner',
                'proteinAddOn': 'high-protein-legume',
                'baseMealSlug': 'base-salad',
                'baseMeal': 'Base Salad Name',
                'highlightTags': ['new', 'spicy'],
                'displayNutritionOnWebsite': True,
                'ingredients': BASE_INGREDIENTS,
                'netWeight': 435,
                'grossWeight': 557,
                'hasStandalone': True,
                'standaloneIngredients': STANDALONE_INGREDIENTS,
                'standaloneNutrition': MOCK_STANDALONE_RECONCILED_NUTRITIONALS,
                'standaloneRecipeId': STANDALONE_RECIPE_ID,
                'standaloneRecipeName': STANDALONE_RECIPE_NAME,
                'standaloneNetWeight': 57,
                'standaloneSuggestedServing': "1 oz",
                'standaloneServingSizeWeight': 28,
                'standaloneServings': 2.0,
                'hasAllergen': False,
                'allergens': []
            }
        ]
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': mock_recipe(SELLABLE_RECIPE_ID)
                        }]
                    }
                }
            }
        }
        result = get_formatted_recipes_data(recipe_ids=[SELLABLE_RECIPE_ID], location_name=DEFAULT_LOCATION)
        self.assertEqual(result, expected_result)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_empty(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': {}
                        }]
                    }
                }
            }
        }
        result = get_formatted_recipes_data(recipe_ids=[SELLABLE_RECIPE_ID], location_name=DEFAULT_LOCATION)
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_missing(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': None
                        }]
                    }
                }
            }
        }
        result = get_formatted_recipes_data(recipe_ids=['1', '2'], location_name=DEFAULT_LOCATION)
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
        mock_grmd.assert_called_with(dates, DEFAULT_LOCATION, DEFAULT_MENU_TYPE)
        get_formatted_menu_data(dates, 'Montana', 'staging')
        mock_grmd.assert_called_with(dates, 'Montana', 'staging')

    def test_get_formatted_menu_data_base_meal_title_format(self):
        self.assertEqual(format_title("beet-poke"), "Beet-Poke")
        self.assertEqual(format_title("persephone's salad"), "Persephone's Salad")
        self.assertEqual(format_title("brussel sprout & asian pear 'fried' rice"),
                         "Brussel Sprout & Asian Pear 'Fried' Rice")
        self.assertEqual(format_title("beetroot quinoa & sun 'cheese' salad"),
                         "Beetroot Quinoa & Sun 'Cheese' Salad")

    def test_should_throw_error_if_location_provided_is_None(self):
        with self.assertRaises(ValueError):
            get_formatted_recipes_data(recipe_ids=[], location_name=None)
