import logging
from unittest import TestCase, mock
from galley.queries import (get_ops_menu_query,
                            get_ops_recipe_item_connection_query,
                            get_raw_recipe_items_data_via_connection)

logger = logging.getLogger(__name__)


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
            recipeTreeComponents(levels: [1]) {
            quantity
            unit {
            id
            name
            }
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
            categoryValues {
            id
            name
            category {
            id
            name
            itemType
            }
            }
            dietaryFlags {
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
            dietaryFlagsWithUsages {
            dietaryFlag {
            id
            name
            }
            }
            recipeTreeComponents(levels: [1]) {
            quantity
            unit {
            id
            name
            }
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
            categoryValues {
            id
            name
            category {
            id
            name
            itemType
            }
            }
            dietaryFlags {
            id
            name
            }
            }
            recipeItem {
            subRecipe {
            id
            name
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
            recipeInstructions {
            text
            position
            }
            dietaryFlagsWithUsages {
            dietaryFlag {
            id
            name
            }
            }
            recipeTreeComponents(levels: [1]) {
            quantity
            unit {
            id
            name
            }
            ingredient {
            id
            name
            externalName
            dietaryFlags {
            id
            name
            }
            }
            recipeItem {
            subRecipe {
            id
            name
            externalName
            dietaryFlagsWithUsages {
            dietaryFlag {
            id
            name
            }
            }
            }
            }
            }
            }
            }
            }
            }
            }
            }
            }
            volume
            unit {
            id
            name
            }
            }
            }
            }
            }'''.replace(' '*12, '')

    def test_get_ops_menu_query(self):
        query = get_ops_menu_query(dates=["2022-03-28"])
        query_str = bytes(query).decode('utf-8')
        self.maxDiff = None
        self.assertEqual(query_str, self.expected_query)


class TestOpsRecipeItemConnectionQuery(TestCase):
    def setUp(self) -> None:
        self.data = {
            'WRONGID==': None,
            'cmVjaXBlOjE3NjQxNA==': {'edges': [{'node': {'id': 'cmVjaXBlSXRlbToxMTUwNDY5', 'recipeId': 'cmVjaXBlOjE3NjQyMw==', 'preparations': [{'id': 'cHJlcGFyYXRpb246MzEzNjk=', 'name': 'Core Recipe'}]}}, {'node': {'id': 'cmVjaXBlSXRlbToxMTUwNDE3', 'recipeId': 'cmVjaXBlOjE3NjQxMw==', 'preparations': [{'id': 'cHJlcGFyYXRpb246MzEzNjk=', 'name': 'Core Recipe'}]}}]},
            'cmVjaXBlOjIwMjI5NA==': {'edges': [{'node': {'id': 'cmVjaXBlSXRlbToxMjkwMjAw', 'recipeId': 'cmVjaXBlOjIwMjMwNQ==', 'preparations': []}}, {'node': {'id': 'cmVjaXBlSXRlbToxMjkwMTgx', 'recipeId': 'cmVjaXBlOjIwMjMwMA==', 'preparations': []}}]},
        }

        self.expected_query = '''query {
            viewer {
            recipeItemConnection(filters: {subRecipeIds: ["cmVjaXBlOjIwMjI5NA=="]}) {
            edges {
            node {
            id
            recipeId
            preparations {
            id
            name
            }
            }
            }
            }
            }
            }'''.replace(' '*12, '')

    def response(self, *data):
        return ({
            'data': {
                'viewer': {
                    'recipeItemConnection': data
                }
            }
        })

    def test_get_ops_recipe_item_connection_query(self):
        query = get_ops_recipe_item_connection_query(sub_recipe_ids=["cmVjaXBlOjIwMjI5NA=="])
        query_str = bytes(query).decode('utf-8')
        self.maxDiff = None
        self.assertEqual(query_str, self.expected_query)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipe_items_data_via_connection_successful(self, mock_retrieval_method):
        mock_retrieval_method.side_effect = [
            self.response(self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['cmVjaXBlOjE3NjQxNA=='], self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['WRONGID=='], self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['WRONGID==']),
        ]

        self.maxDiff = None

        # one valid menu name
        result1 = get_raw_recipe_items_data_via_connection(["cmVjaXBlOjIwMjI5NA=="])
        self.assertEqual(result1, (self.data["cmVjaXBlOjIwMjI5NA=="],))

        # multiple valid menu names
        result2 = get_raw_recipe_items_data_via_connection(['cmVjaXBlOjIwMjI5NA==', 'cmVjaXBlOjE3NjQxNA=='])
        self.assertEqual(result2, (self.data['cmVjaXBlOjE3NjQxNA=='],
                                   self.data['cmVjaXBlOjIwMjI5NA==']))

        # one valid menu name and one invalid menu name
        result3 = get_raw_recipe_items_data_via_connection(['WRONGID==', 'cmVjaXBlOjE3NjQxNA=='])
        self.assertEqual(result3, (None, self.data['cmVjaXBlOjIwMjI5NA=='],))

        # one invalid menu name
        result4 = get_raw_recipe_items_data_via_connection(['WRONGID=='])
        self.assertEqual(result4, (None,))
