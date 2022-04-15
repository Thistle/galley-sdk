import logging
from unittest import TestCase, mock

from galley.queries import (
    Query, get_menu_query, get_raw_menu_data,
    get_raw_recipes_data, recipe_connection_query,
    get_ops_menu_query
)
from sgqlc.operation import Operation

from tests.mock_responses import mock_recipes_data
from tests.mock_responses.mock_menu_data import mock_menu
from pprint import pprint

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
        query_operation.viewer().recipes().__fields__(
            'id', 'externalName', 'instructions', 'notes', 'description')
        query_str = bytes(query_operation).decode('utf-8')
        self.assertEqual(query_str, self.expected_query)

    def test_recipe_query_failure(self):
        query_operation = Operation(Query)
        query_str = bytes(query_operation).decode('utf-8')
        self.assertNotEqual(query_str, self.expected_query)


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
            id
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
            name
            recipeItems {
            subRecipeId
            preparations {
            id
            name
            }
            }
            categoryValues{
            id
            name
            category{
            id
            name
            itemType
            }
            }
            media{
            altText
            caption
            sourceUrl
            }
            isDish
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


class TestRecipeConnectionQuery(TestCase):
    def setUp(self) -> None:
        self.expected_query = '''query {
            viewer {
            recipeConnection(filters: {id: ["cmVjaXBlOjE2NzEwOQ==", "cmVjaXBlOjE2OTEyMg==", "cmVjaXBlOjE2NTY5MA=="]}, paginationOptions: {first: 2, startIndex: 0}) {
            edges {
            node {
            id
            externalName
            name
            notes
            description
            media {
            altText
            caption
            sourceUrl
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
            category {
            id
            name
            itemType
            }
            }
            }
            subRecipe {
            id
            allIngredients
            name
            externalName
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
            nutritionalsQuantity
            nutritionalsUnit {
            id
            name
            }
            recipeInstructions {
            text
            position
            }
            recipeTreeComponents {
            id
            }
            }
            preparations {
            id
            name
            }
            }
            recipeTreeComponents(levels: [1]) {
            id
            quantityUnitValues {
            unit {
            id
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
            category {
            id
            name
            itemType
            }
            }
            externalName
            }
            subRecipe {
            id
            allIngredients
            externalName
            name
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
            nutritionalsQuantity
            nutritionalsUnit {
            id
            name
            }
            }
            subRecipeId
            quantity
            unit {
            id
            name
            }
            }
            }
            dietaryFlagsWithUsages {
            dietaryFlag {
            id
            }
            }
            }
            }
            pageInfo {
            endIndex
            hasNextPage
            hasPreviousPage
            startIndex
            }
            }
            }
            }'''.replace(' '*12, '')

    def test_recipe_connection_query(self):
        query = recipe_connection_query(
            recipe_ids=["cmVjaXBlOjE2NzEwOQ==", "cmVjaXBlOjE2OTEyMg==", "cmVjaXBlOjE2NTY5MA=="],
            page_size=2,
            start_index=0
        )
        query_str = bytes(query).decode('utf-8')
        self.maxDiff = None
        self.assertEqual(query_str, self.expected_query)


class TestQueryGetRawRecipesData(TestCase):
    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_data_successful(self, mock_retrieval_method):
        recipe_connection_data = mock_recipes_data.mock_recipe_connection(['1'])
        expected_recipe_data = [mock_recipes_data.mock_recipe('1')]
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': recipe_connection_data
                }
            }
        }
        result = get_raw_recipes_data(['1'])
        self.assertEqual(result, expected_recipe_data)


    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_edges_empty(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': []
                    },
                    'pageInfo': mock_recipes_data.mock_page_info()
                }
            }
        }
        result = get_raw_recipes_data(['Fake'])
        self.assertEqual(result, [])

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_node_empty(self, mock_retrieval_method):
        mock_retrieval_method.return_value = {
            'data': {
                'viewer': {
                    'recipeConnection': {
                        'edges': [{
                            'node': {}
                        }]
                    },
                    'pageInfo': mock_recipes_data.mock_page_info()
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
                    'recipeConnection': None
                }
            }
        }
        result = get_raw_recipes_data(['Fake'])
        self.assertEqual(result, None)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipes_multiple_pages(self, mock_retrieval_method):
        # Mocking 2 pages with with a 2 recipe limit
        page_1 = mock_recipes_data.mock_recipe_connection(
            ['1', '2'],
            has_previous_page=False,
            has_next_page=True,
            start_index=0,
            end_index=2
        )
        page_2 = mock_recipes_data.mock_recipe_connection(
            ['3'],
            has_previous_page=True,
            has_next_page=False,
            start_index=2,
            end_index=3
        )
        expected_recipe_data = list(map(mock_recipes_data.mock_recipe, ['1', '2', '3']))
        mock_retrieval_method.side_effect = [
            {
                'data': {
                    'viewer': {
                        'recipeConnection': page_1
                    }
                }
            },
            {
                'data': {
                    'viewer': {
                        'recipeConnection': page_2
                    }
                }
            }
        ]
        result = get_raw_recipes_data(['1', '2', '3'])
        self.assertEqual(mock_retrieval_method.call_count, 2)
        self.assertEqual(result, expected_recipe_data)


class TestOpsMenuDataQuery(TestCase):
    def setUp(self) -> None:
        self.expected_query = '''query {
            viewer {
            menus(where: {date: ["2022-03-28"]}) {
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
            id
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
            files {
            photos {
            sourceUrl
            caption
            }
            }
            id
            name
            categoryValues {
            id
            name
            category {
            id
            name
            itemType
            }
            }
            recipeInstructions {
            text
            position
            }
            recipeTreeComponents(levels: [1]) {
            quantityUnitValues {
            value
            unit {
            id
            name
            }
            }
            recipeItem {
            preparations {
            id
            name
            }
            subRecipe {
            id
            name
            externalName
            recipeTreeComponents(levels: [1]) {
            quantityUnitValues {
            value
            unit {
            id
            name
            }
            }
            ingredient {
            id
            name
            externalName
            }
            recipeItem {
            preparations {
            id
            name
            }
            subRecipe {
            id
            name
            externalName
            recipeInstructions {
            text
            position
            }
            }
            }
            }
            }
            }
            }
            }
            volume
            }
            }
            }
            }'''.replace(' '*12, '')
            
    def test_get_ops_menu_query(self):
        query = get_ops_menu_query(dates=["2022-03-28"])
        query_str = bytes(query).decode('utf-8')
        self.maxDiff = None
        self.assertEqual(query_str, self.expected_query)
