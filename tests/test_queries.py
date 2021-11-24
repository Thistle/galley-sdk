import logging
from unittest import TestCase, mock

from galley.queries import (Query, get_menu_query, get_raw_menu_data,
                            get_raw_recipes_data, get_recipe_data,
                            recipes_data_query)
from sgqlc.operation import Operation

from tests.mock_responses import mock_recipes_data
from tests.mock_responses.mock_menu_data import mock_menu

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
            menus(where: {date: ["2021-10-04", "2021-10-07"]}) {
            id
            name
            date
            location {
            name
            }
            categoryValues {
            id
            name
            category {
            id
            name
            itemType
            }
            }
            menuItems {
            recipeId
            categoryValues {
            id
            name
            category {
            id
            name
            itemType
            }
            }
            recipe {
            externalName
            recipeItems {
            subRecipeId
            preparations {
            id
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
        query = get_menu_query(["2021-10-04", "2021-10-07"])
        query_str = query.__to_graphql__(auto_select_depth=3)
        self.assertEqual(query_str.replace(' ', ''),
                         self.expected_query.replace(' ', ''))

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_successful(self, mock_retrieval_method):
        mock_retrieval_method.side_effect = [
            self.response(mock_menu('2021-11-14')),
            self.response(mock_menu('2021-11-21'), mock_menu('2021-11-21'),
                          mock_menu('2021-11-28')),
            self.response(mock_menu('2021-11-28'), mock_menu('2021-12-05')),
            self.response(mock_menu('2021-12-05')),
        ]

        # one valid menu name
        result1 = get_raw_menu_data(['2021-11-14'], "Vacaville", "production")
        self.assertEqual(result1, [mock_menu('2021-11-14')])

        # multiple valid menu names
        result2 = get_raw_menu_data(['2021-11-21', '2021-11-21', '2021-11-28'],
                                    "Vacaville", "production")
        self.assertEqual(result2, [mock_menu('2021-11-21'),
                                   mock_menu('2021-11-21'),
                                   mock_menu('2021-11-28')])

        # one valid menu name and one invalid menu name
        result3 = get_raw_menu_data(['2021-11-28', '2021-12-05'],
                                    "Vacaville", "production")
        self.assertEqual(result3, [mock_menu('2021-11-28')])

        # one invalid menu name
        result4 = get_raw_menu_data(['2021-12-05'], "Vacaville", "production")
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
        with self.assertRaises(ValueError):
            get_raw_menu_data(['YYYY-MM-DD'], "Vacaville", "production")

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_null(self, mock_retrieval_method):
        mock_retrieval_method.return_value = None
        result = get_raw_menu_data([], 'Vacaville', 'production')
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_filters_by_location(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'menus': [
                        mock_menu('2021-10-04', 'Vacaville'),
                        mock_menu('2021-10-04', 'Long Beach'),
                    ]
                }
            }
        }
        result = get_raw_menu_data(['2021-10-04'], 'Vacaville', 'production')
        self.assertEqual(result, [mock_menu('2021-10-04',
                                            location_name='Vacaville')])
        self.assertEqual(len(result), 1)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_menu_data_filter_by_menu_type(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'menus': [
                        mock_menu('2021-10-04', menu_type='production'),
                        mock_menu('2021-10-04', menu_type='development'),
                    ]
                }
            }
        }
        result = get_raw_menu_data(['2021-10-04'], 'Vacaville', 'production')
        self.assertEqual(len(result), 1)
        self.assertEqual(result,
                         [mock_menu('2021-10-04', menu_type='production')])


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
            id
            name
            category {
            id
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
            categoryValues {
            id
            name
            }
            }
            subRecipe {
            allIngredients
            }
            preparations {
            id
            name
            }
            }
            recipeTreeComponents(levels: [1]) {
            quantityUnitValues {
            unit {
            name
            }
            value
            }
            recipeItem {
            preparations {
            id
            name
            }
            ingredient {
            categoryValues {
            id
            name
            }
            externalName
            }
            }
            }
            }
            }
            }'''.replace(' '*12, '')

    def test_recipes_data_query(self):
        query = recipes_data_query(["cmVjaXBlOjE2NzEwOQ==", "cmVjaXBlOjE2OTEyMg==", "cmVjaXBlOjE2NTY5MA=="])
        query_str = bytes(query).decode('utf-8')
        self.assertEqual(query_str, self.expected_query)


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
