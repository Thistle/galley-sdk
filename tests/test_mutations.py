from unittest import mock, TestCase
from sgqlc.operation import Operation

from galley.mutations import Mutation, add_recipe_instruction, upsert_menu_data, build_upsert_mutation_query
from galley.types import (
    MenuInput,
    Menu,
    RecipeInstructionInput,
    InstructionInput
)
import logging

logger = logging.getLogger(__name__)


class TestCreateRecipeInstructionMethod(TestCase):
    def setUp(self) -> None:
        self.galley_graphql_mutation_str = '''mutation {
            createRecipeInstruction(input: {recipeId: "cmVjaXBlOjE2NDgzMw", recipeInstruction: {text: "Add salt"}}) {
            recipeInstruction {
            recipeId
            text
            position
            }
            }
            }'''.replace(' '*12, '')

        self.payload = {
            'recipeId': 'ABCDE123',
            'text': 'Test instruction text.',
            'position': 10
        }

        self.data = {
            'data': {
                'createRecipeInstruction': {
                    'recipeInstruction': self.payload
                }
            }
        }

    def test_add_recipe_instruction_mutation(self):
        mutation_operation = Operation(Mutation)
        mutation_operation.createRecipeInstruction(input=RecipeInstructionInput(
            recipeId="cmVjaXBlOjE2NDgzMw",
            recipeInstruction=InstructionInput(text="Add salt")
        )).recipeInstruction().__fields__('recipeId', 'text', 'position')
        mutation_str = bytes(mutation_operation).decode('utf-8')
        self.assertEqual(mutation_str, self.galley_graphql_mutation_str)

    def test_add_recipe_instruction_failure(self):
        mutation_operation = Operation(Mutation)
        mutation_str = bytes(mutation_operation).decode('utf-8')
        self.assertNotEqual(mutation_str, self.galley_graphql_mutation_str)

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_add_recipe_instruction_with_step_successful(self, mock_mr):
        mock_mr.return_value = self.data
        result = add_recipe_instruction('ABCDE123', 'Test instruction text.', 10)
        self.assertEqual(result, self.payload)

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_add_recipe_instruction_without_step_successful(self, mock_mr):
        mock_mr.return_value = self.data
        result = add_recipe_instruction('ABCDE123', 'Test instruction text.')
        self.assertEqual(result, self.payload)

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_add_recipe_instruction_validation_failure(self, mock_mr):
        mock_mr.return_value = {
            'data': {
                'createRecipeInstruction': {
                    'test': 'test'
                }
            }
        }
        result = add_recipe_instruction('ABCDE123', 'Test instruction text.')
        self.assertEqual(result, None)

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
        result = upsert_menu_data(payload)
        self.assertIsNone(result)

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
