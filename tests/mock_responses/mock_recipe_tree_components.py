from galley.enums import IngredientCategoryValueEnum, PreparationEnum


mock_recipe_tree_components_data = [
    {
        "id": "q3inld9o38n",
        "quantity": 6,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 170.0971386,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 6,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.3749999996693066,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.006249999994488443,
                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
            },
            {
                "value": 0.03749999996693066,
                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 6,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI3OA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI3OA==",
                "externalName": None,
                "name": "Brown Rice Pudding",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 27.2155422,
                                "unit": { "id": "dW5pdDoy", "name": "kg" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 113.3980924,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.2499999997795377,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MTY=",
                            "externalName": "Flax Seed*",
                            "name": "flax seed, meal"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 453.59237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 16.000000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 11,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4989.51607,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 176.00000015520544,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NzQ=",
                            "externalName": "Coconut Milk (Coconut, Water, Guar Gum)*",
                            "name": "milk, coconut"
                        }
                    },
                    {
                        "totalQuantity": 1.28,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 36.287389567999995,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.28,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.07999999992945206,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 1.12,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 508.0234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 17.920000015802735,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1.12,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    },
                    {
                        "totalQuantity": 0.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 17.00971386,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 0.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.03749999996693065,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3OTU=",
                            "externalName": "Cardamom",
                            "name": "spice, cardamom, ground"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 28.3495231,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.06249999994488443,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ4MDM=",
                            "externalName": "Cinnamon",
                            "name": "spice, cinnamon, ground"
                        }
                    },
                    {
                        "totalQuantity": 1.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 45.35923696,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.09999999991181507,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 48,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 21772.43376,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 768.0000006772601,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 48,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 11.2,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 5080.234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 179.20000015802734,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11.2,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDUyNjA=",
                            "externalName": "Sprouted Brown Rice",
                            "name": "rice, sprouted, brown, short-grain, dry"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wl870lsd6qd",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
            },
            {
                "value": 0.0046874999958663325,
                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4Mg==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4Mg==",
                "externalName": None,
                "name": "Pistachios & Toasted Coconut",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 8,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 3628.73896,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 128.00000011287668,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 8,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQzODA=",
                            "externalName": "Coconut Chips*",
                            "name": "coconut chips"
                        }
                    },
                    {
                        "totalQuantity": 18,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 8164.662660000001,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 288.00000025397253,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 18,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ2MjA=",
                            "externalName": "Pistachio Nuts*",
                            "name": "nuts, pistachio"
                        }
                    },
                    {
                        "totalQuantity": 14,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 6350.29318,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 224.00000019753418,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 14,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wq71ba1itv9",
        "quantity": 1.5,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 42.52428465,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.5,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.09374999991732665,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0015624999986221107,
                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
            },
            {
                "value": 0.009374999991732665,
                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 1.5,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [
                { "id": PreparationEnum.STANDALONE.value, "name": "standalone" },
                { "id": "cHJlcGFyYXRpb246MjgxMTU=", "name": "2 oz RAM" }
            ],
            "subRecipeId": "cmVjaXBlOjE3NDI3NQ==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NDI3NQ==",
                "externalName": None,
                "name": "Vanilla Cashew Cream",
                "reconciledNutritionals": {
                    'addedSugarG': 0,
                    'addedSugarPercentDRV': 0.0,
                    'calciumMg': 3.1684181569284497,
                    'calciumPercentRDI': 0.002,
                    'caloriesKCal': 53.66203631343362,
                    'carbsG': 5.931480844736274,
                    'carbsPercentDRV': 0.022,
                    'cholesterolMg': 0,
                    'cholesterolPercentDRV': None,
                    'copperMg': 0.021694334590068795,
                    'copperPercentRDI': 0.024,
                    'fiberG': 0.25925700237554117,
                    'fiberPercentDRV': 0.009,
                    'folateMcg': 4.662944286512987,
                    'folatePercentRDI': 0.012,
                    'ironMg': 0.08727603182928573,
                    'ironPercentRDI': 0.005,
                    'magnesiumMg': 8.422029852813752,
                    'magnesiumPercentRDI': 0.02,
                    'manganeseMg': 0.07968240957035716,
                    'manganesePercentRDI': 0.035,
                    'niacinMg': 0.6287359687622166,
                    'niacinPercentRDI': 0.039,
                    'pantothenicAcidMg': 0.06062563923716235,
                    'phosphorusMg': 16.6108569332684,
                    'phosphorusPercentRDI': 0.013,
                    'potassiumMg': 35.3618045624374,
                    'potassiumPercentRDI': 0.008,
                    'proteinG': 1.190862966668126,
                    'proteinPercentRDI': 0.024,
                    'riboflavinMg': 0.009900242547519483,
                    'riboflavinPercentRDI': 0.008,
                    'saturatedFatG': 1.1966419313881989,
                    'saturatedFatPercentDRV': 0.01840987586,
                    'seleniumMcg': 0.1983239364917749,
                    'seleniumPercentRDI': 0.004,
                    'sodiumMg': 80.1688699548479,
                    'sodiumPercentDRV': 0.035,
                    'sugarG': 4.635864789281829,
                    'sugarPercentDRV': None,
                    'thiaminMg': 0.008514061320616884,
                    'thiaminPercentRDI': 0.007,
                    'totalFatG': 3.2182500200225643,
                    'totalFatPercentDRV': 0.041,
                    'transFatG': 0.0035436903875000004,
                    'vitaminAMcg': 1.449295858309044,
                    'vitaminAPercentRDI': 0.002,
                    'vitaminB12Mcg': 0,
                    'vitaminB12PercentRDI': None,
                    'vitaminB6Mg': 0.022999931273467538,
                    'vitaminB6PercentRDI': 0.014,
                    'vitaminCMg': 1.7259736392050762,
                    'vitaminCPercentRDI': 0.019,
                    'vitaminDMcg': 0,
                    'vitaminDPercentRDI': None,
                    'vitaminEMg': 0.4437743529419914,
                    'vitaminEPercentRDI': 0.03,
                    'vitaminKMcg': 0.046390128709090914,
                    'vitaminKPercentRDI': 0,
                    'zincMg': 0.12343713881647085,
                    'zincPercentRDI': 0.011
                },
                "nutritionalsQuantity": 1.5,
                "nutritionalsUnit": { "id": "dW5pdDoz", "name": "oz" },
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1814.36948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 64.00000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1MzU=",
                            "externalName": "Lemon Juice",
                            "name": "juice, lemon"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NTA=",
                            "externalName": "Lemon Zest",
                            "name": "frozen, lemon zest"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 85.0485693,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.1874999998346533,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 25,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 11339.80925,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 400.0000003527396,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 25,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNjE1MTc=",
                            "externalName": "Oats",
                            "name": "milk, oat, powder"
                        }
                    },
                    {
                        "totalQuantity": 24,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 10886.21688,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 384.00000033863006,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 24,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyODgwOTM=",
                            "externalName": "Cashew",
                            "name": "milk base, cashew"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "7i687ntvow",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4MA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4MA==",
                "externalName": None,
                "name": "Dried Fruit - Golden Raisins & Blueberries",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 30,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 13607.7711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 480.00000042328753,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 30,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MDU=",
                            "externalName": "Golden Raisins",
                            "name": "dried fruit, golden raisins"
                        }
                    },
                    {
                        "totalQuantity": 10,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4535.9237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 160.00000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 10,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5Nzc=",
                            "externalName": "Dried Blueberries*",
                            "name": "dried fruit, blueberries"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "6yo53kbon0m",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 32.60195156499999,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.15,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.07187499993661708,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "TS20 - 20oz Meal Boxes",
                "externalName": "TS20",
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
    },
    {
        "id": "ob0rleghe",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 2.83495231,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.1,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.006249999994488443,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            },
            {
                "value": 0.0005,
                "unit": { "id": "dW5pdDo3ODA1MjM=", "name": "case" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "RAM2 - 2 oz Portion Cups",
                "externalName": "2 oz Portion Cups",
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
    }
]

