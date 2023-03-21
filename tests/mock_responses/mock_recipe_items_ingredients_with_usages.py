from copy import deepcopy
from galley.enums import IngredientCategoryTagTypeEnum, IngredientCategoryValueEnum, PreparationEnum, UnitEnum
from tests.mock_responses.mock_nutrition_data import MOCK_RECONCILED_NUTRITIONALS, MOCK_STANDALONE_RECONCILED_NUTRITIONALS


SELLABLE_RECIPE_ID = "cmVjaXBlOjIwMjA1OQ=="
SELLABLE_RECIPE_NAME = "Very Delicious Salad"
STANDALONE_RECIPE_ID = "cmVjaXBlOjIyMTEzMg=="
STANDALONE_RECIPE_NAME = "Very Creamy Dressing"


MOCK_RECIPE_ITEMS = [
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [
            {
                "id": PreparationEnum.CORE_RECIPE.value,
                "name": "Core Recipe"
            }
        ],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 262.233088675,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 9.25,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.578124999490181,
                    "unit": {
                        "id": UnitEnum.LB.value,
                        "name": "lb"
                    }
                },
                {
                    "value": 1,
                    "unit": {
                        "id": UnitEnum.EACH.value,
                        "name": "each"
                    }
                }
            ]
        },
        "subRecipe": {
            "id": "cmVjaXBlOjE3OTUzOQ==",
            "name": "Rainbow Slaw Salad BASE",
            "externalName": None,
            "nutritionalsQuantity": None,
            "nutritionalsUnit": None,
            "reconciledNutritionals": MOCK_RECONCILED_NUTRITIONALS,
        },
        "ingredient": None
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 102.05828316,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 3.6,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.22499999980158394,
                    "unit": {
                        "id": UnitEnum.LB.value,
                        "name": "lb"
                    }
                },
                {
                    "value": 1,
                    "unit": {
                        "id": UnitEnum.EACH.value,
                        "name": "each"
                    }
                }
            ]
        },
        "subRecipe": None,
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "ORG, CARROTS RAINBOW SHREDDED 4/5#",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQzNDg=",
            "name": "carrot rainbow, shredded PF, SEND TO PLATE",
            "externalName": "Rainbow Carrots*",
            "categoryValues": [
                {
                    "id": "Y2F0ZWdvcnlWYWx1ZToxNDM5NQ==",
                    "name": "send to plate",
                    "category": {
                        "id": "Y2F0ZWdvcnk6MjUwMg==",
                        "name": "lead time",
                        "itemType": "ingredient"
                    }
                }
            ]
        }
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [],
        "quantity": 2.5,
        "unit": {
            "id": UnitEnum.OZ.value,
            "name": "oz",
            "unitValues": [
                {
                    "value": 28.3495231,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 1,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.06249999994488443,
                    "unit": {
                        "id": UnitEnum.LB.value,
                        "name": "lb"
                    }
                }
            ]
        },
        "subRecipe": {
            "id": "cmVjaXBlOjI4MDkyMg==",
            "name": "Herb Kidney Beans",
            "externalName": None,
            "nutritionalsQuantity": None,
            "nutritionalsUnit": None,
            "reconciledNutritionals": MOCK_RECONCILED_NUTRITIONALS
        },
        "ingredient": None
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [
            {
                "id": PreparationEnum.STANDALONE.value,
                "name": "standalone"
            },
            {
                "id": PreparationEnum.THREE_OZ_RAM.value,
                "name": "3.25 oz RAM"
            }
        ],
        "quantity": 2,
        "unit": {
            "id": UnitEnum.OZ.value,
            "name": "oz",
            "unitValues": [
                {
                    "value": 28.3495231,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 1,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.06249999994488443,
                    "unit": {
                        "id": UnitEnum.LB.value,
                        "name": "lb"
                    }
                }
            ]
        },
        "subRecipe": {
            "id": STANDALONE_RECIPE_ID,
            "name": "Creamy Poppy Seed Dressing 2 oz",
            "externalName": STANDALONE_RECIPE_NAME,
            "nutritionalsQuantity": 1,
            "nutritionalsUnit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "reconciledNutritionals": MOCK_STANDALONE_RECONCILED_NUTRITIONALS
        },
        "ingredient": None
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 65.20390312999999,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 2.3,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.14374999987323417,
                    "unit": {
                        "id": UnitEnum.LB.value,
                        "name": "lb"
                    }
                },
                {
                    "value": 1,
                    "unit": {
                        "id": UnitEnum.EACH.value,
                        "name": "each"
                    }
                }
            ]
        },
        "subRecipe": None,
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "TS48",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDU5MDM=",
            "name": "TS48 - 48oz Meal Boxes",
            "externalName": "48 oz Meal Boxes",
            "categoryValues": [
                {
                    "id": IngredientCategoryValueEnum.FOOD_PACKAGE.value,
                    "name": "food pkg",
                    "category": {
                        "id": IngredientCategoryTagTypeEnum.ACCOUNTING_TAG.value,
                        "name": "accounting group",
                        "itemType": "ingredient"
                    }
                }
            ]
        }
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 2.8349523099999998e-05,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 1e-06,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 6.249999994488442e-08,
                    "unit": {
                        "id": UnitEnum.LB.value,
                        "name": "lb"
                    }
                },
                {
                    "value": 1,
                    "unit": {
                        "id": UnitEnum.EACH.value,
                        "name": "each"
                    }
                }
            ]
        },
        "subRecipe": None,
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "Meal Vegan - 2.75\" x 8\"",
                            "priority": 0,
                            "ingredientListStr": None
                        },
                        {
                            "name": "Meal Vegan - 2.75\" x 8\"",
                            "priority": 1,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDU5MjY=",
            "name": "label vegan meal",
            "externalName": "Vegan Meal Label",
            "categoryValues": [
                {
                    "id": IngredientCategoryValueEnum.FOOD_PACKAGE.value,
                    "name": "food pkg",
                    "category": {
                        "id": IngredientCategoryTagTypeEnum.ACCOUNTING_TAG.value,
                        "name": "accounting group",
                        "itemType": "ingredient"
                    }
                },
                {
                    "id": IngredientCategoryValueEnum.LABEL.value,
                    "name": "label",
                    "category": {
                        "id": "Y2F0ZWdvcnk6Mzc4Mg==",
                        "name": "packaging type",
                        "itemType": "ingredient"
                    }
                }
            ]
        }
    }
]


