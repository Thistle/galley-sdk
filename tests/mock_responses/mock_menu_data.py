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
                    'categoryValues': [
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value,
                            'itemType': 'recipe',
                            'name': 'protein addon'
                        },
                         'id': 'Y2F0ZWdvcnlWYWx1ZToxNjIxMA==',
                         'name': 'chipotle pulled pork'
                        },
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
                            'itemType': 'recipe',
                            'name': 'base meal'
                        },
                         'id': 'Y2F0ZWdvcnlWYWx1ZToxNjYzMQ==',
                         'name': ''},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                            'itemType': 'recipe',
                            'name': 'base meal slug'
                        },
                         'id': 'Y2F0ZWdvcnlWYWx1ZToxNTcwNA==',
                         'name': 'test-recipe-name-1'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                            'itemType': 'recipe',
                            'name': 'meal container'
                        },
                         'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                         'name': 'ts32'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
                            'itemType': 'recipe',
                            'name': 'meal type'
                        },
                         'id': 'Y2F0ZWdvcnlWYWx1ZToxNDYzMQ==',
                         'name': 'dinner'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
                            'itemType': 'recipe',
                            'name': 'protein type'
                        },
                         'id': 'Y2F0ZWdvcnlWYWx1ZToxNDQ4OQ==',
                         'name': 'vegan'}
                    ],
                    'isDish': True,
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
                'categoryValues': [
                    {
                        'name': 'dv2',
                        'category': {
                            'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                            'itemType': 'menuItem',
                            'name': 'product_code'
                        }
                    }
                ],
                'recipe': {
                    'externalName': 'Test Recipe Name 2',
                    'categoryValues': [
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value,
                            'itemType': 'recipe',
                            'name': 'protein addon'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNjIxMA==',
                            'name': 'chipotle pulled pork'
                        },
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
                            'itemType': 'recipe',
                            'name': 'base meal'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNjYzMQ==',
                            'name': ''},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                            'itemType': 'recipe',
                            'name': 'base meal slug'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNTcwNA==',
                            'name': 'test-recipe-name-2'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                            'itemType': 'recipe',
                            'name': 'meal container'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                            'name': 'ts32'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
                            'itemType': 'recipe',
                            'name': 'meal type'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNDYzMQ==',
                            'name': 'dinner'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
                            'itemType': 'recipe',
                            'name': 'protein type'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNDQ4OQ==',
                            'name': 'vegan'}
                    ],
                    'isDish': True,
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
                    'categoryValues': [
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value,
                            'itemType': 'recipe',
                            'name': 'protein addon'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNjIxMA==',
                            'name': 'chipotle pulled pork'
                        },
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
                            'itemType': 'recipe',
                            'name': 'base meal'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNjYzMQ==',
                            'name': ''},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                            'itemType': 'recipe',
                            'name': 'base meal slug'
                        },
                            'id': 'uniqueCatvalueId',
                            'name': 'test-recipe-name-3'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                            'itemType': 'recipe',
                            'name': 'meal container'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                            'name': 'ts32'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
                            'itemType': 'recipe',
                            'name': 'meal type'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNDYzMQ==',
                            'name': 'lunch'},
                        {'category': {
                            'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
                            'itemType': 'recipe',
                            'name': 'protein type'
                        },
                            'id': 'Y2F0ZWdvcnlWYWx1ZToxNDQ4OQ==',
                            'name': 'meat'}
                    ],
                    'isDish': True,
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
                },
            },
            {
                'id': 'MENUITEM4JKL',
                'recipeId': 'RECIPE4JKL',
                'categoryValues': [{
                    'name': 'non-sellable soup',
                    'category': {
                        'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                        'itemType': 'menuItem',
                        'name': 'product_code'
                    }
                }],
                'recipe': {
                    'externalName': 'Test Recipe Name 4',
                    'categoryValues': [],
                    'isDish': False,
                    'recipeItems': [{
                        'preparations': [],
                        'subRecipeId': None
                    }],
                },
            }
        ]
    }) if date != '2021-12-05' else []
