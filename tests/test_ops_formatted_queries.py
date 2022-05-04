from unittest import TestCase, mock

from galley.formatted_queries import (
    get_category_menu_type,
    get_meal_code
)
from galley.formatted_ops_queries import get_formatted_ops_menu_data, format_recipe_instructions, format_allergens, format_bin_weight
from galley.enums import DietaryFlagEnum

from tests.mock_responses.mock_ops_menu_data import (
    mock_ops_menu,
    mock_recipeTreeComponents,
    mock_formatted_primaryRecipeComponents,
)


def formatted_ops_menu(date, location_name='Vacaville', menu_type='production'):
    formatted_ops_menu = {
        'name': f'{date} 1_2_3',
        'id': 'MENU123ABC-OPS',
        'date': f'{date}',
        'location': location_name,
        'categoryMenuType': menu_type,
        'menuItems': [{
            'mealCode': 'lm1',
            'recipeId': 'RECIPE1ABC-OPS',
            'recipeName': 'Test Recipe Name 1',
            'mealContainer': 'ts48',
            'platePhotoUrl': 'https://cdn.filestackcontent.com/2X5ivrEYQvuEh30DyYot',
            'totalCount': 923,
            'primaryRecipeComponents': mock_formatted_primaryRecipeComponents,

        }, {
            'mealCode': 'lv2',
            'recipeId': 'RECIPE2DEF-OPS',
            'recipeName': 'Test Recipe Name 2',
            'mealContainer': 'ts32',
            'platePhotoUrl': 'https://cdn.filestackcontent.com/IQM3KcAkRye81xuN5JY4',
            'totalCount': 1228,
            'primaryRecipeComponents': mock_formatted_primaryRecipeComponents,

        }, {
            'mealCode': 'dv3',
            'recipeId': 'RECIPE3GHI-OPS',
            'recipeName': 'Test Recipe Name 3',
            'mealContainer': 'ts32',
            'platePhotoUrl': None,
            'totalCount': 549,
            'primaryRecipeComponents': mock_formatted_primaryRecipeComponents,

        }]
    }
    return formatted_ops_menu


class TestMealCodeFromMenuItemCategoryValues(TestCase):
    def test_get_meal_code_successful(self):
        expected_result = 'lv2'
        result = get_meal_code(mock_ops_menu('2022-03-28')['menuItems'][1]['categoryValues'])
        self.assertEqual(result, expected_result)

    def test_get_meal_code_empty(self):
        result = get_meal_code([])
        self.assertEqual(result, '')


class TestGetMenuTypeFromMenuCategoryValues(TestCase):
    def test_get_category_menu_type_successful(self):
        expected_result = 'production'
        result = get_category_menu_type(mock_ops_menu('2022-03-28')['categoryValues'])
        self.assertEqual(result, expected_result)

    def test_get_category_menu_type_empty(self):
        result = get_category_menu_type([])
        self.assertEqual(result, '')


class TestFormattedRecipeInstructions(TestCase):
    def test_format_recipe_instructions_successful(self):
        response = [{"text": "Please keep in mind the tamper seal from bottled containers can fall into the recipe you are making. Be sure to discard any tamper seals immediately after breaking the seal.",
                     "position": 0},
                    {"text": "In the blixer combine all of the ingredients and blend on intervals of 30 seconds until the texture is smooth and creamy.",
                     "position": 1},
                    {"text": "Pour into lexans.",
                     "position": 2}]
        expected = [{"id": 1,
                     "text": "Please keep in mind the tamper seal from bottled containers can fall into the recipe you are making. Be sure to discard any tamper seals immediately after breaking the seal."},
                    {"id": 2,
                     "text": "In the blixer combine all of the ingredients and blend on intervals of 30 seconds until the texture is smooth and creamy."},
                    {"id": 3,
                     "text": "Pour into lexans."}]
        result = format_recipe_instructions(response)
        self.assertEqual(result, expected)

    def test_format_recipe_instructions_empty(self):
        result = format_recipe_instructions([])
        self.assertEqual(result, [])

    def test_format_recipe_instructions_None(self):
        result = format_recipe_instructions(None)
        self.assertEqual(result, [])