mock_recipe_tree_components_data_no_pkg_no_standalone = [
    {
        "id": "q3inld9o38n",
        "quantity": 6,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 170.0971386,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 6,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.3749999996693066,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.006249999994488443,
                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
            },
            {
                "value": 0.03749999996693066,
                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 6,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI3OA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI3OA==",
                "externalName": None,
                "name": "Brown Rice Pudding",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 27.2155422,
                                "unit": { "id": "dW5pdDoy", "name": "kg" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 113.3980924,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.2499999997795377,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MTY=",
                            "externalName": "Flax Seed*",
                            "name": "flax seed, meal"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 453.59237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 16.000000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 11,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4989.51607,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 176.00000015520544,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NzQ=",
                            "externalName": "Coconut Milk (Coconut, Water, Guar Gum)*",
                            "name": "milk, coconut"
                        }
                    },
                    {
                        "totalQuantity": 1.28,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 36.287389567999995,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.28,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.07999999992945206,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 1.12,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 508.0234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 17.920000015802735,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1.12,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    },
                    {
                        "totalQuantity": 0.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 17.00971386,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 0.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.03749999996693065,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3OTU=",
                            "externalName": "Cardamom",
                            "name": "spice, cardamom, ground"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 28.3495231,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.06249999994488443,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ4MDM=",
                            "externalName": "Cinnamon",
                            "name": "spice, cinnamon, ground"
                        }
                    },
                    {
                        "totalQuantity": 1.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 45.35923696,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.09999999991181507,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 48,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 21772.43376,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 768.0000006772601,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 48,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 11.2,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 5080.234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 179.20000015802734,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11.2,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDUyNjA=",
                            "externalName": "Sprouted Brown Rice",
                            "name": "rice, sprouted, brown, short-grain, dry"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wl870lsd6qd",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
            },
            {
                "value": 0.0046874999958663325,
                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4Mg==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4Mg==",
                "externalName": None,
                "name": "Pistachios & Toasted Coconut",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 8,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 3628.73896,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 128.00000011287668,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 8,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQzODA=",
                            "externalName": "Coconut Chips*",
                            "name": "coconut chips"
                        }
                    },
                    {
                        "totalQuantity": 18,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 8164.662660000001,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 288.00000025397253,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 18,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ2MjA=",
                            "externalName": "Pistachio Nuts*",
                            "name": "nuts, pistachio"
                        }
                    },
                    {
                        "totalQuantity": 14,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 6350.29318,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 224.00000019753418,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 14,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wq71ba1itv9",
        "quantity": 1.5,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 42.52428465,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.5,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.09374999991732665,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0015624999986221107,
                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
            },
            {
                "value": 0.009374999991732665,
                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 1.5,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE3NDI3NQ==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NDI3NQ==",
                "externalName": None,
                "name": "Vanilla Cashew Cream",
                "nutritionalsQuantity": 1.5,
                "nutritionalsUnit": { "id": "dW5pdDoz", "name": "oz" },
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1814.36948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 64.00000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1MzU=",
                            "externalName": "Lemon Juice",
                            "name": "juice, lemon"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NTA=",
                            "externalName": "Lemon Zest",
                            "name": "frozen, lemon zest"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 85.0485693,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.1874999998346533,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 25,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 11339.80925,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 400.0000003527396,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 25,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNjE1MTc=",
                            "externalName": "Oats",
                            "name": "milk, oat, powder"
                        }
                    },
                    {
                        "totalQuantity": 24,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 10886.21688,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 384.00000033863006,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 24,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyODgwOTM=",
                            "externalName": "Cashew",
                            "name": "milk base, cashew"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "7i687ntvow",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4MA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4MA==",
                "externalName": None,
                "name": "Dried Fruit - Golden Raisins & Blueberries",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 30,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 13607.7711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 480.00000042328753,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 30,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MDU=",
                            "externalName": "Golden Raisins",
                            "name": "dried fruit, golden raisins"
                        }
                    },
                    {
                        "totalQuantity": 10,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4535.9237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 160.00000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 10,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5Nzc=",
                            "externalName": "Dried Blueberries*",
                            "name": "dried fruit, blueberries"
                        }
                    }
                ]
            }
        }
    },
    {
        'quantityUnitValues': [],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    }
]

