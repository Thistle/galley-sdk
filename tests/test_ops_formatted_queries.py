from copy import deepcopy
from unittest import TestCase, mock
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.enums import DietaryFlagEnum as DF, PreparationEnum
from galley.formatted_queries import get_menu_type, get_item_code
from galley.formatted_ops_queries import RecipeItem, format_components, get_formatted_ops_menu_data
from tests.mock_responses.mock_ops_menu_data import SESAME_SEEDS, SOY, TREE_NUTS, mock_ops_menu, MOCK_RECIPE_TREE_COMPONENTS, MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS


def formatted_ops_menu(date, location_name=DEFAULT_LOCATION, menu_type=DEFAULT_MENU_TYPE):
    formatted_ops_menu = {
        'name': f'{date} 1_2_3',
        'id': 'MENU123ABC-OPS',
        'date': f'{date}',
        'location': location_name,
        'categoryMenuType': menu_type,
        'menuItems': [{
            'menuItemId': 'MENUITEM1ABC-OPS',
            'mealCode': 'lm1',
            'recipeId': 'RECIPE1ABC-OPS',
            'recipeName': 'Test Recipe Name 1',
            'mealContainer': 'ts48',
            'platePhotoUrl': 'https://cdn.filestackcontent.com/2X5ivrEYQvuEh30DyYot',
            'totalCount': 923,
            'totalCountUnit': 'each',
            'primaryRecipeComponents': MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS,

        }, {
            'menuItemId': 'MENUITEM2DEF-OPS',
            'mealCode': 'lv2',
            'recipeId': 'RECIPE2DEF-OPS',
            'recipeName': 'Test Recipe Name 2',
            'mealContainer': 'ts32',
            'platePhotoUrl': 'https://cdn.filestackcontent.com/IQM3KcAkRye81xuN5JY4',
            'totalCount': 1228,
            'totalCountUnit': 'each',
            'primaryRecipeComponents': MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS,

        }, {
            'menuItemId': 'MENUITEM3GHI-OPS',
            'mealCode': 'dv3',
            'recipeId': 'RECIPE3GHI-OPS',
            'recipeName': 'Test Recipe Name 3',
            'mealContainer': 'ts32',
            'platePhotoUrl': None,
            'totalCount': 549,
            'totalCountUnit': 'each',
            'primaryRecipeComponents': MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS,

        }, {
            'menuItemId': 'MENUITEM4JKL-OPS',
            'mealCode': 'ssa',
            'recipeId': 'RECIPE4JKL-OPS',
            'recipeName': 'Jar Salad 1',
            'mealContainer': 'ts32',
            'platePhotoUrl': None,
            'totalCount': 123,
            'totalCountUnit': 'each',
            'primaryRecipeComponents': MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS,
        }, {
            'menuItemId': 'MENUITEM5MNO-OPS',
            'mealCode': 'sch',
            'recipeId': 'RECIPE5MNO-OPS',
            'recipeName': 'Side Soup 4',
            'mealContainer': 'ts32',
            'platePhotoUrl': None,
            'totalCount': 321,
            'totalCountUnit': 'each',
            'primaryRecipeComponents': MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS,
        }]
    }
    return formatted_ops_menu


class TestMealCodeFromMenuItemCategoryValues(TestCase):
    def test_get_item_code_successful(self):
        expected_result = 'lv2'
        result = get_item_code(mock_ops_menu('2022-03-28')['menuItems'][1])
        self.assertEqual(result, expected_result)

    def test_get_item_code_empty(self):
        result = get_item_code({})
        self.assertEqual(result, '')


class TestGetMenuTypeFromMenuCategoryValues(TestCase):
    def test_get_menu_type_successful(self):
        expected_result = DEFAULT_MENU_TYPE
        result = get_menu_type(mock_ops_menu('2022-03-28'))
        self.assertEqual(result, expected_result)

    def test_get_menu_type_empty(self):
        result = get_menu_type({})
        self.assertEqual(result, '')


