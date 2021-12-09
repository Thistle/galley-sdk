from galley.types import PageInfoType
from tests.mock_responses import mock_nutrition_data, mock_recipe_items, mock_recipe_tree_components
from galley.enums import RecipeCategoryTagTypeEnum


def mock_recipe_base(id):
    return ({
        'id': id,
        'externalName': f'Test Recipe {id}',
        'notes': f'Some notes about recipe {id}',
        'description': f'Details about recipe {id}',
        'categoryValues': [
            {
                'name': 'vegan',
                'category': {
                    'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
                    'itemType': 'recipe',
                    'name': 'protein type'
                }
            },
            {
                'name': 'ts48',
                'category': {
                    'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                    'itemType': 'recipe',
                    'name': 'meal container'
                }
            },
            {
                'name': 'dinner',
                'category': {
                    'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
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
                    'id': RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value,
                    'itemType': 'recipe',
                    'name': 'protein addon'
                }
            },
            {
                'name': 'base-salad',
                'category': {
                    'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                    'itemType': 'recipe',
                    'name': 'base meal slug'
                }
            }
        ],
        'recipeItems': mock_recipe_items.mock_data,
        'reconciledNutritionals': mock_nutrition_data.mock_data
})


def mock_recipe(id):
    return ({
        **mock_recipe_base(id),
        'recipeTreeComponents': mock_recipe_tree_components.mock_data
    })


def mock_recipe_with_standalone_recipe_item(id):
    return ({
        **mock_recipe_base(id),
        'recipeTreeComponents': mock_recipe_tree_components.mock_data_standalone_recipe_item
    })


def mock_page_info(end_index: int = 1, 
                   has_next_page: bool = False, 
                   has_previous_page: bool = False, 
                   start_index: int = 0):
    return ({
        'endIndex': end_index,
        'hasNextPage': has_next_page,
        'hasPreviousPage': has_previous_page,
        'startIndex': start_index
    })


def mock_recipe_connection(ids, 
                           end_index: int = 1, 
                           has_next_page: bool = False, 
                           has_previous_page: bool = False, 
                           start_index: int = 0):
    edges = []
    for id in ids:
        edges.append(
            {
                'node': mock_recipe(id)
            }
        )

    return ({        
        'edges': edges,
        'pageInfo': mock_page_info(
            end_index=end_index,
            has_next_page=has_next_page,
            has_previous_page=has_previous_page,
            start_index=start_index)
    })


def mock_recipe_connection_with_standalone(ids, 
                           end_index: int = 1, 
                           has_next_page: bool = False, 
                           has_previous_page: bool = False, 
                           start_index: int = 0):
    edges = []
    for id in ids:
        edges.append(
            {
                'node': mock_recipe_with_standalone_recipe_item(id)
            }
        )

    return ({        
        'edges': edges,
        'pageInfo': mock_page_info(
            end_index=end_index,
            has_next_page=has_next_page,
            has_previous_page=has_previous_page,
            start_index=start_index)
    })