mock_recipe_tree_components_data_with_multiple_servings_of_standalone = [
    {
        "id": "q3inld9o38n",
        "quantity": 1,
        "unit": { "id": "dW5pdDoz", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 170.0971386,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 6,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.3749999996693066,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoz", "name": "each" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI3OA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI3OA==",
                "externalName": None,
                "name": "Brown Rice Pudding",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 27.2155422,
                                "unit": { "id": "dW5pdDoy", "name": "kg" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 113.3980924,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.2499999997795377,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MTY=",
                            "externalName": "Flax Seed*",
                            "name": "flax seed, meal"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 453.59237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 16.000000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 11,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4989.51607,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 176.00000015520544,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NzQ=",
                            "externalName": "Coconut Milk (Coconut, Water, Guar Gum)*",
                            "name": "milk, coconut"
                        }
                    },
                    {
                        "totalQuantity": 1.28,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 36.287389567999995,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.28,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.07999999992945206,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 1.12,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 508.0234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 17.920000015802735,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1.12,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    },
                    {
                        "totalQuantity": 0.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 17.00971386,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 0.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.03749999996693065,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3OTU=",
                            "externalName": "Cardamom",
                            "name": "spice, cardamom, ground"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 28.3495231,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.06249999994488443,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ4MDM=",
                            "externalName": "Cinnamon",
                            "name": "spice, cinnamon, ground"
                        }
                    },
                    {
                        "totalQuantity": 1.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 45.35923696,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.09999999991181507,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 48,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 21772.43376,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 768.0000006772601,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 48,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 11.2,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 5080.234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 179.20000015802734,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11.2,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDUyNjA=",
                            "externalName": "Sprouted Brown Rice",
                            "name": "rice, sprouted, brown, short-grain, dry"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wl870lsd6qd",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
            },
            {
                "value": 0.0046874999958663325,
                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4Mg==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4Mg==",
                "externalName": None,
                "name": "Pistachios & Toasted Coconut",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 8,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 3628.73896,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 128.00000011287668,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 8,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQzODA=",
                            "externalName": "Coconut Chips*",
                            "name": "coconut chips"
                        }
                    },
                    {
                        "totalQuantity": 18,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 8164.662660000001,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 288.00000025397253,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 18,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ2MjA=",
                            "externalName": "Pistachio Nuts*",
                            "name": "nuts, pistachio"
                        }
                    },
                    {
                        "totalQuantity": 14,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 6350.29318,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 224.00000019753418,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 14,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wq71ba1itv9",
        "quantity": 1.5,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 42.52428465,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.5,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.09374999991732665,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0015624999986221107,
                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
            },
            {
                "value": 0.009374999991732665,
                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 1.5,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [
                { "id": PreparationEnum.STANDALONE.value, "name": "standalone" },
                { "id": "cHJlcGFyYXRpb246MjgxMTU=", "name": "2 oz RAM" }
            ],
            "subRecipeId": "cmVjaXBlOjE3NDI3NQ==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NDI3NQ==",
                "externalName": None,
                "name": "Vanilla Cashew Cream",
                "reconciledNutritionals": {
                    'addedSugarG': 0,
                    'addedSugarPercentDRV': 0.0,
                    'calciumMg': 3.1684181569284497,
                    'calciumPercentRDI': 0.002,
                    'caloriesKCal': 53.66203631343362,
                    'carbsG': 5.931480844736274,
                    'carbsPercentDRV': 0.022,
                    'cholesterolMg': 0,
                    'cholesterolPercentDRV': None,
                    'copperMg': 0.021694334590068795,
                    'copperPercentRDI': 0.024,
                    'fiberG': 0.25925700237554117,
                    'fiberPercentDRV': 0.009,
                    'folateMcg': 4.662944286512987,
                    'folatePercentRDI': 0.012,
                    'ironMg': 0.08727603182928573,
                    'ironPercentRDI': 0.005,
                    'magnesiumMg': 8.422029852813752,
                    'magnesiumPercentRDI': 0.02,
                    'manganeseMg': 0.07968240957035716,
                    'manganesePercentRDI': 0.035,
                    'niacinMg': 0.6287359687622166,
                    'niacinPercentRDI': 0.039,
                    'pantothenicAcidMg': 0.06062563923716235,
                    'phosphorusMg': 16.6108569332684,
                    'phosphorusPercentRDI': 0.013,
                    'potassiumMg': 35.3618045624374,
                    'potassiumPercentRDI': 0.008,
                    'proteinG': 1.190862966668126,
                    'proteinPercentRDI': 0.024,
                    'riboflavinMg': 0.009900242547519483,
                    'riboflavinPercentRDI': 0.008,
                    'saturatedFatG': 1.1966419313881989,
                    'saturatedFatPercentDRV': 0.01840987586,
                    'seleniumMcg': 0.1983239364917749,
                    'seleniumPercentRDI': 0.004,
                    'sodiumMg': 80.1688699548479,
                    'sodiumPercentDRV': 0.035,
                    'sugarG': 4.635864789281829,
                    'sugarPercentDRV': None,
                    'thiaminMg': 0.008514061320616884,
                    'thiaminPercentRDI': 0.007,
                    'totalFatG': 3.2182500200225643,
                    'totalFatPercentDRV': 0.041,
                    'transFatG': 0.0035436903875000004,
                    'vitaminAMcg': 1.449295858309044,
                    'vitaminAPercentRDI': 0.002,
                    'vitaminB12Mcg': 0,
                    'vitaminB12PercentRDI': None,
                    'vitaminB6Mg': 0.022999931273467538,
                    'vitaminB6PercentRDI': 0.014,
                    'vitaminCMg': 1.7259736392050762,
                    'vitaminCPercentRDI': 0.019,
                    'vitaminDMcg': 0,
                    'vitaminDPercentRDI': None,
                    'vitaminEMg': 0.4437743529419914,
                    'vitaminEPercentRDI': 0.03,
                    'vitaminKMcg': 0.046390128709090914,
                    'vitaminKPercentRDI': 0,
                    'zincMg': 0.12343713881647085,
                    'zincPercentRDI': 0.011
                },
                "nutritionalsQuantity": 0.75,
                "nutritionalsUnit": { "id": "dW5pdDoz", "name": "oz" },
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1814.36948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 64.00000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1MzU=",
                            "externalName": "Lemon Juice",
                            "name": "juice, lemon"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NTA=",
                            "externalName": "Lemon Zest",
                            "name": "frozen, lemon zest"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 85.0485693,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.1874999998346533,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 25,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 11339.80925,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 400.0000003527396,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 25,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNjE1MTc=",
                            "externalName": "Oats",
                            "name": "milk, oat, powder"
                        }
                    },
                    {
                        "totalQuantity": 24,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 10886.21688,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 384.00000033863006,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 24,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyODgwOTM=",
                            "externalName": "Cashew",
                            "name": "milk base, cashew"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "7i687ntvow",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4MA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4MA==",
                "externalName": None,
                "name": "Dried Fruit - Golden Raisins & Blueberries",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 30,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 13607.7711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 480.00000042328753,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 30,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MDU=",
                            "externalName": "Golden Raisins",
                            "name": "dried fruit, golden raisins"
                        }
                    },
                    {
                        "totalQuantity": 10,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4535.9237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 160.00000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 10,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5Nzc=",
                            "externalName": "Dried Blueberries*",
                            "name": "dried fruit, blueberries"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "6yo53kbon0m",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 32.60195156499999,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.15,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.07187499993661708,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "TS20 - 20oz Meal Boxes",
                "externalName": "TS20",
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
    },
    {
        "id": "ob0rleghe",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 2.83495231,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.1,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.006249999994488443,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            },
            {
                "value": 0.0005,
                "unit": { "id": "dW5pdDo3ODA1MjM=", "name": "case" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "RAM2 - 2 oz Portion Cups",
                "externalName": "2 oz Portion Cups",
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
    }
]

