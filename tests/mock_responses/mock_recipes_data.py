from tests.mock_responses.mock_nutrition_data import MOCK_RECONCILED_NUTRITIONALS
from tests.mock_responses.mock_recipe_category_values import MOCK_RECIPE_CATEGORY_VALUES
from tests.mock_responses.mock_recipe_items_ingredients_with_usages import (
    SELLABLE_RECIPE_ID,
    SELLABLE_RECIPE_NAME,
    MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE
)


def mock_recipe_base(id):
    return ({
        'id': SELLABLE_RECIPE_ID,
        'externalName': SELLABLE_RECIPE_NAME,
        'notes': f'Some notes about recipe {id}',
        'description': f'Details about recipe {id}',
        'categoryValues': MOCK_RECIPE_CATEGORY_VALUES,
        'media': [
            {
                'altText': 'None.jpg',
                'caption': None,
                'sourceUrl': 'https://cdn.filestackcontent.com/HaCZIYLBRfWmeMtErKSU',
                'mediaId': 'bWVkaWE6OTEwNA==',
                'storageKey': 'Thistle/Media/ujTTMJETR1eV9LJMJTJo_None.jpg'
            },
            {
                'altText': 'Plating.jpg',
                'caption': 'Plating Photo',
                'sourceUrl': 'https://cdn.filestackcontent.com/rVVEymFAQv4m0LTYz3IV',
                'mediaId': 'bWVkaWE6TEOwNQ==',
                'storageKey': 'Thistle/Media/TnLOVsiTG61I5W1VFwqw_.jpg'
            },
            {
                'altText': f'menu{id}.jpg',
                'caption': 'menu',
                'sourceUrl': f'https://cdn.filestackcontent.com/MENU{id}',
                'mediaId': 'bWVkaWE6OTEwNA==',
                'storageKey': f'Thistle/Media/1uTFWcWhTIGBpybJ1axc_menu{id}.jpg'
            },
        ],
        'versionConnection': {
            'edges': [
                {
                    'node': {
                        'id': 'dmVyc2lvbjozNjQ0NTY1',
                        'versionNumber': 107,
                        'action': 'update'
                    }
                }
            ]
        },
        'isDish': True,
        'reconciledNutritionals': MOCK_RECONCILED_NUTRITIONALS,
        'dietaryFlagsWithUsages': []
})


def mock_recipe(id):
    return ({
        **mock_recipe_base(id),
        **MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE()
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
