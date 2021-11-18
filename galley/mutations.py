from sgqlc.operation import Operation
from sgqlc.types import Field, Type

from galley.common import make_request_to_galley, validate_response_data
from galley.types import (BulkMenusInput, InstructionInput, MenuInput,
                          MenuItemInput, MenuPayload, RecipeInstructionInput,
                          RecipeInstructionPayload, UnitInput)


# This is graphql root for mutating data according to sgqlc lib. So this class name has to be Mutation.
class Mutation(Type):
    createRecipeInstruction = Field(RecipeInstructionPayload, args={'input': RecipeInstructionInput})
    bulkUpsertMenus = Field(MenuPayload, args={'input': BulkMenusInput})


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

# MENU MUTATIONS

def build_unit_input(item):
    if 'unit_name' in item.keys() and item['unit_name'] is not None:
        name = item['unit_name']
    else:
        name = 'each'

    return UnitInput(name=name)

def build_menu_item_inputs(items):
    menu_item_inputs = []
    for item in items:
        unit_input = build_unit_input(item)
        menuItemInput = MenuItemInput(
            id=item['id'],
            volume=item['volume'],
            unit=unit_input
        )
        menu_item_inputs.append(menuItemInput)
    return menu_item_inputs

def build_menu_inputs(menus):
    menu_inputs = []
    for menu in menus:
        if 'menu_id' not in menu.keys() or menu['menu_id'] is None:
            raise ValueError("menu_id is required for successful requests")

        menu_input = MenuInput(id=menu['menu_id'])
        menu_input.menuItems = build_menu_item_inputs(menu['menu_items'])
        menu_inputs.append(menu_input)

    return menu_inputs

def build_upsert_mutation_query(args):
    mutation = Operation(Mutation)
    bulk_input = BulkMenusInput()
    bulk_input.menus = build_menu_inputs(args)
    mutation.bulkUpsertMenus(input=bulk_input)
    return mutation

# args = [
# {
#   menu_id: '',
#       menu_items: [
#           {
#               id: '',
#               volume: float,
#               unit_name: ''
#           },
#           {id: '', ....}
# ]
def upsert_menu_data(args):
    mutation = build_upsert_mutation_query(args)
    response = make_request_to_galley(op=mutation)
    return validate_response_data(response)