mock_recipe_tree_components_data_with_one_serving_of_standalone = [
    {
        "id": "q3inld9o38n",
        "quantity": 1,
        "unit": { "id": "dW5pdDoz", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 170.0971386,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 6,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.3749999996693066,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoz", "name": "each" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI3OA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI3OA==",
                "externalName": None,
                "name": "Brown Rice Pudding",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 27.2155422,
                                "unit": { "id": "dW5pdDoy", "name": "kg" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 113.3980924,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.2499999997795377,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MTY=",
                            "externalName": "Flax Seed*",
                            "name": "flax seed, meal"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 453.59237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 16.000000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 11,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4989.51607,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 176.00000015520544,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NzQ=",
                            "externalName": "Coconut Milk (Coconut, Water, Guar Gum)*",
                            "name": "milk, coconut"
                        }
                    },
                    {
                        "totalQuantity": 1.28,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 36.287389567999995,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.28,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.07999999992945206,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 1.12,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 508.0234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 17.920000015802735,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1.12,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    },
                    {
                        "totalQuantity": 0.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 17.00971386,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 0.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.03749999996693065,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3OTU=",
                            "externalName": "Cardamom",
                            "name": "spice, cardamom, ground"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 28.3495231,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.06249999994488443,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ4MDM=",
                            "externalName": "Cinnamon",
                            "name": "spice, cinnamon, ground"
                        }
                    },
                    {
                        "totalQuantity": 1.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 45.35923696,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.09999999991181507,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 48,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 21772.43376,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 768.0000006772601,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 48,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 11.2,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 5080.234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 179.20000015802734,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11.2,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDUyNjA=",
                            "externalName": "Sprouted Brown Rice",
                            "name": "rice, sprouted, brown, short-grain, dry"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wl870lsd6qd",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
            },
            {
                "value": 0.0046874999958663325,
                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4Mg==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4Mg==",
                "externalName": None,
                "name": "Pistachios & Toasted Coconut",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 8,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 3628.73896,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 128.00000011287668,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 8,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQzODA=",
                            "externalName": "Coconut Chips*",
                            "name": "coconut chips"
                        }
                    },
                    {
                        "totalQuantity": 18,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 8164.662660000001,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 288.00000025397253,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 18,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ2MjA=",
                            "externalName": "Pistachio Nuts*",
                            "name": "nuts, pistachio"
                        }
                    },
                    {
                        "totalQuantity": 14,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 6350.29318,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 224.00000019753418,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 14,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wq71ba1itv9",
        "quantity": 1.5,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 42.52428465,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.5,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.09374999991732665,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0015624999986221107,
                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
            },
            {
                "value": 0.009374999991732665,
                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 1.5,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [
                { "id": PreparationEnum.STANDALONE.value, "name": "standalone" },
                { "id": "cHJlcGFyYXRpb246MjgxMTU=", "name": "2 oz RAM" }
            ],
            "subRecipeId": "cmVjaXBlOjE3NDI3NQ==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NDI3NQ==",
                "externalName": None,
                "name": "Vanilla Cashew Cream",
                "reconciledNutritionals": {
                    'addedSugarG': 0,
                    'addedSugarPercentDRV': 0.0,
                    'calciumMg': 3.1684181569284497,
                    'calciumPercentRDI': 0.002,
                    'caloriesKCal': 53.66203631343362,
                    'carbsG': 5.931480844736274,
                    'carbsPercentDRV': 0.022,
                    'cholesterolMg': 0,
                    'cholesterolPercentDRV': None,
                    'copperMg': 0.021694334590068795,
                    'copperPercentRDI': 0.024,
                    'fiberG': 0.25925700237554117,
                    'fiberPercentDRV': 0.009,
                    'folateMcg': 4.662944286512987,
                    'folatePercentRDI': 0.012,
                    'ironMg': 0.08727603182928573,
                    'ironPercentRDI': 0.005,
                    'magnesiumMg': 8.422029852813752,
                    'magnesiumPercentRDI': 0.02,
                    'manganeseMg': 0.07968240957035716,
                    'manganesePercentRDI': 0.035,
                    'niacinMg': 0.6287359687622166,
                    'niacinPercentRDI': 0.039,
                    'pantothenicAcidMg': 0.06062563923716235,
                    'phosphorusMg': 16.6108569332684,
                    'phosphorusPercentRDI': 0.013,
                    'potassiumMg': 35.3618045624374,
                    'potassiumPercentRDI': 0.008,
                    'proteinG': 1.190862966668126,
                    'proteinPercentRDI': 0.024,
                    'riboflavinMg': 0.009900242547519483,
                    'riboflavinPercentRDI': 0.008,
                    'saturatedFatG': 1.1966419313881989,
                    'saturatedFatPercentDRV': 0.01840987586,
                    'seleniumMcg': 0.1983239364917749,
                    'seleniumPercentRDI': 0.004,
                    'sodiumMg': 80.1688699548479,
                    'sodiumPercentDRV': 0.035,
                    'sugarG': 4.635864789281829,
                    'sugarPercentDRV': None,
                    'thiaminMg': 0.008514061320616884,
                    'thiaminPercentRDI': 0.007,
                    'totalFatG': 3.2182500200225643,
                    'totalFatPercentDRV': 0.041,
                    'transFatG': 0.0035436903875000004,
                    'vitaminAMcg': 1.449295858309044,
                    'vitaminAPercentRDI': 0.002,
                    'vitaminB12Mcg': 0,
                    'vitaminB12PercentRDI': None,
                    'vitaminB6Mg': 0.022999931273467538,
                    'vitaminB6PercentRDI': 0.014,
                    'vitaminCMg': 1.7259736392050762,
                    'vitaminCPercentRDI': 0.019,
                    'vitaminDMcg': 0,
                    'vitaminDPercentRDI': None,
                    'vitaminEMg': 0.4437743529419914,
                    'vitaminEPercentRDI': 0.03,
                    'vitaminKMcg': 0.046390128709090914,
                    'vitaminKPercentRDI': 0,
                    'zincMg': 0.12343713881647085,
                    'zincPercentRDI': 0.011
                },
                "nutritionalsQuantity": 1.5,
                "nutritionalsUnit": { "id": "dW5pdDoz", "name": "oz" },
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1814.36948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 64.00000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1MzU=",
                            "externalName": "Lemon Juice",
                            "name": "juice, lemon"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NTA=",
                            "externalName": "Lemon Zest",
                            "name": "frozen, lemon zest"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 85.0485693,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.1874999998346533,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 25,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 11339.80925,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 400.0000003527396,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 25,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNjE1MTc=",
                            "externalName": "Oats",
                            "name": "milk, oat, powder"
                        }
                    },
                    {
                        "totalQuantity": 24,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 10886.21688,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 384.00000033863006,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 24,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyODgwOTM=",
                            "externalName": "Cashew",
                            "name": "milk base, cashew"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "7i687ntvow",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4MA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4MA==",
                "externalName": None,
                "name": "Dried Fruit - Golden Raisins & Blueberries",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 30,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 13607.7711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 480.00000042328753,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 30,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MDU=",
                            "externalName": "Golden Raisins",
                            "name": "dried fruit, golden raisins"
                        }
                    },
                    {
                        "totalQuantity": 10,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4535.9237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 160.00000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 10,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5Nzc=",
                            "externalName": "Dried Blueberries*",
                            "name": "dried fruit, blueberries"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "6yo53kbon0m",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 32.60195156499999,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.15,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.07187499993661708,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "TS20 - 20oz Meal Boxes",
                "externalName": "TS20",
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
    },
    {
        "id": "ob0rleghe",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 2.83495231,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.1,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.006249999994488443,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            },
            {
                "value": 0.0005,
                "unit": { "id": "dW5pdDo3ODA1MjM=", "name": "case" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "RAM2 - 2 oz Portion Cups",
                "externalName": "2 oz Portion Cups",
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
    }
]

