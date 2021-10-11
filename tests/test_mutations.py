from unittest import mock, TestCase
from sgqlc.operation import Operation

from galley.mutations import Mutation, add_recipe_instruction
from galley.types import RecipeInstructionInput, InstructionInput
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