class TestFormattedRecipeInstructions(TestCase):
    def test_format_instructions_successful(self):
        recipeitem = {
            "preparations": [],
            "ingredient": None,
            "subRecipe": {
                "recipeInstructions": [
                    {"text": "In blixer combine half of the liquids to break up the red onion and garlic.", "position": 0},
                    {"text": "Slowly add in oil through opening on the lid until emulsified.", "position": 1},
                    {"text": "Pour into lexans.", "position": 2}
                ]
            }
        }
        expected = [
            {"id": 1, "text": "In blixer combine half of the liquids to break up the red onion and garlic."},
            {"id": 2, "text": "Slowly add in oil through opening on the lid until emulsified."},
            {"id": 3, "text": "Pour into lexans."}
        ]
        result = RecipeItem(recipeitem=recipeitem).format_instructions()
        self.assertEqual(result, expected)

    def test_format_instructions_empty(self):
        recipeitem = {
            "preparations": [],
            "ingredient": None,
            "subRecipe": {
                "recipeInstructions": []
            }
        }
        result = RecipeItem(recipeitem=recipeitem).format_instructions()
        self.assertEqual(result, [])

    def test_format_instructions_None(self):
        recipeitem = {
            "preparations": [],
            "ingredient": None,
            "subRecipe": {
                "recipeInstructions": None
            }
        }
        result = RecipeItem(recipeitem=recipeitem).format_instructions()
        self.assertEqual(result, [])


class TestFormattedCuppingContainerData(TestCase):
    def test_get_cupping_container_data_successful(self):
        recipeitem = {
            "preparations": [
                {"id": PreparationEnum.TWO_OZ_WINPAK.value, "name": "2 oz WINPAK"},
                {"id": PreparationEnum.STANDALONE.value, "name": "standalone"}
            ],
            "ingredient": None,
            "subRecipe": {}
        }
        result = RecipeItem(recipeitem=recipeitem).get_cupping_container()
        self.assertEqual(result, '2 oz WINPAK')

    def test_get_cupping_container_data_empty_preparations(self):
        recipeitem = {
            "preparations": [],
            "ingredient": None,
            "subRecipe": {}
        }
        result = RecipeItem(recipeitem=recipeitem).get_cupping_container()
        self.assertEqual(result, None)

    def test_get_cupping_container_data_null_preparations(self):
        recipeitem = {
            "preparations": None,
            "ingredient": None,
            "subRecipe": {}
        }
        result = RecipeItem(recipeitem=recipeitem).get_cupping_container()
        self.assertEqual(result, None)


def idx(key, value):
    return MOCK_RECIPE_TREE_COMPONENTS.index(next(filter(
        lambda rtc: rtc[key] == value,
        MOCK_RECIPE_TREE_COMPONENTS
    )))


class TestFormattedAllergenData(TestCase):
    def setUp(self):
        self.MOCK_RECIPE_TREE_COMPONENTS = deepcopy(MOCK_RECIPE_TREE_COMPONENTS)

    def test_format_recipe_allergen_data_successful(self):
        recipeitem = self.MOCK_RECIPE_TREE_COMPONENTS[idx("id", "hdeta8wr90j")]['recipeItem']
        result = RecipeItem(recipeitem=recipeitem).format_allergens()
        self.assertEqual(result, [SOY])

    def test_format_ingredient_allergen_data_successful(self):
        recipeitem = self.MOCK_RECIPE_TREE_COMPONENTS[idx("id", "8o8ode59qdc")]['recipeItem']
        result = RecipeItem(recipeitem=recipeitem).format_allergens()
        self.assertEqual(result, [SESAME_SEEDS, TREE_NUTS])

    def test_format_recipe_allergen_data_empty(self):
        recipeitem = {
            "preparations": [],
            "ingredient": None,
            "subRecipe": {
                "dietaryFlagsWithUsages": []
            }
        }
        result = RecipeItem(recipeitem=recipeitem).format_allergens()
        self.assertEqual(result, [])

    def test_format_ingredient_allergen_data_empty(self):
        recipeitem = {
            "preparations": [],
            "ingredient": {
                "dietaryFlags": []
            },
            "subRecipe": None
        }
        result = RecipeItem(recipeitem=recipeitem).format_allergens()
        self.assertEqual(result, [])

    def test_format_recipe_allergen_data_None(self):
        recipeitem = {
            "preparations": [],
            "ingredient": None,
            "subRecipe": {
                "dietaryFlagsWithUsages": None
            }
        }
        result = RecipeItem(recipeitem=recipeitem).format_allergens()
        self.assertEqual(result, [])

    def test_format_recipe_allergen_data_None(self):
        recipeitem = {
            "preparations": [],
            "ingredient": {
                "dietaryFlags": None
            },
            "subRecipe": None
        }
        result = RecipeItem(recipeitem=recipeitem).format_allergens()
        self.assertEqual(result, [])


