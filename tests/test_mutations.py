import logging
from galley.mutations import (
    upsert_menu_data,
    build_upsert_mutation_query,
    bulk_update_recipe_item_data,
    build_bulk_update_recipe_item_query
)
from unittest import mock, TestCase


logger = logging.getLogger(__name__)


class TestUpsertMenuData(TestCase):
    def setUp(self) -> None:
        self.response_data = {
            "data": {
                "bulkUpsertMenus": {
                "menus": [
                    {
                    "id": "bWVudTo5ODIzOTI=",
                    "name": "2022-01-10 1_2_3",
                    "date": "2022-01-10"
                    }
                ]
                }
            }
        }

    def test_single_menu_item_mutation(self):
        expected_str = '''mutation {
            bulkUpsertMenus(input: {menus: [{id: "bWVudTo5ODIzOTI=", menuItems: [{id: "bWVudUl0ZW06MzM4MTQyMjQ=", volume: 20.0, unit: {name: "each"}}]}]}) {
            menus {
            id
            name
            date
            }
            }
            }'''.replace(' '*12, '')
        payload = [{
            "menu_id": "bWVudTo5ODIzOTI=",
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20,
                    "unit_name": "each"
                }
            ]
        }]
        ret = build_upsert_mutation_query(payload)
        mutation_str = bytes(ret).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    def test_multi_menu_item_mutation_in_same_menu(self):
        expected_str = '''mutation {
            bulkUpsertMenus(input: {menus: [{id: "bWVudTo5ODIzOTI=", menuItems: [{id: "bWVudUl0ZW06MzM4MTQyMjQ=", volume: 20.0, unit: {name: "each"}}, {id: "hashievalues", volume: 2527.0, unit: {name: "each"}}]}]}) {
            menus {
            id
            name
            date
            }
            }
            }'''.replace(' '*12, '')
        payload = [{
            "menu_id": "bWVudTo5ODIzOTI=",
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20,
                    "unit_name": "each"
                },
                {
                    "id": "hashievalues",
                    "volume": 2527,
                    "unit_name": "each"
                }
            ]
        }]
        ret = build_upsert_mutation_query(payload)
        mutation_str = bytes(ret).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    def test_multi_menu_mutation(self):
        expected_str = '''mutation {
            bulkUpsertMenus(input: {menus: [{id: "bWVudTo5ODIzOTI=", menuItems: [{id: "bWVudUl0ZW06MzM4MTQyMjQ=", volume: 20.0, unit: {name: "each"}}]}, {id: "anothermenuid", menuItems: [{id: "lkkjahcjhey23231", volume: 42.0, unit: {name: "each"}}]}]}) {
            menus {
            id
            name
            date
            }
            }
            }'''.replace(' '*12, '')
        payload = [{
            "menu_id": "bWVudTo5ODIzOTI=",
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20,
                    "unit_name": "each"
                }
            ]
        },
        {
            "menu_id": "anothermenuid",
            "menu_items": [
                {
                    "id": "lkkjahcjhey23231",
                    "volume": 42,
                    "unit_name": "each"
                }
            ]
        }]
        ret = build_upsert_mutation_query(payload)
        mutation_str = bytes(ret).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    def test_unit_name_defaults_to_each_if_not_given(self):
        expected_str = '''mutation {
            bulkUpsertMenus(input: {menus: [{id: "bWVudTo5ODIzOTI=", menuItems: [{id: "bWVudUl0ZW06MzM4MTQyMjQ=", volume: 20.0, unit: {name: "each"}}]}]}) {
            menus {
            id
            name
            date
            }
            }
            }'''.replace(' '*12, '')
        payload = [{
            "menu_id": "bWVudTo5ODIzOTI=",
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20
                }
            ]
        }]
        ret = build_upsert_mutation_query(payload)
        mutation_str = bytes(ret).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    def test_unit_name_protects_from_typos(self):
        expected_str = '''mutation {
            bulkUpsertMenus(input: {menus: [{id: "bWVudTo5ODIzOTI=", menuItems: [{id: "bWVudUl0ZW06MzM4MTQyMjQ=", volume: 20.0, unit: {name: "each"}}]}]}) {
            menus {
            id
            name
            date
            }
            }
            }'''.replace(' '*12, '')
        payload = [{
            "menu_id": "bWVudTo5ODIzOTI=",
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20,
                    "unit_name": "echa"
                }
            ]
        }]
        ret = build_upsert_mutation_query(payload)
        mutation_str = bytes(ret).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_upsert_menu_data_returns_expected_response_data(self, mock_mr):
        mock_mr.return_value = self.response_data
        payload = [{
            "menu_id": "bWVudTo5ODIzOTI=",
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20,
                    "unit_name": "each"
                }
            ]
        }]
        result = upsert_menu_data(payload)
        self.assertEqual(result, self.response_data['data'])

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_upsert_menu_data_raises_exception_if_thrown_from_request(self, mock_mr):
        mock_mr.return_value = {
            "errors": [
                { "message": "Unexpected error value: { message: ... }" }
            ],
            "data": 'null'
        }

        payload = [{
            "menu_id": "bWVudTo5ODIzOTI=",
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20,
                    "unit_name": "each"
                }
            ]
        }]
        with self.assertRaises(ValueError):
            upsert_menu_data(payload)

    def test_exception_raised_if_no_menu_id_present(self):
        payload = [{
            "menu_items": [
                {
                    "id": "bWVudUl0ZW06MzM4MTQyMjQ=",
                    "volume": 20,
                    "unit_name": "each"
                }
            ]
        }]
        with self.assertRaises(ValueError):
            upsert_menu_data(payload)


