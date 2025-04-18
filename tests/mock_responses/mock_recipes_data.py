from tests.mock_responses.mock_nutrition_data import MOCK_RECONCILED_NUTRITIONALS
from tests.mock_responses.mock_recipe_category_values import MOCK_RECIPE_CATEGORY_VALUES
from tests.mock_responses.mock_recipe_items_ingredients_with_usages import (
    MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE,
    BASE_RECIPE_DF_ID,
    BASE_RECIPE_DF_NAME,
    STANDALONE_DF_ID,
    STANDALONE_DF_NAME,
    SELLABLE_RECIPE_ID,
    SELLABLE_RECIPE_NAME,
)
from typing import List


def mock_recipe_base(id: str):
    return ({
        'id': SELLABLE_RECIPE_ID,
        'externalName': SELLABLE_RECIPE_NAME,
        'notes': f'Some notes about recipe {id}',
        'description': f'Details about recipe {id}',
        'categoryValues': MOCK_RECIPE_CATEGORY_VALUES,
        'files': {
            'photos': [
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
                    'caption': 'Menu Photo',
                    'sourceUrl': f'https://cdn.filestackcontent.com/MENU{id}',
                    'mediaId': 'bWVkaWE6OTEwNA==',
                    'storageKey': f'Thistle/Media/1uTFWcWhTIGBpybJ1axc_menu{id}.jpg'
                },
                {
                    'altText': f'modal{id}.jpg',
                    'caption': 'Modal Photo',
                    'sourceUrl': f'https://cdn.filestackcontent.com/MODAL{id}',
                    'mediaId': 'bWVkaWE6OTEwNA==',
                    'storageKey': f'Thistle/Media/1uTFWcWhTIGBpybJ1axc_modal{id}.jpg'
                }
            ],
        },
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
        'dietaryFlagsWithUsages': [
            {
                "dietaryFlag": {
                    "id": BASE_RECIPE_DF_ID,
                    "name": BASE_RECIPE_DF_NAME,
                }
            },
            {
                "dietaryFlag": {
                    "id": STANDALONE_DF_ID,
                    "name": STANDALONE_DF_NAME,
                }
            },
        ]
})


def mock_recipe(id: str):
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


def mock_recipe_connection(ids: List[str],
                           end_index: int = 1,
                           has_next_page: bool = False,
                           has_previous_page: bool = False,
                           start_index: int = 0):
    return ({
        'edges': [dict(node=mock_recipe(id)) for id in ids],
        'pageInfo': mock_page_info(
            end_index=end_index,
            has_next_page=has_next_page,
            has_previous_page=has_previous_page,
            start_index=start_index)
    })
