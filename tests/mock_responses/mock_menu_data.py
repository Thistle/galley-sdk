from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.enums import DietaryFlagEnum, MenuCategoryEnum, MenuItemCategoryEnum, PreparationEnum, RecipeCategoryTagTypeEnum


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
                'volume': 100,
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
                        {
                            'name': '',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'test-recipe-name-1',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'dinner',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'vegan',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
                                'itemType': 'recipe'
                            },
                        }
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
                    'files': {
                        'photos':[
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
                            }
                        ]
                    },
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
                'volume': 0,
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
                        {
                            'name': '',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'test-recipe-name-2',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'dinner',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'vegan',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'new',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_ONE_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'spicy',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_TWO_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                    ],
                    'isDish': True,
                    'files': {
                        'photos': [
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
                        ]
                    },
                    'dietaryFlagsWithUsages': [
                        {
                            'dietaryFlag': {
                                'id': DietaryFlagEnum.COCONUT.id,
                                'name': DietaryFlagEnum.COCONUT.name,
                            }
                        },
                        {
                            'dietaryFlag': {
                                'id': DietaryFlagEnum.SOYBEANS.id,
                                'name': DietaryFlagEnum.SOYBEANS.name,
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
                'volume': None,
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
                        {
                            'name': '',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'test-recipe-name-3',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'lunch',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'meat',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
                                'itemType': 'recipe'
                            },
                        },
                        {
                            'name': 'new',
                            'category': {
                                'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_ONE_TAG.value,
                                'itemType': 'recipe'
                            }
                        },
                    ],
                    'isDish': True,
                    'files': {
                        'photos': [
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
                        ]
                    },
                    'dietaryFlagsWithUsages': [
                        {
                            'dietaryFlag': {
                                'id': DietaryFlagEnum.SOYBEANS.id,
                                'name': DietaryFlagEnum.SOYBEANS.name,
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
                'volume': 300,
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