class TestGetFormattedBinWeightData(TestCase):
    def setUp(self):
        self.MOCK_RECIPE_TREE_COMPONENTS = deepcopy(MOCK_RECIPE_TREE_COMPONENTS)

    def test_get_formatted_dynamic_recipe_bin_weight_data_successful(self):
        recipeitem = self.MOCK_RECIPE_TREE_COMPONENTS[idx("id", "d44pdeapsdk")]['recipeItem']
        result = RecipeItem(recipeitem=recipeitem).format_bin_weight()
        self.assertEqual(result, {'value': 50, 'unit': 'lb'})

    def test_get_formatted_dynamic_ingredient_bin_weight_data_successful(self):
        recipeitem = self.MOCK_RECIPE_TREE_COMPONENTS[idx("id", "3oiimc548lt")]['recipeItem']
        result = RecipeItem(recipeitem=recipeitem).format_bin_weight()
        self.assertEqual(result, {'value': 30, 'unit': 'lb'})

    def test_get_formatted_recipe_bin_weight_with_recipe_category_values_empty(self):
        recipeitem = self.MOCK_RECIPE_TREE_COMPONENTS[idx("id", "wuet0e3vilq")]['recipeItem']
        result = RecipeItem(recipeitem=recipeitem).format_bin_weight()
        self.assertEqual(result, {'value': 60, 'unit': 'lb'})

    def test_get_formatted_ingredient_bin_weight_with_ingredient_category_values_empty(self):
        recipeitem = self.MOCK_RECIPE_TREE_COMPONENTS[idx("id", "ss91mevjky")]['recipeItem']
        result = RecipeItem(recipeitem=recipeitem).format_bin_weight()
        self.assertEqual(result, {'value': 60, 'unit': 'lb'})

    def test_get_formatted_recipe_bin_weight_with_recipe_category_values_None(self):
        recipeitem = {
            "preparations": [],
            "ingredient": {
                "categoryValues": None
            },
            "subRecipe": None
        }
        result = RecipeItem(recipeitem=recipeitem).format_bin_weight()
        self.assertEqual(result, {'value': 60, 'unit': 'lb'})

    def test_get_formatted_ingredient_bin_weight_with_ingredient_category_values_None(self):
        recipeitem = {
            "preparations": [],
            "ingredient": None,
            "subRecipe": {
                "categoryValues": None
            }
        }
        result = RecipeItem(recipeitem=recipeitem).format_bin_weight()
        self.assertEqual(result, {'value': 60, 'unit': 'lb'})


class TestGetFormattedOpsMenuData(TestCase):
    def response(self, *menus):
        return ({
            'data': {
                'viewer': {
                    'menus': [m for m in menus if m]
                }
            }
        })

    def test_format_primary_recipe_components(self):
        result = format_components(deepcopy(MOCK_RECIPE_TREE_COMPONENTS))
        self.assertEqual(result, MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_returns_whitelisted_meal_codes(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_ops_menu('2022-03-28'))
        result = get_formatted_ops_menu_data(['2022-03-28'])
        meal_codes = set(mi['mealCode'] for mi in result[0]['menuItems'])
        self.assertTrue('av' not in meal_codes and 'hla' not in meal_codes)
        self.assertEqual(set(['lm1', 'lv2', 'dv3', 'ssa', 'sch']), meal_codes)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_successful_for_one_valid_menu(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_ops_menu('2022-03-28'))
        result = get_formatted_ops_menu_data(['2022-03-28'])
        self.assertEqual(result, [formatted_ops_menu('2022-03-28')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_successful_for_multiple_valid_menus(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(
            mock_ops_menu('2022-03-28'),
            mock_ops_menu('2022-04-04'),
            mock_ops_menu('2022-04-18')
        )
        result = get_formatted_ops_menu_data(['2022-03-28', '2022-04-04', '2022-04-18'])
        self.assertEqual(result, [
            formatted_ops_menu('2022-03-28'),
            formatted_ops_menu('2022-04-04'),
            formatted_ops_menu('2022-04-18')
        ])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_exception(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        with self.assertRaises(ValueError):
            get_formatted_ops_menu_data([])

    @mock.patch('galley.formatted_ops_queries.get_raw_menu_data')
    def test_get_formatted_ops_menu_data_args_defaults(self, mock_raw_menu_data):
        dates = ['2022-03-28', '2022-04-04']
        get_formatted_ops_menu_data(dates)
        mock_raw_menu_data.assert_called_with(dates, DEFAULT_LOCATION, DEFAULT_MENU_TYPE, is_ops=True)
        get_formatted_ops_menu_data(dates, 'Montana', 'staging')
        mock_raw_menu_data.assert_called_with(dates, 'Montana', 'staging', is_ops=True)
