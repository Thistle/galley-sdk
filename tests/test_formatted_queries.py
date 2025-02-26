from unittest import TestCase, mock
from galley.enums import DietaryFlagEnum, IngredientCategoryValueEnum, RecipeCategoryTagTypeEnum
from tests.mock_responses.mock_menu_data import mock_menu
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.formatted_queries import (
    ALLERGEN_LABELS,
    RecipeItem,
    format_title,
    get_recipe_label_and_weights,
    calculate_servings,
    get_ingredient_name,
    get_formatted_menu_data,
    get_recipe_category_tags,
    get_formatted_recipes_data,
    calculate_serving_size_weight,
    get_recipe_ingredients_and_standalone_data,
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
    MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_NO_STANDALONE,
    MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE,
)


BASE_INGREDIENTS = ['Rainbow Carrots*',
                    'Buckwheat Groats',
                    'Spring Mix Lettuce*, Kale* or Seasonal Greens*§',
                    'Kidney Beans*',
                    'Red Beets',
                    'Dried Cherries*',
                    'Pumpkin Seed',
                    'Extra Virgin Olive Oil',
                    'Parsley',
                    'Rice Bran Oil',
                    'Sea Salt']


STANDALONE_INGREDIENTS = ['Rice Bran Oil',
                          'Aquafaba (Chickpeas, Water)*',
                          'Maple Syrup*',
                          'Dijon Mustard (Water, Mustard Seeds, Vinegar, Salt)',
                          'Garlic',
                          'Apple Cider Vinegar',
                          'Garbanzo Beans (Garbanzo Beans, Water, Salt)',
                          'Poppy Seeds*',
                          'Sea Salt']


BASE_RECIPE_ALLERGENS = [ALLERGEN_LABELS[DietaryFlagEnum.COCONUT.name]]
STANDALONE_ALLERGENS = [ALLERGEN_LABELS[DietaryFlagEnum.SOYBEANS.name]]
SELLABLE_RECIPE_ALLERGENS = BASE_RECIPE_ALLERGENS + STANDALONE_ALLERGENS

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
            'recipeMenuModalPhotoUrl': 'https://cdn.filestackcontent.com/Recipe_1_Menu_Modal',
            'recipeName': 'Test Recipe Name 1',
            'recipeProteinType': 'vegan',
            'volume': 100,
        }, {
            'allergens': SELLABLE_RECIPE_ALLERGENS,
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
            'recipeMenuModalPhotoUrl': 'https://cdn.filestackcontent.com/Recipe_2_Menu_Modal',
            'recipeName': 'Test Recipe Name 2',
            'recipeProteinType': 'vegan',
            'volume': 0,
        }, {
            'allergens': STANDALONE_ALLERGENS,
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
            'recipeMenuModalPhotoUrl': 'https://cdn.filestackcontent.com/Recipe_3_Menu_Modal',
            'recipeName': 'Test Recipe Name 3',
            'recipeProteinType': 'meat',
            'volume': None,
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
            'recipeMenuModalPhotoUrl': None,
            'recipeName': 'Test Recipe Name 4',
            'recipeProteinType': '',
            'volume': 300,
        })
    return formatted_menu


