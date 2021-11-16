def mock_menu(name):
    return ({
        'name': name,
        'id': 'MENU123ABC',
        'date': 'YYYY-MM-DD',
        'location': {
            'name': 'Vacaville'
        },
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
    }) if name.split()[0] != '21-12-05' else []