class TestFormattedAllergenData(TestCase):
    def test_format_recipe_allergen_data_successful(self):
        mock_data = mock_recipeTreeComponents[0]['recipeItem']['subRecipe']
        mock_data['dietaryFlagsWithUsage'] = [{'dietaryFlag': {'id': DietaryFlagEnum.PEANUTS.value,
                                                               'name': 'peanuts'}},
                                              {'dietaryFlag': {'id': DietaryFlagEnum.SOY_BEANS.value,
                                                               'name': 'soy beans'}}]
        expected = ['peanuts', 'soy']
        result = format_allergens(mock_data['dietaryFlagsWithUsage'])
        self.assertEqual(result, expected)

    def test_format_ingredient_allergen_data_successful(self):
        mock_data = mock_recipeTreeComponents[0]['recipeItem']['subRecipe']['recipeTreeComponents'][3]['ingredient']['dietaryFlags']
        expected = ['sesame_seeds', 'tree_nuts']
        result = format_allergens(mock_data, is_recipe=False)
        self.assertEqual(result, expected)

    def test_format_allergen_data_empty(self):
        result1 = format_allergens([])
        result2 = format_allergens([], is_recipe=False)
        self.assertEqual(result1, [])
        self.assertEqual(result2, [])

    def test_format_allergen_data_None(self):
        result1 = format_allergens(None)
        result2 = format_allergens(None, is_recipe=False)
        self.assertEqual(result1, [])
        self.assertEqual(result2, [])


class TestGetFormattedBinWeightData(TestCase):
    def test_get_formatted_dynamic_bin_weight_data_successful(self):
        mock_response = mock_recipeTreeComponents[0]['recipeItem']['subRecipe']['recipeTreeComponents'][0]['recipeItem']['subRecipe']['categoryValues']
        expected = { 'value': 50, 'unit': 'lb' }
        result = format_bin_weight(mock_response)
        self.assertEqual(result, expected)

    def test_get_formatted_bin_weight_data_empty(self):
        mock_response = mock_recipeTreeComponents[0]['recipeItem']['subRecipe']['recipeTreeComponents'][1]['recipeItem']['subRecipe']['categoryValues']
        expected_default = { 'value': 60, 'unit': 'lb' }
        result = format_bin_weight(mock_response)
        self.assertEqual(result, expected_default)

    def test_get_formatted_bin_weight_data_None(self):
        expected_default = { 'value': 60, 'unit': 'lb' }
        result = format_bin_weight(None)
        self.assertEqual(result, expected_default)


class TestGetFormattedOpsMenuData(TestCase):
    def response(self, *menus):
        return ({
            'data': {
                'viewer': {
                    'menus': [m for m in menus if m]
                }
            }
        })

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_successful_for_one_valid_menu(self, mock_retrieval_method):
        mock_retrieval_method.return_value = self.response(mock_ops_menu('2022-03-28'))
        result = get_formatted_ops_menu_data(['2022-03-28'])
        self.assertEqual(result, [formatted_ops_menu('2022-03-28')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_successful_for_multiple_valid_menus(self, mock_retrieval_method):
        self.maxDiff = None
        mock_retrieval_method.return_value = self.response(mock_ops_menu('2022-03-28'), mock_ops_menu('2022-04-04'), mock_ops_menu('2022-04-18'))
        result = get_formatted_ops_menu_data(['2022-03-28', '2022-04-04', '2022-04-18'])
        self.assertEqual(result, [formatted_ops_menu('2022-03-28'), formatted_ops_menu('2022-04-04'), formatted_ops_menu('2022-04-18')])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_formatted_ops_menu_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_formatted_ops_menu_data([])
        self.assertEqual(result, None)

    @mock.patch('galley.formatted_ops_queries.get_raw_menu_data')
    def test_get_formatted_ops_menu_data_args_defaults(self, mock_gromd):
        dates = ['2022-03-28', '2022-04-04']
        get_formatted_ops_menu_data(dates)
        mock_gromd.assert_called_with(dates, 'Vacaville', 'production', is_ops=True)
        get_formatted_ops_menu_data(dates, 'Montana', 'staging')
        mock_gromd.assert_called_with(dates, 'Montana', 'staging', is_ops=True)