class TestIngredientsFromRecipeItems(TestCase):
    def test_get_ingredient_usage_successful(self):
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
        result = get_recipe_ingredients_and_standalone_data(
            MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE()
        )
        self.assertEqual(result['ingredients'], BASE_INGREDIENTS)

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
        result = get_recipe_label_and_weights(MOCK_RECIPE_ITEMS)
        self.assertEqual(result['netWeight'], 435)
        self.assertEqual(result['grossWeight'], 557)

    def test_weight_from_recipe_items_successful_no_pkg_no_standalone(self):
        result = get_recipe_label_and_weights(MOCK_RECIPE_ITEMS[:3])
        self.assertEqual(result['netWeight'], 435)
        self.assertEqual(result['grossWeight'], 435)

    def test_weight_from_recipe_items_empty(self):
        result = get_recipe_label_and_weights([])
        self.assertEqual(result['netWeight'], 0)
        self.assertEqual(result['grossWeight'], 0)

    def test_format_data_with_standalone_component(self):
        weights = get_recipe_label_and_weights(MOCK_RECIPE_ITEMS)
        ingredients_and_standalone_data = get_recipe_ingredients_and_standalone_data(
            MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE()
        )
        result = weights | ingredients_and_standalone_data
        expected = {
            'ingredients': BASE_INGREDIENTS,
            'baseRecipeAllergens': BASE_RECIPE_ALLERGENS,
            'netWeight': 435,
            'grossWeight': 557,
            'hasStandalone': True,
            'labelName': "Vegan Meal Label",
            'standaloneRecipeId': STANDALONE_RECIPE_ID,
            'standaloneRecipeName': STANDALONE_RECIPE_NAME,
            'standaloneNutrition': MOCK_STANDALONE_RECONCILED_NUTRITIONALS,
            'standaloneIngredients': STANDALONE_INGREDIENTS,
            'standaloneAllergens': STANDALONE_ALLERGENS,
            'standaloneNetWeight': 57,
            'standaloneSuggestedServing': "1 oz",
            'standaloneServingSizeWeight': 28,
            'standaloneServings': 2.0,
        }
        self.assertEqual(result, expected)

    def test_format_recipe_tree_components_data_with_standalone_missing_nutritionals_quantity_data(self):
        data = MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE()
        data['recipeItems'][3]['subRecipe']['nutritionalsQuantity'] = None
        data['recipeItems'][3]['subRecipe']['nutritionalsUnit'] = None

        weights = get_recipe_label_and_weights(data['recipeItems'])
        ingredients_and_standalone_data = get_recipe_ingredients_and_standalone_data(data)
        result = weights | ingredients_and_standalone_data
        expected = {
            'ingredients': BASE_INGREDIENTS,
            'baseRecipeAllergens': BASE_RECIPE_ALLERGENS,
            'netWeight': 435,
            'grossWeight': 557,
            'hasStandalone': True,
            'labelName': "Vegan Meal Label",
            'standaloneRecipeId': STANDALONE_RECIPE_ID,
            'standaloneRecipeName': STANDALONE_RECIPE_NAME,
            'standaloneNutrition': MOCK_STANDALONE_RECONCILED_NUTRITIONALS,
            'standaloneIngredients': STANDALONE_INGREDIENTS,
            'standaloneAllergens': STANDALONE_ALLERGENS,
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
        expected_result = [
            {
                'id': SELLABLE_RECIPE_ID,
                'externalName': SELLABLE_RECIPE_NAME,
                'version': 'dmVyc2lvbjozNjQ0NTY1',
                'notes': f'Some notes about recipe {SELLABLE_RECIPE_ID}',
                'description': f'Details about recipe {SELLABLE_RECIPE_ID}',
                'labelName': 'Vegan Meal Label',
                'menuPhotoUrl': f'https://cdn.filestackcontent.com/MENU{SELLABLE_RECIPE_ID}',
                'menuModalPhotoUrl': f'https://cdn.filestackcontent.com/MODAL{SELLABLE_RECIPE_ID}',
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
                'baseRecipeAllergens': BASE_RECIPE_ALLERGENS,
                'netWeight': 435,
                'grossWeight': 557,
                'hasStandalone': True,
                'standaloneIngredients': STANDALONE_INGREDIENTS,
                'standaloneNutrition': MOCK_STANDALONE_RECONCILED_NUTRITIONALS,
                'standaloneRecipeId': STANDALONE_RECIPE_ID,
                'standaloneRecipeName': STANDALONE_RECIPE_NAME,
                'standaloneAllergens': STANDALONE_ALLERGENS,
                'standaloneNetWeight': 57,
                'standaloneSuggestedServing': "1 oz",
                'standaloneServingSizeWeight': 28,
                'standaloneServings': 2.0,
                'hasAllergen': True,
                'allergens': SELLABLE_RECIPE_ALLERGENS
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
        result = get_formatted_recipes_data(recipe_ids=[SELLABLE_RECIPE_ID], location_name=DEFAULT_LOCATION)
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_no_standalone(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_NO_STANDALONE()
                        }]
                    }
                }
            }
        }
        result = get_formatted_recipes_data(recipe_ids=[SELLABLE_RECIPE_ID], location_name=DEFAULT_LOCATION)
        self.assertEqual(result[0]['ingredients'], BASE_INGREDIENTS)
        self.assertEqual(result[0]['hasStandalone'], False)
        self.assertEqual(result[0]['standaloneRecipeName'], None)
        self.assertEqual(result[0]['standaloneRecipeId'], None)
        self.assertEqual(result[0]['standaloneNetWeight'], None)
        self.assertEqual(result[0]['standaloneAllergens'], None)
        self.assertEqual(result[0]['standaloneSuggestedServing'], None)
        self.assertEqual(result[0]['standaloneServingSizeWeight'], None)
        self.assertEqual(result[0]['standaloneServings'], None)
        self.assertEqual(result[0]['standaloneIngredients'], None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_with_allergen_and_standalone_successful(self, mock_retrieval_method):
        mock_recipe_data = mock_recipe(SELLABLE_RECIPE_ID)
        mock_recipe_data['dietaryFlagsWithUsages'] = [{
            'dietaryFlag': {
                'id': DietaryFlagEnum.SOYBEANS.id,
                'name': DietaryFlagEnum.SOYBEANS.name,
            }
        }, {
            'dietaryFlag': {
                'id': DietaryFlagEnum.COCONUT.id,
                'name': DietaryFlagEnum.COCONUT.name,
            }
        }]
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': mock_recipe_data
                        }]
                    }
                }
            }
        }
        result = get_formatted_recipes_data(recipe_ids=[SELLABLE_RECIPE_ID], location_name=DEFAULT_LOCATION)
        self.assertEqual(result[0]['ingredients'], BASE_INGREDIENTS)
        self.assertEqual(result[0]['baseRecipeAllergens'], BASE_RECIPE_ALLERGENS)
        self.assertEqual(result[0]['hasStandalone'], True)
        self.assertEqual(result[0]['standaloneRecipeName'], STANDALONE_RECIPE_NAME)
        self.assertEqual(result[0]['standaloneRecipeId'], STANDALONE_RECIPE_ID)
        self.assertEqual(result[0]['standaloneNetWeight'], 57)
        self.assertEqual(result[0]['standaloneAllergens'], STANDALONE_ALLERGENS)
        self.assertEqual(result[0]['standaloneSuggestedServing'], "1 oz")
        self.assertEqual(result[0]['standaloneServingSizeWeight'], 28)
        self.assertEqual(result[0]['standaloneServings'], 2.0)
        self.assertEqual(result[0]['standaloneIngredients'], STANDALONE_INGREDIENTS)
        self.assertEqual(result[0]['hasAllergen'], True)
        self.assertEqual(result[0]['allergens'], SELLABLE_RECIPE_ALLERGENS)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_recipes_data_with_non_supported_allergen_successful(self, mock_retrieval_method):
        mock_recipe_data = mock_recipe(SELLABLE_RECIPE_ID)
        mock_recipe_data['dietaryFlagsWithUsages'] = [{
            'dietaryFlag': {
                'id': DietaryFlagEnum.SULPHITES.id,
                'name': DietaryFlagEnum.SULPHITES.name,
            }
        }]
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': mock_recipe_data
                        }]
                    }
                }
            }
        }
        result = get_formatted_recipes_data(recipe_ids=[SELLABLE_RECIPE_ID], location_name=DEFAULT_LOCATION)
        self.assertEqual(result[0]['hasAllergen'], False)
        self.assertEqual(result[0]['allergens'], [])


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
        self.assertEqual(format_title("brussel sprout & asian pear 'fried' rice"), "Brussel Sprout & Asian Pear 'Fried' Rice")
        self.assertEqual(format_title("beetroot quinoa & sun 'cheese' salad"), "Beetroot Quinoa & Sun 'Cheese' Salad")

    def test_should_throw_error_if_location_provided_is_None(self):
        with self.assertRaises(ValueError):
            get_formatted_recipes_data(recipe_ids=[], location_name=None)