class TestUpdateRecipeItemData(TestCase):
    def setUp(self) -> None:
        self.response_data = {
            "data": {
                "bulkUpdateRecipeItems": {
                    "recipeItems": [
                        {
                            "id": "cmVjaXBlSXRlbToxMTY0NTQ3",
                            "subRecipeId": "cmVjaXBlOjE3OTk5Ng==",
                            "quantity": 1
                        },
                        {
                            "id": "cmVjaXBlSXRlbToxMjkyNDEy",
                            "subRecipeId": "cmVjaXBlOjE3OTk5Ng==",
                            "quantity": 1
                        }
                    ]
                }
            },
            'noRepeats': {'bulkUpdateRecipeItems': {'recipeItems': []}},
        }

    def test_single_recipe_item_mutation(self):
        expected_str = '''mutation {
            bulkUpdateRecipeItems(input: {ids: ["cmVjaXBlOjIwMjI5NA=="], attrs: {preparationIds: ["cHJlcGFyYXRpb246MzEzNjk="]}}) {
            recipeItems {
            id
            recipeId
            subRecipeId
            quantity
            }
            }
            }'''.replace(' '*12, '')

        payload = {
            "ids": ["cmVjaXBlOjIwMjI5NA=="],
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        ret = build_bulk_update_recipe_item_query(payload)
        mutation_str = bytes(ret).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    def test_multi_recipe_item_mutation(self):
        ids = ["cmVjaXBlOjIwMjI5NA==", "cmVjaXBlOjE3NjQxNA=="]
        expected_str = '''mutation {
            bulkUpdateRecipeItems(input: {ids: ["cmVjaXBlOjIwMjI5NA==", "cmVjaXBlOjE3NjQxNA=="], attrs: {preparationIds: ["cHJlcGFyYXRpb246MzEzNjk="]}}) {
            recipeItems {
            id
            recipeId
            subRecipeId
            quantity
            }
            }
            }'''.replace(' '*12, '')
        payload = {
            "ids": ids,
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        ret = build_bulk_update_recipe_item_query(payload)
        mutation_str = bytes(ret).decode('utf-8')

        key_len = len('"cmVjaXBlOjIwMjI5NA=="')
        start_len = len('mutation {bulkUpdateRecipeItems(input: {ids: ["')
        stop_len = start_len + key_len
        next_start_len = stop_len + 2
        next_stop_len = next_start_len + key_len
        mutation_keys = []
        mutation_keys.append(mutation_str[start_len:stop_len].replace('"', ''))
        mutation_keys.append(mutation_str[next_start_len:next_stop_len].replace('"', ''))
        for idx in ids:
            mutation_str = mutation_str.replace(idx, "KEY")
            expected_str = expected_str.replace(idx, "KEY")
        self.assertEqual(" ".join(sorted(mutation_keys)), " ".join(sorted(ids)))
        self.assertEqual(mutation_str, expected_str)

    def test_validated_id_if_non_string_recipe_item_ids_provided(self):
        expected_str = '''mutation {
            bulkUpdateRecipeItems(input: {ids: ["cmVjaXBlOjIwMjI5NA=="], attrs: {preparationIds: ["cHJlcGFyYXRpb246MzEzNjk="]}}) {
            recipeItems {
            id
            recipeId
            subRecipeId
            quantity
            }
            }
            }'''.replace(' '*12, '')
        payload = {
            "ids": ["cmVjaXBlOjIwMjI5NA==", None, 1],
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        ret = build_bulk_update_recipe_item_query(payload)
        mutation_str = bytes(ret).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    def test_exception_raised_if_no_recipe_id_provided(self):
        payload = {
            "ids": None,
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        with self.assertRaises(ValueError):
            bulk_update_recipe_item_data(payload)

    def test_exception_raised_if_no_valid_recipe_id_provided(self):
        payload = {
            "ids": [{}, None, 1],
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        with self.assertRaises(ValueError):
            bulk_update_recipe_item_data(payload)

    def test_exception_raised_if_no_attrs_provided(self):
        payload = {
            "ids": ["cmVjaXBlOjIwMjI5NA==", None, 1],
            "attrs": None
        }
        with self.assertRaises(ValueError):
            bulk_update_recipe_item_data(payload)

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_bulk_update_recipe_item_data_raises_exception_if_thrown_from_request(self, mock_mr):
        mock_mr.return_value = {
            "errors": [
                { "message": "Unexpected error value: { message: ... }" }
            ],
            "data": "null"
        }
        payload = {
            "ids": ["cmVjaXBlOjIwMjI5NA=="],
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        with self.assertRaises(ValueError):
            bulk_update_recipe_item_data(payload)
        # result = bulk_update_recipe_item_data(payload)
        # self.assertIsNone(result)

    @mock.patch('galley.mutations.make_request_to_galley')
    @mock.patch('galley.queries.make_request_to_galley')
    def test_bulk_update_recipe_item_data_returns_expected_response_data(self, mock_mr, mock_mr_2):
        mock_mr.return_value = self.response_data
        mock_mr_2.return_value = self.response_data
        payload = {
            "ids": ["cmVjaXBlOjIwMjI5NA=="],
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        result = bulk_update_recipe_item_data(payload)
        self.assertEqual(result, self.response_data['data'])

    @mock.patch('galley.mutations.make_request_to_galley')
    @mock.patch('galley.queries.make_request_to_galley')
    def test_bulk_update_recipe_item_data_avoids_duplications(self, mock_first, mock_second):
        # first migration run
        mock_first.return_value = { "data": self.response_data["data"] }
        # second migration run
        mock_second.return_value = { "data": self.response_data["noRepeats"] }
        payload = {
            "ids": ["cmVjaXBlOjIwMjI5NA=="],
            "attrs": {
                "preparationIds": ["cHJlcGFyYXRpb246MzEzNjk="]
            }
        }
        result = bulk_update_recipe_item_data(payload)
        # expect no repeat response after the second call
        self.assertEqual(result, self.response_data['noRepeats'])