mock_recipe_tree_components_data_with_standalone_missing_nutritionals_quantity_data = [
    {
        "id": "q3inld9o38n",
        "quantity": 6,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 170.0971386,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 6,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.3749999996693066,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.006249999994488443,
                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
            },
            {
                "value": 0.03749999996693066,
                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 6,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI3OA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI3OA==",
                "externalName": None,
                "name": "Brown Rice Pudding",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 27.2155422,
                                "unit": { "id": "dW5pdDoy", "name": "kg" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ2OTU=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ2OTY=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 113.3980924,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.2499999997795377,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MTY=",
                            "externalName": "Flax Seed*",
                            "name": "flax seed, meal"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 453.59237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 16.000000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 11,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4989.51607,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 176.00000015520544,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NzQ=",
                            "externalName": "Coconut Milk (Coconut, Water, Guar Gum)*",
                            "name": "milk, coconut"
                        }
                    },
                    {
                        "totalQuantity": 1.28,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 36.287389567999995,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.28,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.07999999992945206,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 1.12,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 508.0234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 17.920000015802735,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 1.12,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    },
                    {
                        "totalQuantity": 0.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 17.00971386,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 0.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.03749999996693065,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3OTU=",
                            "externalName": "Cardamom",
                            "name": "spice, cardamom, ground"
                        }
                    },
                    {
                        "totalQuantity": 1,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 28.3495231,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.06249999994488443,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ4MDM=",
                            "externalName": "Cinnamon",
                            "name": "spice, cinnamon, ground"
                        }
                    },
                    {
                        "totalQuantity": 1.6,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 45.35923696,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 1.6,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.09999999991181507,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 48,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 21772.43376,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 768.0000006772601,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 48,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 11.2,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 5080.234544,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 179.20000015802734,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 11.2,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDUyNjA=",
                            "externalName": "Sprouted Brown Rice",
                            "name": "rice, sprouted, brown, short-grain, dry"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wl870lsd6qd",
        "quantity": 0.75,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0011718749989665831,
                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
            },
            {
                "value": 0.0046874999958663325,
                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 0.75,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4Mg==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4Mg==",
                "externalName": None,
                "name": "Pistachios & Toasted Coconut",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDU=", "name": "max batch" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo5MjQ3MDc=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 8,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 3628.73896,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 128.00000011287668,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 8,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQzODA=",
                            "externalName": "Coconut Chips*",
                            "name": "coconut chips"
                        }
                    },
                    {
                        "totalQuantity": 18,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 8164.662660000001,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 288.00000025397253,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 18,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ2MjA=",
                            "externalName": "Pistachio Nuts*",
                            "name": "nuts, pistachio"
                        }
                    },
                    {
                        "totalQuantity": 14,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 6350.29318,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 224.00000019753418,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 14,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3Nzg=",
                            "externalName": "Hemp Seeds",
                            "name": "seeds, hemp"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "wq71ba1itv9",
        "quantity": 1.5,
        "unit": { "id": "dW5pdDoz", "name": "oz" },
        "quantityUnitValues": [
            {
                "value": 42.52428465,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.5,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.09374999991732665,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 0.0015624999986221107,
                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
            },
            {
                "value": 0.009374999991732665,
                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
            }
        ],
        "recipeItem": {
            "quantity": 1.5,
            "unit": { "id": "dW5pdDoz", "name": "oz" },
            "preparations": [
                { "id": PreparationEnum.STANDALONE.value, "name": "standalone" },
                { "id": "cHJlcGFyYXRpb246MjgxMTU=", "name": "2 oz RAM" }
            ],
            "subRecipeId": "cmVjaXBlOjE3NDI3NQ==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NDI3NQ==",
                "externalName": None,
                "name": "Vanilla Cashew Cream",
                "reconciledNutritionals": {
                    'addedSugarG': 0,
                    'addedSugarPercentDRV': 0.0,
                    'calciumMg': 3.1684181569284497,
                    'calciumPercentRDI': 0.002,
                    'caloriesKCal': 53.66203631343362,
                    'carbsG': 5.931480844736274,
                    'carbsPercentDRV': 0.022,
                    'cholesterolMg': 0,
                    'cholesterolPercentDRV': None,
                    'copperMg': 0.021694334590068795,
                    'copperPercentRDI': 0.024,
                    'fiberG': 0.25925700237554117,
                    'fiberPercentDRV': 0.009,
                    'folateMcg': 4.662944286512987,
                    'folatePercentRDI': 0.012,
                    'ironMg': 0.08727603182928573,
                    'ironPercentRDI': 0.005,
                    'magnesiumMg': 8.422029852813752,
                    'magnesiumPercentRDI': 0.02,
                    'manganeseMg': 0.07968240957035716,
                    'manganesePercentRDI': 0.035,
                    'niacinMg': 0.6287359687622166,
                    'niacinPercentRDI': 0.039,
                    'pantothenicAcidMg': 0.06062563923716235,
                    'phosphorusMg': 16.6108569332684,
                    'phosphorusPercentRDI': 0.013,
                    'potassiumMg': 35.3618045624374,
                    'potassiumPercentRDI': 0.008,
                    'proteinG': 1.190862966668126,
                    'proteinPercentRDI': 0.024,
                    'riboflavinMg': 0.009900242547519483,
                    'riboflavinPercentRDI': 0.008,
                    'saturatedFatG': 1.1966419313881989,
                    'saturatedFatPercentDRV': 0.01840987586,
                    'seleniumMcg': 0.1983239364917749,
                    'seleniumPercentRDI': 0.004,
                    'sodiumMg': 80.1688699548479,
                    'sodiumPercentDRV': 0.035,
                    'sugarG': 4.635864789281829,
                    'sugarPercentDRV': None,
                    'thiaminMg': 0.008514061320616884,
                    'thiaminPercentRDI': 0.007,
                    'totalFatG': 3.2182500200225643,
                    'totalFatPercentDRV': 0.041,
                    'transFatG': 0.0035436903875000004,
                    'vitaminAMcg': 1.449295858309044,
                    'vitaminAPercentRDI': 0.002,
                    'vitaminB12Mcg': 0,
                    'vitaminB12PercentRDI': None,
                    'vitaminB6Mg': 0.022999931273467538,
                    'vitaminB6PercentRDI': 0.014,
                    'vitaminCMg': 1.7259736392050762,
                    'vitaminCPercentRDI': 0.019,
                    'vitaminDMcg': 0,
                    'vitaminDPercentRDI': None,
                    'vitaminEMg': 0.4437743529419914,
                    'vitaminEPercentRDI': 0.03,
                    'vitaminKMcg': 0.046390128709090914,
                    'vitaminKPercentRDI': 0,
                    'zincMg': 0.12343713881647085,
                    'zincPercentRDI': 0.011
                },
                "recipeTreeComponents": [
                    {
                        "quantity": 60,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 27215.5422,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 960.0000008465751,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 60,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDk=", "name": "max batch" }
                            },
                            {
                                "value": 6,
                                "unit": { "id": "dW5pdDo5MjQ3MTI=", "name": "min batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 4,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1814.36948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 64.00000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 4,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1MzU=",
                            "externalName": "Lemon Juice",
                            "name": "juice, lemon"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NTA=",
                            "externalName": "Lemon Zest",
                            "name": "frozen, lemon zest"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ1NjY=",
                            "externalName": "Maple Syrup*",
                            "name": "maple syrup"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 85.0485693,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.1874999998346533,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ3NjQ=",
                            "externalName": "Sea Salt",
                            "name": "salt, sea"
                        }
                    },
                    {
                        "totalQuantity": 12,
                        "unit": { "id": "dW5pdDoz", "name": "oz" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 340.1942772,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 12,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 0.7499999993386132,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MDM=",
                            "externalName": "Vanilla Extract*",
                            "name": "vanilla extract"
                        }
                    },
                    {
                        "totalQuantity": 25,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 11339.80925,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 400.0000003527396,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 25,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5MTk=",
                            "externalName": "Water",
                            "name": "water"
                        }
                    },
                    {
                        "totalQuantity": 3,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 1360.77711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 48.00000004232876,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 3,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNjE1MTc=",
                            "externalName": "Oats",
                            "name": "milk, oat, powder"
                        }
                    },
                    {
                        "totalQuantity": 24,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 10886.21688,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 384.00000033863006,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 24,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyODgwOTM=",
                            "externalName": "Cashew",
                            "name": "milk base, cashew"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "7i687ntvow",
        "quantity": 1,
        "unit": { "id": "dW5pdDoz", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 21.262142325,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.75,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.04687499995866332,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoz", "name": "each" },
            "preparations": [],
            "subRecipeId": "cmVjaXBlOjE4NjI4MA==",
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NjI4MA==",
                "externalName": None,
                "name": "Dried Fruit - Golden Raisins & Blueberries",
                "nutritionalsQuantity": None,
                "nutritionalsUnit": None,
                "recipeTreeComponents": [
                    {
                        "quantity": 40,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "quantityUnitValues": [
                            {
                                "value": 18143.6948,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 640.0000005643834,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 40,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            },
                            {
                                "value": 1,
                                "unit": { "id": "dW5pdDo5MjQ3MDI=", "name": "max batch" }
                            }
                        ]
                    }
                ],
                "allIngredientsWithUsages": [
                    {
                        "totalQuantity": 30,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 13607.7711,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 480.00000042328753,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 30,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ0MDU=",
                            "externalName": "Golden Raisins",
                            "name": "dried fruit, golden raisins"
                        }
                    },
                    {
                        "totalQuantity": 10,
                        "unit": { "id": "dW5pdDo0", "name": "lb" },
                        "totalQuantityUnitValues": [
                            {
                                "value": 4535.9237,
                                "unit": { "id": "dW5pdDox", "name": "g" }
                            },
                            {
                                "value": 160.00000014109585,
                                "unit": { "id": "dW5pdDoz", "name": "oz" }
                            },
                            {
                                "value": 10,
                                "unit": { "id": "dW5pdDo0", "name": "lb" }
                            }
                        ],
                        "ingredient": {
                            "id": "aW5ncmVkaWVudDoyNDQ5Nzc=",
                            "externalName": "Dried Blueberries*",
                            "name": "dried fruit, blueberries"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "6yo53kbon0m",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 32.60195156499999,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 1.15,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.07187499993661708,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "TS20 - 20oz Meal Boxes",
                "externalName": "TS20",
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
    },
    {
        "id": "ob0rleghe",
        "quantity": 1,
        "unit": { "id": "dW5pdDoxNA==", "name": "each" },
        "quantityUnitValues": [
            {
                "value": 2.83495231,
                "unit": { "id": "dW5pdDox", "name": "g" }
            },
            {
                "value": 0.1,
                "unit": { "id": "dW5pdDoz", "name": "oz" }
            },
            {
                "value": 0.006249999994488443,
                "unit": { "id": "dW5pdDo0", "name": "lb" }
            },
            {
                "value": 1,
                "unit": { "id": "dW5pdDoxNA==", "name": "each" }
            },
            {
                "value": 0.0005,
                "unit": { "id": "dW5pdDo3ODA1MjM=", "name": "case" }
            }
        ],
        "recipeItem": {
            "quantity": 1,
            "unit": { "id": "dW5pdDoxNA==", "name": "each" },
            "preparations": [],
            "subRecipeId": None,
            "ingredient": {
                "name": "RAM2 - 2 oz Portion Cups",
                "externalName": "2 oz Portion Cups",
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
    }
]
