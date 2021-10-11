from sgqlc.operation import Operation
from sgqlc.types import Field, Type

from galley.types import RecipeInstructionPayload, RecipeInstructionInput, InstructionInput
from galley.common import make_request_to_galley, validate_response_data


# This is graphql root for mutating data according to sgqlc lib. So this class name has to be Mutation.
class Mutation(Type):
    createRecipeInstruction = Field(RecipeInstructionPayload, args={'input': RecipeInstructionInput})


# RECIPE MUTATIONS

def add_recipe_instruction(recipe_id, instruction, position=None):
    mutation = Operation(Mutation)
    vars = {'recipeId': recipe_id, 'text': instruction}

    if position is not None:
        mutation.createRecipeInstruction(input=RecipeInstructionInput(
            recipeId=recipe_id,
            recipeInstruction=InstructionInput(text=instruction, position=position)
        )).recipeInstruction().__fields__('recipeId', 'text', 'position')
        vars.setdefault('position', position)
    else:
        mutation.createRecipeInstruction(input=RecipeInstructionInput(
            recipeId=recipe_id,
            recipeInstruction=InstructionInput(text=instruction)
        )).recipeInstruction().__fields__('recipeId', 'text', 'position')

    raw_data = make_request_to_galley(op=mutation, variables=vars)
    return validate_response_data(raw_data, 'createRecipeInstruction', 'recipeInstruction')

