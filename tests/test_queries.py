from unittest import mock, TestCase
from sgqlc.operation import Operation

from galley.queries import Query, get_raw_recipes_data, get_recipe_data, \
    get_raw_menu_data, recipes_data_query, get_menu_data_for_dates, MenuCategoryEnum
from tests.mock_responses.mock_menu_data import mock_menu
from galley.types import MenuFilterInput

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
                'externalName': 'test recipe 2',
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


class TestQueryWeekMenuData(TestCase):
    def setUp(self) -> None:
        self.expected_query = '''query {
            viewer {
            menus(where: {name: ["2021-10-04 1_2_3", "2021-10-04 4_5_6"]}) {
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
            recipe {
            externalName
            recipeItems {
            subRecipeId
            preparations {
            name
            }
            }
            }
            }
            }
            }
            }'''.replace(' '*12, '')

    def response(self, *menus):
        return ({
            'data': {
                'viewer': {
                    'menus': [m for m in menus if m]
                }
            }
        })

    def test_week_menu_data_query(self):
        query = menu_data_query(["2021-10-04 1_2_3", "2021-10-04 4_5_6"])
        query_str = query.__to_graphql__(auto_select_depth=3)
        self.assertEqual(query_str.replace(' ', ''), self.expected_query.replace(' ', ''))

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_successful(self, mock_retrieval_method):
        mock_retrieval_method.side_effect = [
            self.response(mock_menu('21-11-14 123')),
            self.response(mock_menu('21-11-21 123'), mock_menu('21-11-21 456'), mock_menu('21-11-28 123')),
            self.response(mock_menu('21-11-28 456'), mock_menu('21-12-05 123')),
            self.response(mock_menu('21-12-05 456')),
        ]

        # one valid menu name
        result1 = get_raw_menu_data(['21-11-14 123'])
        self.assertEqual(result1, [mock_menu('21-11-14 123')])

        # multiple valid menu names
        result2 = get_raw_menu_data(['21-11-21 123', '21-11-21 456', '21-11-28 123'])
        self.assertEqual(result2, [mock_menu('21-11-21 123'), mock_menu('21-11-21 456'), mock_menu('21-11-28 123')])

        # one valid menu name and one invalid menu name
        result3 = get_raw_menu_data(['21-11-28 456', '21-12-05 123'])
        self.assertEqual(result3, [mock_menu('21-11-28 456')])

        # one invalid menu name
        result4 = get_raw_menu_data(['21-12-05 456'])
        self.assertEqual(result4, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_validation_failure(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'test': 'test'
                }
            }
        }
        result = get_raw_menu_data('YYYY-MM-DD 1_2_3')
        self.assertEqual(result, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_raw_menu_data([])
        self.assertEqual(result, None)


class TestRecipesDataQuery(TestCase):
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
            recipeItems {
            ingredient {
            externalName
            }
            subRecipe {
            allIngredients
            }
            subRecipeId
            preparations {
            name
            }
            }
            }
            recipe {
            recipeItems {
            ingredient {
            externalName
            categoryValues {
            name
            }
            }
            subRecipe {
            allIngredients
            }
            preparations {
            name
            }
            }
            }
            }
            }'''.replace(' '*12, '')

    def test_recipes_data_query(self):
        query = recipes_data_query(["cmVjaXBlOjE2NzEwOQ==", "cmVjaXBlOjE2OTEyMg==", "cmVjaXBlOjE2NTY5MA=="])
        query_str = bytes(query).decode('utf-8')
        self.assertEqual(query_str, self.expected_query)

    def test_week_menu_data_query(self):
        query_operation = Operation(Query)
        query_operation.viewer().menus(where=MenuFilterInput(date=["2021-10-04"])).__fields__(
            'id', 'name', 'date', 'location', 'categoryValues', 'menuItems'
        )
        query_operation.viewer.menus.menuItems.__fields__('recipeId', 'categoryValues', 'recipe')
        query_operation.viewer.menus.menuItems.recipe.__fields__('externalName', 'recipeItems')
        query_operation.viewer.menus.menuItems.recipe.recipeItems.__fields__('subRecipeId', 'preparations')
        query_operation.viewer.menus.menuItems.recipe.recipeItems.preparations.__fields__('name')
        query_str = query_operation.__to_graphql__(auto_select_depth=3)
        self.assertEqual(query_str.replace(' ', ''), self.expected_query.replace(' ', ''))

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_menu_data_for_dates_successful(self, mock_retrieval_method):
        def menus(date):
            return ({
                'name': f"{date} 1_2_3",
                'id': 'MENU123ABC',
                'date': f"{date}",
                'location': {
                    'name': 'Vacaville'
                },
                'categoryValues': [
                    {
                        'id': '1',
                        'name': 'production',
                        'category': {
                            'id': MenuCategoryEnum.MENU_TYPE.value,
                            'name': 'menu type',
                            'itemType': 'menu'
                        }
                    },
                ],
                'menuItems': [
                    {
                        'recipeId': 'RECIPE1ABC',
                        'categoryValues': [{
                            'name': 'dv1',
                            'category': {
                                'itemType': 'menuItem',
                                'name': 'menu item type'
                            }
                        }],
                        'recipe': {
                            'externalName': 'Test Recipe Name 1',
                            'recipeItems': [{
                                'preparations': [
                                    {'name':  'standalone'}
                                ],
                                'subRecipeId': 'SUBRECIPEID456'
                            }]
                        },
                    },
                    {
                        'recipeId': 'RECIPE2DEF',
                        'categoryValues': [{
                            'name': 'dv2',
                            'category': {
                                'itemType': 'menuItem',
                                'name': 'menu item type'
                            }
                        }],
                        'recipe': {
                            'externalName': 'Test Recipe Name 2',
                            'recipeItems': [{
                                'preparations': [
                                    {'name':  'standalone'}
                                ],
                                'subRecipeId': 'SUBRECIPEID789'
                            }]
                        },
                    },
                ]
            }) if date != '2021-12-05' else []

        def response(*menus):
            return ({
                'data': {
                    'viewer': {
                        'menus': [m for m in menus if m]
                    }
                }
            })

        mock_retrieval_method.side_effect = [
            response(menus('2021-11-14')),
            response(menus('2021-11-21'), menus('2021-11-21'),
                     menus('2021-11-28')),
            response(menus('2021-11-28'), menus('2021-12-05')),
            response(menus('2021-12-05')),
        ]

        # one valid menu name
        result1 = get_menu_data_for_dates(['2021-11-14'])
        self.assertEqual(result1, [menus('2021-11-14')])

        # multiple valid menu names
        result2 = get_menu_data_for_dates(['2021-11-21', '2021-11-21',
                                      '2021-11-28'])
        self.assertEqual(result2, [menus('2021-11-21'), menus('2021-11-21'),
                                   menus('2021-11-28')])

        # one valid menu name and one invalid menu name
        result3 = get_menu_data_for_dates(['2021-11-28', '2021-12-05'])
        self.assertEqual(result3, [menus('2021-11-28')])

        # one invalid menu name
        result4 = get_menu_data_for_dates(['2021-12-05'])
        self.assertEqual(result4, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_menu_data_for_dates_validation_failure(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'test': 'test'
                }
            }
        }

        with self.assertRaises(ValueError):
            get_menu_data_for_dates(['YYYY-MM-DD'])

class TestQueryGetRawRecipesData(TestCase):
    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_data_successful(self, mock_retrieval_method):
        recipe_data = mock_recipes_data.mock_recipe('1')

        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipes': recipe_data
                }
            }
        }
        result = get_raw_recipes_data(['1'])
        self.assertEqual(result, recipe_data)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_data_empty(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipes': []
                }
            }
        }
        result = get_raw_recipes_data(['Fake'])
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_data_missing(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipes': None
                }
            }
        }
        result = get_raw_recipes_data(['Fake'])
        self.assertEqual(result, None)
