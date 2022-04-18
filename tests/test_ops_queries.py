import logging
from unittest import TestCase
from galley.queries import get_ops_menu_query


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