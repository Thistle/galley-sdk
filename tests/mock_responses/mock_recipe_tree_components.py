from galley.enums import PreparationEnum


mock_data = [
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': [
                {
                    'name': '2 oz RAM'
                },
                {
                    'id': PreparationEnum.STANDALONE.value,
                    'name': 'standalone'
                }
            ]
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': {
                'categoryValues': [
                    {
                        'id': 'Y2F0ZWdvcnlWYWx1ZToxNDAxNQ==',
                        'name': 'food pkg',
                        'category': {
                            'id': "Y2F0ZWdvcnk6MjQyMA==",
                            'name': "category",
                            'itemType': 'ingredient'
                        }
                    }
                ],
                'externalName': '48 oz Meal Boxes'
            },
            'preparations': []
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

mock_data_no_pkg_no_standalone = [
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
        }
    },
    {
        'quantityUnitValues': [
            {
                'unit': {
                    'name': 'g'
                },
                'value': 276.40785022499995
            },
            {
                'unit': {
                    'name': 'kg'
                },
                'value': 0.276407850225
            },
            {
                'unit': {
                    'name': 'oz'
                },
                'value': 9.75
            },
            {
                'unit': {
                    'name': 'lb'
                },
                'value': 0.6093749994626232
            },
            {
                'unit': {
                    'name': 'each'
                },
                'value': 1
            }
        ],
        'recipeItem': {
            'ingredient': None,
            'preparations': []
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

mock_data_standalone_recipe_item = [
    {
        "quantityUnitValues": [
            {
                "unit": {
                    "id": "dW5pdDoxNA==",
                    "name": "each"
                },
                "value": 1
            }
        ],
        "id": "l7n5ecjjdyd",
              "ingredient": None,
              "recipeItem": {
                  "subRecipeId": "cmVjaXBlOjE3MDM5Mw==",
            "subRecipe": {
                "id": "cmVjaXBlOjE3MDM5Mw==",
                "name": "Balinese Gado Gado Salad BASE",
                        "externalName": None,
                        "allIngredients": [
                            "Baby Spinach",
                            "Green Beans",
                            "Cucumber",
                            "Shredded Rainbow Carrots",
                            "Cabbage",
                            "Lemon Zest",
                            "Himalayan Pink Salt"
                        ],
                "reconciledNutritionals": {
                            "addedSugarG": 0,
                            "calciumMg": 130.9257425805093,
                            "calciumPercentRDI": 0.101,
                            "caloriesKCal": 62.0924415065955,
                            "carbsG": 12.988484501763947,
                            "carbsPercentDRV": 0.047,
                            "cholesterolMg": 0,
                            "cholesterolPercentDRV": None,
                            "copperMg": 0.18063482367033684,
                            "copperPercentRDI": 0.201,
                            "fiberG": 5.384836389507282,
                            "fiberPercentDRV": 0.192,
                            "folateMcg": 203.54935310047495,
                            "folatePercentRDI": 0.509,
                            "ironMg": 3.1960343834451326,
                            "ironPercentRDI": 0.178,
                            "magnesiumMg": 92.31866226530008,
                            "magnesiumPercentRDI": 0.22,
                            "manganeseMg": 0.9961531365279406,
                            "manganesePercentRDI": 0.433,
                            "niacinMg": 1.413228804476075,
                            "niacinPercentRDI": 0.088,
                            "pantothenicAcidMg": 0.401949020950366,
                            "phosphorusMg": 88.07161323788152,
                            "phosphorusPercentRDI": 0.07,
                            "potassiumMg": 784.223636769088,
                            "potassiumPercentRDI": 0.167,
                            "proteinG": 4.297710005745912,
                            "proteinPercentRDI": 0.086,
                            "riboflavinMg": 0.2577903715697369,
                            "riboflavinPercentRDI": 0.198,
                            "saturatedFatG": 0.12156197775213858,
                            "seleniumMcg": 1.3875234922387756,
                            "seleniumPercentRDI": 0.025,
                            "sodiumMg": 191.22044146188216,
                            "sodiumPercentDRV": 0.083,
                            "sugarG": 5.146191688748732,
                            "sugarPercentDRV": None,
                            "thiaminMg": 0.15720713861727426,
                            "thiaminPercentRDI": 0.131,
                            "totalFatG": 0.5777541917214527,
                            "totalFatPercentDRV": 0.007,
                            "transFatG": 0,
                            "vitaminAMcg": 3851.410713597795,
                            "vitaminAPercentRDI": 4.279,
                            "vitaminB12Mcg": 0,
                            "vitaminB12PercentRDI": None,
                            "vitaminB6Mg": 0.33252588361458996,
                            "vitaminB6PercentRDI": 0.196,
                            "vitaminCMg": 47.419118105002575,
                            "vitaminCPercentRDI": 0.527,
                            "vitaminDMcg": 0,
                            "vitaminDPercentRDI": None,
                            "vitaminEMg": 2.2072884201822753,
                            "vitaminEPercentRDI": 0.147,
                            "vitaminKMcg": 465.5096291016638,
                            "vitaminKPercentRDI": 3.879,
                            "zincMg": 0.7685196228818442,
                            "zincPercentRDI": 0.07
                        }
            },
            "ingredient": None,
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": "dW5pdDoxNA==",
                "name": "each"
            }
        }
    },
    {
        "quantityUnitValues": [
            {
                "unit": {
                    "id": "dW5pdDox",
                    "name": "g"
                },
                "value": 85.0485693
            },
            {
                "unit": {
                    "id": "dW5pdDoy",
                    "name": "kg"
                },
                "value": 0.0850485693
            },
            {
                "unit": {
                    "id": "dW5pdDoz",
                    "name": "oz"
                },
                "value": 3
            },
            {
                "unit": {
                    "id": "dW5pdDo0",
                    "name": "lb"
                },
                "value": 0.1874999998346533
            }
        ],
        "id": "7n61v30l0j8",
              "ingredient": None,
              "recipeItem": {
                  "subRecipeId": "cmVjaXBlOjE2NzEyMg==",
            "subRecipe": {
                "id": "cmVjaXBlOjE2NzEyMg==",
                "name": "Sesame Ground Chicken",
                        "externalName": None,
                        "allIngredients": [
                            "Ground Chicken",
                            "Garlic",
                            "Sesame Seeds",
                            "Sesame Oil",
                            "Himalayan Pink Salt",
                            "Black Pepper"
                        ],
                "reconciledNutritionals": {
                            "addedSugarG": 0,
                            "calciumMg": 13547.25145638252,
                            "calciumPercentRDI": 10.421,
                            "caloriesKCal": 116918.10550117132,
                            "carbsG": 436.956529045912,
                            "carbsPercentDRV": 1.589,
                            "cholesterolMg": 58239.02034567902,
                            "cholesterolPercentDRV": 194.13,
                            "copperMg": 71.31195214486098,
                            "copperPercentRDI": 79.236,
                            "fiberG": 119.77440453846869,
                            "fiberPercentDRV": 4.278,
                            "folateMcg": 1767.815876410046,
                            "folatePercentRDI": 4.42,
                            "ironMg": 643.3447086154572,
                            "ironPercentRDI": 35.741,
                            "magnesiumMg": 18522.844266899057,
                            "magnesiumPercentRDI": 44.102,
                            "manganeseMg": 38.00971416167416,
                            "manganesePercentRDI": 16.526,
                            "niacinMg": 3894.8856929758213,
                            "niacinPercentRDI": 243.43,
                            "pantothenicAcidMg": 722.3803359247019,
                            "phosphorusMg": 133005.65521163418,
                            "phosphorusPercentRDI": 106.405,
                            "potassiumMg": 375526.74218602147,
                            "potassiumPercentRDI": 79.899,
                            "proteinG": 12881.400411396457,
                            "proteinPercentRDI": 257.628,
                            "riboflavinMg": 166.75166105475347,
                            "riboflavinPercentRDI": 128.271,
                            "saturatedFatG": 1893.8084282904579,
                            "seleniumMcg": 8110.921473342941,
                            "seleniumPercentRDI": 147.471,
                            "sodiumMg": 84188.43469892853,
                            "sodiumPercentDRV": 36.604,
                            "sugarG": 3.56897576566979,
                            "sugarPercentDRV": None,
                            "thiaminMg": 73.07134716397437,
                            "thiaminPercentRDI": 60.893,
                            "totalFatG": 7317.755887866779,
                            "totalFatPercentDRV": 93.817,
                            "transFatG": 51.46972244916486,
                            "vitaminAMcg": 691.4086726556613,
                            "vitaminAPercentRDI": 0.768,
                            "vitaminB12Mcg": 277.7553278024692,
                            "vitaminB12PercentRDI": 115.731,
                            "vitaminB6Mg": 299.8591908945021,
                            "vitaminB6PercentRDI": 176.388,
                            "vitaminCMg": 22.234920098039222,
                            "vitaminCPercentRDI": 0.247,
                            "vitaminDMcg": 0,
                            "vitaminDPercentRDI": None,
                            "vitaminEMg": 241.0934915736993,
                            "vitaminEPercentRDI": 16.073,
                            "vitaminKMcg": 1377.7030301780142,
                            "vitaminKPercentRDI": 11.481,
                            "zincMg": 1114.7717097471852,
                            "zincPercentRDI": 101.343
                        }
            },
            "ingredient": None,
            "preparations": [],
            "quantity": 3,
            "unit": {
                "id": "dW5pdDoz",
                "name": "oz"
            }
        }
    },
    {
        "quantityUnitValues": [
            {
                "unit": {
                    "id": "dW5pdDox",
                    "name": "g"
                },
                "value": 70.87380775
            },
            {
                "unit": {
                    "id": "dW5pdDoy",
                    "name": "kg"
                },
                "value": 0.07087380775
            },
            {
                "unit": {
                    "id": "dW5pdDoz",
                    "name": "oz"
                },
                "value": 2.5
            },
            {
                "unit": {
                    "id": "dW5pdDo0",
                    "name": "lb"
                },
                "value": 0.15624999986221108
            },
            {
                "unit": {
                    "id": "dW5pdDo3NTU1MTY=",
                    "name": "batch"
                },
                "value": 0.0026041666643701845
            }
        ],
        "id": "qubvx9ak5bb",
              "ingredient": None,
              "recipeItem": {
                  "subRecipeId": "cmVjaXBlOjE3MDM5NA==",
            "subRecipe": {
                "id": "cmVjaXBlOjE3MDM5NA==",
                "name": "Peanut Coconut Sauce",
                        "externalName": None,
                        "allIngredients": [
                            "Coconut Aminos (Coconut Tree Sap, Sea Salt)",
                            "Lime Juice",
                            "Coconut Milk (Coconut, Water, Guar Gum)",
                            "Peanut Butter (Dry Roasted Peanuts)",
                            "Water",
                            "Sambal (Red Chile Peppers, Vinegar, Salt)",
                            "Garlic"
                        ],
                "reconciledNutritionals": {
                            "addedSugarG": 0,
                            "calciumMg": 3.1684181569284497,
                            "calciumPercentRDI": 0.002,
                            "caloriesKCal": 53.66203631343362,
                            "carbsG": 5.931480844736274,
                            "carbsPercentDRV": 0.022,
                            "cholesterolMg": 0,
                            "cholesterolPercentDRV": None,
                            "copperMg": 0.021694334590068795,
                            "copperPercentRDI": 0.024,
                            "fiberG": 0.25925700237554117,
                            "fiberPercentDRV": 0.009,
                            "folateMcg": 4.662944286512987,
                            "folatePercentRDI": 0.012,
                            "ironMg": 0.08727603182928573,
                            "ironPercentRDI": 0.005,
                            "magnesiumMg": 8.422029852813752,
                            "magnesiumPercentRDI": 0.02,
                            "manganeseMg": 0.07968240957035716,
                            "manganesePercentRDI": 0.035,
                            "niacinMg": 0.6287359687622166,
                            "niacinPercentRDI": 0.039,
                            "pantothenicAcidMg": 0.06062563923716235,
                            "phosphorusMg": 16.6108569332684,
                            "phosphorusPercentRDI": 0.013,
                            "potassiumMg": 35.3618045624374,
                            "potassiumPercentRDI": 0.008,
                            "proteinG": 1.190862966668126,
                            "proteinPercentRDI": 0.024,
                            "riboflavinMg": 0.009900242547519483,
                            "riboflavinPercentRDI": 0.008,
                            "saturatedFatG": 1.1966419313881989,
                            "seleniumMcg": 0.1983239364917749,
                            "seleniumPercentRDI": 0.004,
                            "sodiumMg": 80.1688699548479,
                            "sodiumPercentDRV": 0.035,
                            "sugarG": 4.635864789281829,
                            "sugarPercentDRV": None,
                            "thiaminMg": 0.008514061320616884,
                            "thiaminPercentRDI": 0.007,
                            "totalFatG": 3.2182500200225643,
                            "totalFatPercentDRV": 0.041,
                            "transFatG": 0.0035436903875000004,
                            "vitaminAMcg": 1.449295858309044,
                            "vitaminAPercentRDI": 0.002,
                            "vitaminB12Mcg": 0,
                            "vitaminB12PercentRDI": None,
                            "vitaminB6Mg": 0.022999931273467538,
                            "vitaminB6PercentRDI": 0.014,
                            "vitaminCMg": 1.7259736392050762,
                            "vitaminCPercentRDI": 0.019,
                            "vitaminDMcg": 0,
                            "vitaminDPercentRDI": None,
                            "vitaminEMg": 0.4437743529419914,
                            "vitaminEPercentRDI": 0.03,
                            "vitaminKMcg": 0.046390128709090914,
                            "vitaminKPercentRDI": 0,
                            "zincMg": 0.12343713881647085,
                            "zincPercentRDI": 0.011
                        }
            },
            "ingredient": None,
            "preparations": [
                {
                    "id": "cHJlcGFyYXRpb246MjgxMTQ=",
                    "name": "3.25 oz RAM"
                },
                {
                    "id": "cHJlcGFyYXRpb246MjgzMzQ=",
                    "name": "standalone"
                }
            ],
            "quantity": 2.5,
            "unit": {
                "id": "dW5pdDoz",
                "name": "oz"
            }
        }
    },
    {
        "quantityUnitValues": [
            {
                "unit": {
                    "id": "dW5pdDox",
                    "name": "g"
                },
                "value": 0.5669904619999999
            },
            {
                "unit": {
                    "id": "dW5pdDoy",
                    "name": "kg"
                },
                "value": 0.000566990462
            },
            {
                "unit": {
                    "id": "dW5pdDoz",
                    "name": "oz"
                },
                "value": 0.02
            },
            {
                "unit": {
                    "id": "dW5pdDo0",
                    "name": "lb"
                },
                "value": 0.0012499999988976884
            },
            {
                "unit": {
                    "id": "dW5pdDoxNA==",
                    "name": "each"
                },
                "value": 1
            },
            {
                "unit": {
                    "id": "dW5pdDo3ODA1Mjc=",
                    "name": "case"
                },
                "value": 0.0005
            }
        ],
        "id": "pe1jbs2qawh",
              "ingredient": {
                  "name": "RAM3/RAM4 Lid - 3.25 oz Portion Cup Lids"
        },
        "recipeItem": {
                  "subRecipeId": None,
            "subRecipe": None,
            "ingredient": {
                "externalName": "RAM3 Lid - 3.25 oz Portion Cup Lids",
                "name": "RAM3/RAM4 Lid - 3.25 oz Portion Cup Lids"
            },
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": "dW5pdDoxNA==",
                "name": "each"
            }
        }
    },
    {
        "quantityUnitValues": [
            {
                "unit": {
                    "id": "dW5pdDox",
                    "name": "g"
                },
                "value": 5.66990462
            },
            {
                "unit": {
                    "id": "dW5pdDoy",
                    "name": "kg"
                },
                "value": 0.00566990462
            },
            {
                "unit": {
                    "id": "dW5pdDoz",
                    "name": "oz"
                },
                "value": 0.2
            },
            {
                "unit": {
                    "id": "dW5pdDo0",
                    "name": "lb"
                },
                "value": 0.012499999988976886
            },
            {
                "unit": {
                    "id": "dW5pdDoxNA==",
                    "name": "each"
                },
                "value": 1
            },
            {
                "unit": {
                    "id": "dW5pdDo3ODA1MjY=",
                    "name": "case"
                },
                "value": 0.0005
            }
        ],
        "id": "qipk6vmp8kl",
              "ingredient": {
                  "name": "RAM3 - 3.25 oz Portion Cups"
        },
        "recipeItem": {
                  "subRecipeId": None,
            "subRecipe": None,
            "ingredient": {
                "externalName": "RAM3 - 3.25 oz Portion Cups",
                "name": "RAM3 - 3.25 oz Portion Cups"
            },
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": "dW5pdDoxNA==",
                "name": "each"
            }
        }
    },
    {
        "quantityUnitValues": [
            {
                "unit": {
                    "id": "dW5pdDox",
                    "name": "g"
                },
                "value": 65.20390312999999
            },
            {
                "unit": {
                    "id": "dW5pdDoy",
                    "name": "kg"
                },
                "value": 0.06520390312999999
            },
            {
                "unit": {
                    "id": "dW5pdDoz",
                    "name": "oz"
                },
                "value": 2.3
            },
            {
                "unit": {
                    "id": "dW5pdDo0",
                    "name": "lb"
                },
                "value": 0.14374999987323417
            },
            {
                "unit": {
                    "id": "dW5pdDoxNA==",
                    "name": "each"
                },
                "value": 1
            },
            {
                "unit": {
                    "id": "dW5pdDo3ODA1MzM=",
                    "name": "case"
                },
                "value": 0.006666666666666667
            }
        ],
        "id": "85qgllkyigr",
              "ingredient": {
                  "name": "TS48 - 48Oz Meal Boxes"
        },
        "recipeItem": {
                  "subRecipeId": None,
            "subRecipe": None,
            "ingredient": {
                "externalName": "48 oz Meal Boxes",
                "name": "TS48 - 48Oz Meal Boxes"
            },
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": "dW5pdDoxNA==",
                "name": "each"
            }
        }
    },
    {
        "quantityUnitValues": [
            {
                "unit": {
                    "id": "dW5pdDoxNA==",
                    "name": "each"
                },
                "value": 1
            }
        ],
        "id": "qf748nz6npr",
              "ingredient": {
                  "name": "Label Meal Meat - 2.75\" x 8\" RECTANGLE2 COLORS on MATTE BOPP w/ UV VARNISH ((for TS20, TS24, TS32, TS48)"
        },
        "recipeItem": {
                  "subRecipeId": None,
            "subRecipe": None,
            "ingredient": {
                "externalName": "Meal Meat - 2.75\" x 8\" RECTANGLE\n2 COLORS on MATTE BOPP w/ UV VARNISH",
                "name": "Label Meal Meat - 2.75\" x 8\" RECTANGLE2 COLORS on MATTE BOPP w/ UV VARNISH ((for TS20, TS24, TS32, TS48)"
            },
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": "dW5pdDoxNA==",
                "name": "each"
            }
        }
    }
]
