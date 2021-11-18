from tests.mock_responses import mock_nutrition_data, mock_recipe_items

def mock_recipe(id):
    return ({
        'id': id,
        'externalName': f'Test Recipe {id}',
        'notes': f'Some notes about recipe {id}',
        'description': f'Details about recipe {id}',
        'categoryValues': [
            {
                'name': 'vegan',
                'category': {
                    'itemType': 'recipe',
                    'name': 'protein type'
                }
            },
            {
                'name': 'ts48',
                'category': {
                    'itemType': 'recipe',
                    'name': 'meal container'
                }
            },
            {
                'name': 'dinner',
                'category': {
                    'itemType': 'recipe',
                    'name': 'meal type'
                }
            },
            {
                'name': 'true',
                'category': {
                    'itemType': 'recipe',
                    'name': 'is perishable'
                }
            }
        ],
        'recipeItems': mock_recipe_items.mock_data,        
        'reconciledNutritionals': mock_nutrition_data.mock_data,
        'recipeTreeComponents': []
    })