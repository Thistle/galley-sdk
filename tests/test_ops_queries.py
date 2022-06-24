import logging
from unittest import TestCase, mock
from galley.queries import (get_ops_menu_query,
                            get_ops_recipe_items_query,
                            get_raw_recipe_items_data)

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


class TestOpsRecipeDataQuery(TestCase):
    def setUp(self) -> None:
        self.data = {
            'WRONGID==': None,
            'cmVjaXBlOjE3NjQxNA==': {
                'id': 'cmVjaXBlOjE3NjQxNA==', 'parentRecipeItems': [{'recipe': {'recipeItems': [{'id': 'cmVjaXBlSXRlbToxMTUwNDE3', 'subRecipe': {'id': 'cmVjaXBlOjE3NjQxNA=='}, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMTUwNDIx', 'subRecipe': {'id': 'cmVjaXBlOjE3NjQxNQ=='}, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMzkzNjU5', 'subRecipe': {'id': 'cmVjaXBlOjIyMjEyMA=='}, 'preparations': [{'id': 'cHJlcGFyYXRpb246MjgzMzQ=', 'name': 'standalone'}, {'id': 'cHJlcGFyYXRpb246MzEwMjI=', 'name': '2 oz WINPAK'}]}, {'id': 'cmVjaXBlSXRlbToxMTUwNDIw', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMjQ5MTk5', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxNDQ1ODI3', 'subRecipe': None, 'preparations': []}]}}, {'recipe': {'recipeItems': [{'id': 'cmVjaXBlSXRlbToxMTUwNDY5', 'subRecipe': {'id': 'cmVjaXBlOjE3NjQxNA=='}, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMTUwNDcw', 'subRecipe': {'id': 'cmVjaXBlOjE3NDgyMA=='}, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMzkzNjU3', 'subRecipe': {'id': 'cmVjaXBlOjIyMjEyMA=='}, 'preparations': [{'id': 'cHJlcGFyYXRpb246MjgzMzQ=', 'name': 'standalone'}, {'id': 'cHJlcGFyYXRpb246MzEwMjI=', 'name': '2 oz WINPAK'}]}, {'id': 'cmVjaXBlSXRlbToxMTUwNDY3', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMjUyNTEy', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxNDQ1ODI2', 'subRecipe': None, 'preparations': []}]}}]},
            'cmVjaXBlOjIwMjI5NA==': {
                'id': 'cmVjaXBlOjIwMjI5NA==', 'parentRecipeItems': [{'recipe': {'recipeItems': [{'id': 'cmVjaXBlSXRlbToxMjkwMTgx', 'subRecipe': {'id': 'cmVjaXBlOjIwMjI5NA=='}, 'preparations': [{'id': 'cHJlcGFyYXRpb246MzEzNjk=', 'name': 'Core Recipe'}]}, {'id': 'cmVjaXBlSXRlbToxMjkwMTgy', 'subRecipe': {'id': 'cmVjaXBlOjE4NTQ1OQ=='}, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMzkzNjg3', 'subRecipe': {'id': 'cmVjaXBlOjIyMTEyOA=='}, 'preparations': [{'id': 'cHJlcGFyYXRpb246MjgzMzQ=', 'name': 'standalone'}, {'id': 'cHJlcGFyYXRpb246MzEwMjI=', 'name': '2 oz WINPAK'}]}, {'id': 'cmVjaXBlSXRlbToxMjkwMTg0', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMjkwMTg3', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxNDQ1ODI0', 'subRecipe': None, 'preparations': []}]}}, {'recipe': {'recipeItems': [{'id': 'cmVjaXBlSXRlbToxMjkwMjAw', 'subRecipe': {'id': 'cmVjaXBlOjIwMjI5NA=='}, 'preparations': [{'id': 'cHJlcGFyYXRpb246MzEzNjk=', 'name': 'Core Recipe'}]}, {'id': 'cmVjaXBlSXRlbToxMjkwMjEy', 'subRecipe': {'id': 'cmVjaXBlOjE3NDg1Ng=='}, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMzkzNjg1', 'subRecipe': {'id': 'cmVjaXBlOjIyMTEyOA=='}, 'preparations': [{'id': 'cHJlcGFyYXRpb246MjgzMzQ=', 'name': 'standalone'}, {'id': 'cHJlcGFyYXRpb246MzEwMjI=', 'name': '2 oz WINPAK'}]}, {'id': 'cmVjaXBlSXRlbToxMjkwMjE0', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxMjkwMjAz', 'subRecipe': None, 'preparations': []}, {'id': 'cmVjaXBlSXRlbToxNDQ1ODAy', 'subRecipe': None, 'preparations': []}]}}]}
        }
        self.expected_query = '''query {
            viewer {
            recipes(where: {id: ["cmVjaXBlOjIwMjI5NA=="]}) {
            id
            parentRecipeItems {
            recipe {
            recipeItems {
            id
            subRecipe {
            id
            }
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

    def response(self, *data):
        return ({
            'data': {
                'viewer': {
                    'recipes': [d for d in data if d]
                }
            }
        })

    def test_get_ops_recipe_items_query(self):
        query = get_ops_recipe_items_query(recipe_ids=["cmVjaXBlOjIwMjI5NA=="])
        query_str = bytes(query).decode('utf-8')
        self.maxDiff = None
        self.assertEqual(query_str, self.expected_query)

    @mock.patch('galley.queries.make_request_to_galley')
    def test_get_raw_recipe_items_data_successful(self, mock_retrieval_method):
        mock_retrieval_method.side_effect = [
            self.response(self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['cmVjaXBlOjE3NjQxNA=='], self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['WRONGID=='], self.data['cmVjaXBlOjIwMjI5NA==']),
            self.response(self.data['WRONGID==']),
        ]

        self.maxDiff = None

        # one valid menu name
        result1 = get_raw_recipe_items_data(["cmVjaXBlOjIwMjI5NA=="])
        self.assertEqual(result1, [self.data["cmVjaXBlOjIwMjI5NA=="]])

        # multiple valid menu names
        result2 = get_raw_recipe_items_data(['cmVjaXBlOjIwMjI5NA==', 'cmVjaXBlOjE3NjQxNA=='])
        self.assertEqual(result2, [self.data['cmVjaXBlOjE3NjQxNA=='],
                                   self.data['cmVjaXBlOjIwMjI5NA==']])

        # one valid menu name and one invalid menu name
        result3 = get_raw_recipe_items_data(['WRONGID==', 'cmVjaXBlOjE3NjQxNA=='])
        self.assertEqual(result3, [self.data['cmVjaXBlOjIwMjI5NA==']])

        # one invalid menu name
        result4 = get_raw_recipe_items_data(['WRONGID=='])
        self.assertEqual(result4, [])
