from galley.enums import MenuCategoryEnum, MenuItemCategoryEnum, PreparationEnum, RecipeCategoryTagTypeEnum


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
                'id': 'MENUITEM1ABC',
                'recipeId': 'RECIPE1ABC',
                'categoryValues': [{
                    'name': 'dv1',
                    'category': {
                        'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                        'itemType': 'menuItem',
                        'name': 'product_code'
                    }
                }],
                'recipe': {
                    'externalName': 'Test Recipe Name 1',
                    'recipeItems': [{
                        'preparations': [
                            {
                                'id': PreparationEnum.STANDALONE.value,
                                'name':  'standalone'
                            }
                        ],
                        'subRecipeId': 'SUBRECIPEID456'
                    }]
                },
            },
            {
                'id': 'MENUITEM2DEF',
                'recipeId': 'RECIPE2DEF',
                'categoryValues': [{
                    'name': 'dv2',
                    'category': {
                        'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                        'itemType': 'menuItem',
                        'name': 'product_code'
                    }
                }],
                'recipe': {
                    'externalName': 'Test Recipe Name 2',
                    'recipeItems': [{
                        'preparations': [
                            {
                                'id': PreparationEnum.TWO_OUNCE_RAM.value,
                                'name':  '2 oz RAM'
                            }
                        ],
                        'subRecipeId': 'SUBRECIPEID789'
                    }]
                },
            },
            {
                'id': 'MENUITEM3GHI',
                'recipeId': 'RECIPE3GHI',
                'categoryValues': [{
                    'name': 'lm2',
                    'category': {
                        'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                        'itemType': 'menuItem',
                        'name': 'product_code'
                    }
                }],
                'recipe': {
                    'externalName': 'Test Recipe Name 3',
                    'recipeItems': [{
                        'preparations': [
                            {
                                'id': PreparationEnum.THREE_OUNCE_RAM.value,
                                'name':  '3.25 oz RAM'},
                            {
                                'id': PreparationEnum.STANDALONE.value,
                                'name': 'standalone'
                            }
                        ],
                        'subRecipeId': 'SUBRECIPEID321'
                    }],
                    'categoryValues': [{
                        'id': 'uniqueCatvalueId',
                        'name': 'test-recipe-name-3',
                        'category': {
                            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                            'name': 'base meal slug',
                            'itemType': 'recipe'
                        }
                    }]
                },
            }
        ]
    }) if date != '2021-12-05' else []
