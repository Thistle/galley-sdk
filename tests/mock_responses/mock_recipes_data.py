from tests.mock_responses import mock_nutrition_data, mock_recipe_items, mock_recipe_tree_components

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
                    'id': "Y2F0ZWdvcnk6MjUwOA==",
                    'itemType': 'recipe',
                    'name': 'protein type'
                }
            },
            {
                'name': 'ts48',
                'category': {
                    'id': "Y2F0ZWdvcnk6MjU2Nw==",
                    'itemType': 'recipe',
                    'name': 'meal container'
                }
            },
            {
                'name': 'dinner',
                'category': {
                    'id': "Y2F0ZWdvcnk6MjQyMg==",
                    'itemType': 'recipe',
                    'name': 'meal type'
                }
            },
            {
                'name': 'true',
                'category': {
                    'id': "",
                    'itemType': 'recipe',
                    'name': 'is perishable'
                }
            },
            {
                'name': 'high-protein-legume',
                'category': {
                    'id': "Y2F0ZWdvcnk6MjU4MQ==",
                    'itemType': 'recipe',
                    'name': 'protein addon'
                }
            },
            {
                'name': 'base-salad',
                'category': {
                    'id': "Y2F0ZWdvcnk6MjYyMA==",
                    'itemType': 'recipe',
                    'name': 'base meal slug'
                }
            }
        ],
        'recipeItems': mock_recipe_items.mock_data,
        'reconciledNutritionals': mock_nutrition_data.mock_data,
        'recipeTreeComponents': mock_recipe_tree_components.mock_data
    })
