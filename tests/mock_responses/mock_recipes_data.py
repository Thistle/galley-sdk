from tests.mock_responses import (mock_nutrition_data,
                                  mock_recipe_items,
                                  mock_recipe_tree_components,
                                  mock_recipe_category_values,
                                  mock_all_ingredients_with_usages_data)


def mock_recipe_base(id):
    return ({
        'id': id,
        'externalName': f'Test Recipe {id}',
        'notes': f'Some notes about recipe {id}',
        'description': f'Details about recipe {id}',
        'categoryValues': mock_recipe_category_values.mock_data,
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
        'recipeItems': mock_recipe_items.mock_data,
        'reconciledNutritionals': mock_nutrition_data.mock_data,
        'allIngredientsWithUsages': mock_all_ingredients_with_usages_data.mock_data,
        'dietaryFlagsWithUsages': []
})


def mock_recipe(id):
    return ({
        **mock_recipe_base(id),
        'recipeTreeComponents': mock_recipe_tree_components.mock_recipe_tree_components_data
    })


def mock_recipe_with_no_standalone_recipe_item(id):
    return ({
        **mock_recipe_base(id),
        'recipeTreeComponents': mock_recipe_tree_components.mock_recipe_tree_components_data_no_pkg_no_standalone
    })


def mock_recipe_with_standalone_recipe_item(id):
    return ({
        **mock_recipe_base(id),
        'recipeTreeComponents': mock_recipe_tree_components.mock_recipe_tree_components_data_with_multiple_servings_of_standalone
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


def mock_recipe_connection_with_no_standalone(ids,
                                              end_index: int = 1,
                                              has_next_page: bool = False,
                                              has_previous_page: bool = False,
                                              start_index: int = 0):
    edges = []
    for id in ids:
        edges.append(
            {
                'node': mock_recipe_with_no_standalone_recipe_item(id)
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
