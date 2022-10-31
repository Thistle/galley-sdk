from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.enums import MenuCategoryEnum, MenuItemCategoryEnum, PreparationEnum, RecipeCategoryTagTypeEnum


def mock_menu(date, location_name= DEFAULT_LOCATION, menu_type=DEFAULT_MENU_TYPE):
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
                    "versionConnection": {
                        "edges": [
                            {
                                "node": {
                                    "id": "dmVyc2lvbjozNjQ0NTY1",
                                    "versionNumber": 107,
                                    "action": "update"
                                }
                            }
                        ]
                    },
                    'media': [
                        {
                            'altText': 'Recipe_1_Plating.jpg',
                            'caption': 'plating',
                            'sourceUrl': 'https://cdn.filestackcontent.com/Recipe_1_Plating',
                            'mediaId': 'bWVkaWE6TEOwNQ==',
                            'storageKey': 'Thistle/Media/TnLOVsiTG61I5W1VFwqw_.jpg'
                        },
                        {
                            'altText': 'Recipe_1_Menu.jpg',
                            'caption': 'menu',
                            'sourceUrl': 'https://cdn.filestackcontent.com/Recipe_1_Menu',
                            'mediaId': 'bWVkaWE6OTEwNA==',
                            'storageKey': 'Thistle/Media/1uTFWcWhTIGBpybJ1axc_.jpg'
                        },
                    ],
                    'dietaryFlagsWithUsages': [],
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
                            'name': 'vegan'},
                        {
                            'name': 'new',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_ONE_TAG.value,
                                'itemType': 'recipe',
                                'name': 'highlight_1'
                            }
                        },
                        {
                            'name': 'spicy',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_TWO_TAG.value,
                                'itemType': 'recipe',
                                'name': 'highlight_2'
                            }
                        },
                    ],
                    'isDish': True,
                    'media': [
                        {
                            'altText': 'Recipe_2_Plating.jpg',
                            'caption': 'plating',
                            'sourceUrl': 'https://cdn.filestackcontent.com/Recipe_2_Plating',
                            'mediaId': 'bWVkaWE6TEOwNQ==',
                            'storageKey': 'Thistle/Media/TnLOVsiTG61I5W1VFwqw_.jpg'
                        },
                        {
                            'altText': 'Recipe_2_Menu.jpg',
                            'caption': 'menu',
                            'sourceUrl': 'https://cdn.filestackcontent.com/Recipe_2_Menu',
                            'mediaId': 'bWVkaWE6OTEwNA==',
                            'storageKey': 'Thistle/Media/1uTFWcWhTIGBpybJ1axc_.jpg'
                        },
                    ],
                    'dietaryFlagsWithUsages': [
                        {
                            'dietaryFlag': {
                                'id': 'ZGlldGFyeUZsYWc6OTc=',
                                'name': 'coconut'
                            }
                        },
                        {
                            'dietaryFlag': {
                                'id': 'ZGlldGFyeUZsYWc6Ng==',
                                'name': 'soy beans'
                            }
                        }
                    ],
                    'recipeItems': [{
                        'preparations': [
                            {
                                'id': PreparationEnum.TWO_OZ_RAM.value,
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
                            'name': 'meat'},
                        {
                            'name': 'new',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_ONE_TAG.value,
                                'itemType': 'recipe',
                                'name': 'highlight_1'
                            }
                        },
                    ],
                    'isDish': True,
                    'media': [
                        {
                            'altText': 'Recipe_3_Plating.jpg',
                            'caption': 'plating',
                            'sourceUrl': 'https://cdn.filestackcontent.com/Recipe_3_Plating',
                            'mediaId': 'bWVkaWE6TEOwNQ==',
                            'storageKey': 'Thistle/Media/TnLOVsiTG61I5W1VFwqw_.jpg'
                        },
                        {
                            'altText': 'Recipe_3_Menu.jpg',
                            'caption': 'menu',
                            'sourceUrl': 'https://cdn.filestackcontent.com/Recipe_3_Menu',
                            'mediaId': 'bWVkaWE6OTEwNA==',
                            'storageKey': 'Thistle/Media/1uTFWcWhTIGBpybJ1axc_.jpg'
                        },
                    ],
                    'dietaryFlagsWithUsages': [
                        {
                            'dietaryFlag': {
                                'id': 'ZGlldGFyeUZsYWc6Ng==',
                                'name': 'soy beans'
                            }
                        }
                    ],
                    'recipeItems': [{
                        'preparations': [
                            {
                                'id': PreparationEnum.THREE_OZ_RAM.value,
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
