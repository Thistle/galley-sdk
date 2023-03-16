from galley.enums import PreparationEnum, UnitEnum
from tests.mock_responses.mock_nutrition_data import MOCK_RECONCILED_NUTRITIONALS

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
        "ingredient": None,
        "subRecipe": {
            "id": "RECIPE123ABC",
            "name": "Example Base Recipe",
            "externalName": None,
            "nutritionalsQuantity": None,
            "nutritionalsUnit": None,
            "reconciledNutritionals": MOCK_RECONCILED_NUTRITIONALS,
        }
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [
            {
                "id": PreparationEnum.STANDALONE.value,
                "name": "standalone"
            },
            {
                "id": PreparationEnum.TWO_OZ_RAM.value,
                "name": "2 oz RAM"
            }
        ],
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
        "ingredient": None,
        "subRecipe": {
            "id": "SUBRECIPE123ABC",
            "name": "test subrecipe",
            "externalName": "Test Subrecipe",
            "nutritionalsQuantity": 2.0,
            "nutritionalsUnit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "reconciledNutritionals": MOCK_RECONCILED_NUTRITIONALS
        },
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [],
        "quantity": 0.5,
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
        },
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "SPRING LETTUCE MIX 3#",
                            "priority": 0,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "INGREDIENT123ABC",
            "name": "lettuce, shredded, SEND TO PLATE",
            "externalName": "Lettuce",
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
        "subRecipe": None
    },
    {
        "recipeId": "SELLABLE123ABC",
        "preparations": [],
        "quantity": 1,
        "unit": {
            "id": "dW5pdDoxNA==",
            "name": "each",
            "unitValues": [
                {
                    "value": 5.66990462,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 0.2,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.012499999988976886,
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
        "ingredient": {
            "locationVendorItems": [
                {
                    "vendorItems": [
                        {
                            "name": "GXL345PC Clear PLA Portion Cup Lids",
                            "priority": 0,
                            "ingredientListStr": None
                        },
                        {
                            "name": "RAM3/RAM4 Lid Portion Cup Lids",
                            "priority": 1,
                            "ingredientListStr": None
                        }
                    ]
                }
            ],
            "id": "INGREDIENT456ABC",
            "name": "lid, portion cup, 3 oz",
            "externalName": "Lid, Portion Cup, 3 oz",
            "categoryValues": [
                {
                    "id": "Y2F0ZWdvcnlWYWx1ZToxNDAxNQ==",
                    "name": "food pkg",
                    "category": {
                        "id": "Y2F0ZWdvcnk6MjQyMA==",
                        "name": "accounting group",
                        "itemType": "ingredient"
                    }
                }
            ]
        },
        "subRecipe": None
    }
]