INGREDIENTS_WITH_USAGES = [
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "CANNED, GARBANZO BEAN OG, 6/108oz (40.5#cs) 08009",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQyODA=",
            "name": "beans, garbanzo, canned",
            "externalName": "Garbanzo Beans (Garbanzo Beans, Water, Salt)",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.0030555555528610167,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "BEAN, KINDEY RED DK,25#",
                            "priority": 0,
                            "ingredientListStr": None
                        },
                        {
                            "name": "beans, kidney, dry",
                            "priority": 1,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQyODQ=",
            "name": "beans, kidney, dry",
            "externalName": "Kidney Beans*",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjI4MDkyMg==",
                        "name": "Herb Kidney Beans"
                    }
                ],
                "quantity": 0.07812499993110555,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "ORG, CARROTS RAINBOW SHREDDED 4/5#",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQzNDg=",
            "name": "carrot rainbow, shredded PF, SEND TO PLATE",
            "externalName": "Rainbow Carrots*",
            "categoryValues": [
                {
                    "id": "Y2F0ZWdvcnlWYWx1ZToxNDM5NQ==",
                    "name": "send to plate",
                    "category": {
                        "id": "Y2F0ZWdvcnk6MjUwMg==",
                        "name": "lead time",
                        "itemType": "ingredient"
                    }
                }
            ]
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    }
                ],
                "quantity": 0.22499999980158394,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "DRIED FRUIT, CHERRIES, BING, PTTD 25# F131",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQzOTk=",
            "name": "dried fruit, cherries",
            "externalName": "Dried Cherries*",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 0.02916666664094607,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "GARLIC, #1 PEELED 4/5#",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ0NjI=",
            "name": "garlic, cloves",
            "externalName": "Garlic",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.004166666662992296,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "5 Gallon Pail, Grade A Dark & Robust, Organic Maple Syrup LESS THAN 12",
                            "priority": 0,
                            "ingredientListStr": None
                        },
                        {
                            "name": "Syrup Maple 100%",
                            "priority": 1,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
            "name": "maple syrup",
            "externalName": "Maple Syrup*",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.01041666665748074,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "OIL, OLIVE_EXTRA VIRGIN 420#drum",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ2MzA=",
            "name": "oil, olive",
            "externalName": "Extra Virgin Olive Oil",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 0.004166666662992296,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            },
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjI4MDkyMg==",
                        "name": "Herb Kidney Beans"
                    }
                ],
                "quantity": 0.031249999972442218,
                "unit": {
                    "id": UnitEnum.OZ.value,
                    "name": "oz",
                    "unitValues": [
                        {
                            "value": 28.3495231,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 0.06249999994488443,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "spices, salt, himalyan pink",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
            "name": "salt, sea",
            "externalName": "Sea Salt",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.016666666651969184,
                "unit": {
                    "id": UnitEnum.OZ.value,
                    "name": "oz",
                    "unitValues": [
                        {
                            "value": 28.3495231,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 0.06249999994488443,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            },
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 0.008333333325984592,
                "unit": {
                    "id": UnitEnum.OZ.value,
                    "name": "oz",
                    "unitValues": [
                        {
                            "value": 28.3495231,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 0.06249999994488443,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                    ]
                }
            },
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjI4MDkyMg==",
                        "name": "Herb Kidney Beans"
                    }
                ],
                "quantity": 0.007812499993110554,
                "unit": {
                    "id": UnitEnum.OZ.value,
                    "name": "oz",
                    "unitValues": [
                        {
                            "value": 28.3495231,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 0.06249999994488443,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "MUSTARD DIJON SMOOTH TIN 54#  135622",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ3NzA=",
            "name": "sauce, mustard, dijon",
            "externalName": "Dijon Mustard (Water, Mustard Seeds, Vinegar, Salt)",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.004583333329291525,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "PUMPKIN SEEDS, HULLED 55.12#",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ3Nzk=",
            "name": "seeds, pumpkin",
            "externalName": "Pumpkin Seed",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 0.01041666665748074,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "seeds, poppy",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ3ODA=",
            "name": "seeds, poppy",
            "externalName": "Poppy Seeds*",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.016666666651969184,
                "unit": {
                    "id": UnitEnum.OZ.value,
                    "name": "oz",
                    "unitValues": [
                        {
                            "value": 28.3495231,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 0.06249999994488443,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "VINEGAR, APPLE CIDER  462# drum",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDQ5MDU=",
            "name": "vinegar, apple cider",
            "externalName": "Apple Cider Vinegar",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.0030555555528610167,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "THISTLE, BEETS RED SHREDDED 4/5#",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDUzMDM=",
            "name": "beets, red, shredded PF, SEND TO PLATE",
            "externalName": "Red Beets",
            "categoryValues": [
                {
                    "id": "Y2F0ZWdvcnlWYWx1ZToxNDM5NQ==",
                    "name": "send to plate",
                    "category": {
                        "id": "Y2F0ZWdvcnk6MjUwMg==",
                        "name": "lead time",
                        "itemType": "ingredient"
                    }
                }
            ]
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 0.062499999944884435,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "Frozen Parsley Small 38#",
                            "priority": 0,
                            "ingredientListStr": None
                        },
                        {
                            "name": "herb, frozen, parsley",
                            "priority": 1,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDUzMjM=",
            "name": "herb, frozen, parsley",
            "externalName": "Parsley",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjI4MDkyMg==",
                        "name": "Herb Kidney Beans"
                    }
                ],
                "quantity": 0.002604166664370185,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "CANNED, GARBANZO BEAN OG, 6/108oz (40.5#cs) 08009",
                            "priority": 0,
                            "ingredientListStr": None
                        },
                        {
                            "name": "AQUAFABA POWDER (MAYO PRODUCTION)",
                            "priority": 1,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDU2NTA=",
            "name": "aquafaba",
            "externalName": "Aquafaba (Chickpeas, Water)*",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.019861111093596607,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "TS48",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDU5MDM=",
            "name": "TS48 - 48oz Meal Boxes",
            "externalName": "48 oz Meal Boxes",
            "categoryValues": [
                {
                    "id": IngredientCategoryValueEnum.FOOD_PACKAGE.value,
                    "name": "food pkg",
                    "category": {
                        "id": IngredientCategoryTagTypeEnum.ACCOUNTING_TAG.value,
                        "name": "accounting group",
                        "itemType": "ingredient"
                    }
                }
            ]
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    }
                ],
                "quantity": 1,
                "unit": {
                    "id": UnitEnum.EACH.value,
                    "name": "each",
                    "unitValues": [
                        {
                            "value": 65.20390312999999,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 2.3,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 0.14374999987323417,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.EACH.value,
                                "name": "each"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "Meal Vegan - 2.75\" x 8\"",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDU5MjY=",
            "name": "label vegan meal",
            "externalName": "Vegan Meal Label",
            "categoryValues": [
                {
                    "id": IngredientCategoryValueEnum.FOOD_PACKAGE.value,
                    "name": "food pkg",
                    "category": {
                        "id": IngredientCategoryTagTypeEnum.ACCOUNTING_TAG.value,
                        "name": "accounting group",
                        "itemType": "ingredient"
                    }
                },
                {
                    "id": IngredientCategoryValueEnum.LABEL.value,
                    "name": "label",
                    "category": {
                        "id": "Y2F0ZWdvcnk6Mzc4Mg==",
                        "name": "packaging type",
                        "itemType": "ingredient"
                    }
                }
            ]
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    }
                ],
                "quantity": 1,
                "unit": {
                    "id": UnitEnum.EACH.value,
                    "name": "each",
                    "unitValues": [
                        {
                            "value": 2.8349523099999998e-05,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 1e-06,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 6.249999994488442e-08,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.EACH.value,
                                "name": "each"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "ORG., SPRING MIX & BABY KALE MIX 3#",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNDk1MzE=",
            "name": "spring mix & baby kale PF, SEND TO PLATE",
            "externalName": "Spring Mix Lettuce*, Kale* or Seasonal Greens*\u00a7",
            "categoryValues": [
                {
                    "id": "Y2F0ZWdvcnlWYWx1ZToxNDM5NQ==",
                    "name": "send to plate",
                    "category": {
                        "id": "Y2F0ZWdvcnk6MjUwMg==",
                        "name": "lead time",
                        "itemType": "ingredient"
                    }
                }
            ]
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 2.75,
                "unit": {
                    "id": UnitEnum.OZ.value,
                    "name": "oz",
                    "unitValues": [
                        {
                            "value": 28.3495231,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 0.06249999994488443,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        }
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "GRAINS, BUCKWHEAT GROATS IQF 40 LB",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyNTY1NzM=",
            "name": "grain, buckwheat groats, cooked IQF",
            "externalName": "Buckwheat Groats",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 0.1999999998236302,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                    ]
                }
            }
        ]
    },
    {
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "OIL, RICE BRAN, RBDW, 420# drum",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "aW5ncmVkaWVudDoyODI4NDI=",
            "name": "oil, rice bran",
            "externalName": "Rice Bran Oil",
            "categoryValues": []
        },
        "usages": [
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": STANDALONE_RECIPE_ID,
                        "name": STANDALONE_RECIPE_NAME
                    }
                ],
                "quantity": 0.061111111057220335,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                        {
                            "value": 0.002380952380952381,
                            "unit": {
                                "id": UnitEnum.EACH.value,
                                "name": "each"
                            }
                        }
                    ]
                }
            },
            {
                "ancestorRecipes": [
                    {
                        "id": SELLABLE_RECIPE_ID,
                        "name": SELLABLE_RECIPE_NAME
                    },
                    {
                        "id": "cmVjaXBlOjE3OTUzOQ==",
                        "name": "Rainbow Slaw Salad BASE"
                    }
                ],
                "quantity": 0.001041666665748074,
                "unit": {
                    "id": UnitEnum.LB.value,
                    "name": "lb",
                    "unitValues": [
                        {
                            "value": 453.59237,
                            "unit": {
                                "id": UnitEnum.G.value,
                                "name": "g"
                            }
                        },
                        {
                            "value": 16.000000014109585,
                            "unit": {
                                "id": UnitEnum.OZ.value,
                                "name": "oz"
                            }
                        },
                        {
                            "value": 1,
                            "unit": {
                                "id": UnitEnum.LB.value,
                                "name": "lb"
                            }
                        },
                        {
                            "value": 0.002380952380952381,
                            "unit": {
                                "id": UnitEnum.EACH.value,
                                "name": "each"
                            }
                        }
                    ]
                }
            }
        ]
    }
]


def MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_ONE_STANDALONE():
    mockRecipeItems = deepcopy(MOCK_RECIPE_ITEMS)
    ingredientsWithUsages = deepcopy(INGREDIENTS_WITH_USAGES)
    return {
        'recipeItems': mockRecipeItems,
        'ingredientsWithUsages': ingredientsWithUsages
    }


def MOCK_RECIPE_ITEMS_INGREDIENTS_WITH_USAGES_NO_STANDALONE():
    mockRecipeItems = [
        ri for ri in MOCK_RECIPE_ITEMS
        if all(
            prep['id'] != PreparationEnum.STANDALONE.value
            for prep in ri['preparations']
        )
    ]
    ingredientsWithUsages = [
        {**iu, 'usages': usages} for iu in INGREDIENTS_WITH_USAGES
        if (usages:= [
                usage for usage in iu['usages']
                if all(
                    recipe['id'] != STANDALONE_RECIPE_ID
                    for recipe in usage['ancestorRecipes']
                )
            ]
        )
    ]
    return {
        'recipeItems': mockRecipeItems,
        'ingredientsWithUsages': ingredientsWithUsages
    }
