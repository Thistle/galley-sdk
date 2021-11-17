from galley.queries import MenuCategoryEnum


def mock_menu(date, location_name="Vacaville", menu_type="production"):
    return ({
        'name': f"{date} 1_2_3",
        'id': 'MENU123ABC',
        'date': f"{date}",
        'location': {
            'name': location_name,
        },
        'categoryValues': [{
            'id': '1',
            'name': menu_type,
            'category': {
                'id': MenuCategoryEnum.MENU_TYPE.value,
                'name': 'menu type',
                'itemType': 'menu'
            },
        }],
        'menuItems': [
            {
                'recipeId': 'RECIPE1ABC',
                'categoryValues': [{
                    'name': 'dv1',
                    'category': {
                        'itemType': 'menuItem',
                        'name': 'product_code'
                    }
                }],
                'recipe': {
                    'externalName': 'Test Recipe Name 1',
                    'recipeItems': [{
                        'preparations': [
                            {'name':  'standalone'}
                        ],
                        'subRecipeId': 'SUBRECIPEID456'
                    }]
                },
            },
            {
                'recipeId': 'RECIPE2DEF',
                'categoryValues': [{
                    'name': 'dv2',
                    'category': {
                        'itemType': 'menuItem',
                        'name': 'product_code'
                    }
                }],
                'recipe': {
                    'externalName': 'Test Recipe Name 2',
                    'recipeItems': [{
                        'preparations': [
                            {'name':  '2 oz RAM'}
                        ],
                        'subRecipeId': 'SUBRECIPEID789'
                    }]
                },
            },
            {
                'recipeId': 'RECIPE3GHI',
                'categoryValues': [{
                    'name': 'lm2',
                    'category': {
                        'itemType': 'menuItem',
                        'name': 'product_code'
                    }
                }],
                'recipe': {
                    'externalName': 'Test Recipe Name 3',
                    'recipeItems': [{
                        'preparations': [
                            {'name':  '3 oz RAM'},
                            {'name': 'standalone'}
                        ],
                        'subRecipeId': 'SUBRECIPEID321'
                    }]
                },
            }
        ]
    }) if date != '2021-12-05' else []
