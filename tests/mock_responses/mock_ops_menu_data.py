from copy import deepcopy
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.enums import IngredientCategoryTagTypeEnum, MenuCategoryEnum, MenuItemCategoryEnum, PreparationEnum, RecipeCategoryTagTypeEnum, IngredientCategoryValueEnum, DietaryFlagEnum, UnitEnum


MOCK_RECIPE_TREE_COMPONENTS = [
    {
        "id": "x5ccun97m7",
        "ancestorComponentIds": [],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 1,
                    "unit": {
                        "id": UnitEnum.EACH.value,
                        "name": "each"
                    }
                }
            ]
        },
        "recipeItem": None
    },
    {
        "id": "k41l3crd8of",
        "ancestorComponentIds": [
            "x5ccun97m7"
        ],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 222.54375633499996,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 7.85,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.4906249995673427,
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
        "recipeItem": {
            "preparations": [
                {
                    "id": PreparationEnum.CORE_RECIPE.value,
                    "name": "Core Recipe"
                }
            ],
            "quantity": 1,
            "unit": {
                "id": UnitEnum.EACH.value,
                "name": "each"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE5MjY1NA==",
                "name": "Greek Salad with Crispy Chickpeas BASE",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [],
                "dietaryFlagsWithUsages": [
                    {
                        "dietaryFlag": {
                            "id": DietaryFlagEnum.SOY_BEANS.value,
                            "name": "soybeans"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "d44pdeapsdk",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of"
        ],
        "quantity": 4,
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
        "recipeItem": {
            "preparations": [
                {
                    'id': PreparationEnum.TWO_OZ_RAM.value,
                    'name': '2 oz RAM'
                }
            ],
            "quantity": 4,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4OTcwNA==",
                "name": "Olive, Red Pepper & Cucumber Quinoa Pilaf",
                "externalName": None,
                "categoryValues": [
                    {
                        "id": "Y2F0ZWdvcnlWYWx1ZToxODQ3NA==",
                        "name": "50",
                        "category": {
                            "id": RecipeCategoryTagTypeEnum.BIN_WEIGHT_TAG.value,
                            "name": "bin weight",
                            "itemType": "recipe"
                        }
                    }
                ],
                "recipeInstructions": [
                    {
                        "text": "Stage lexans for mixing. With sleeved gloves, mix the cucumber, red bell pepper, olives, hemp seeds, parsley and scallions in the quinoa being sure to distribute each ingredient evenly.",
                        "position": 0
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "wuet0e3vilq",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of",
            "d44pdeapsdk"
        ],
        "quantity": 0.12499999988976887,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 30,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4ODYwNg==",
                "name": "Cooked Rainbow Quinoa",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "Bring water in tilt skillet to a boil. Add quinoa to tilt skillet, no more than 75 lbs at a time.",
                        "position": 0
                    },
                    {
                        "text": "Simmer, close lid, and cook until tender, stirring occasionally to prevent dry spots in the corners.",
                        "position": 1
                    },
                    {
                        "text": "After 10 minutes turn off heat and let steam for 5 minutes.",
                        "position": 2
                    },
                    {
                        "text": "Scoop quinoa onto sheet trays to cool down.",
                        "position": 3
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "ss91mevjky",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of",
            "d44pdeapsdk"
        ],
        "quantity": 0.021874999980709554,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 7,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ2Mzc=",
                "name": "olives, kalamata, sliced",
                "externalName": "Kalamata Olives",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "a3rm32jf58",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of",
            "d44pdeapsdk"
        ],
        "quantity": 0.024999999977953775,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 8,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3Mjk2NQ==",
                "name": "Sliced Scallion",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "Pick off any stickers, twisty ties, or rubber bands from any bunched herbs.",
                        "position": 0
                    },
                    {
                        "text": "Using the 2 compartment sink, wash the produce well using a diluted veg wash solution.",
                        "position": 1
                    },
                    {
                        "text": "Once rinsed and visibly clean, strain onto perforated sheet trays.",
                        "position": 2
                    },
                    {
                        "text": "Let air dry on speed rack or spin dry using the electric spinner.",
                        "position": 3
                    },
                    {
                        "text": "Trim the tips of the scallions. Gather the scallions within your hand and line them up evenly slice across to make thin slices.",
                        "position": 4
                    },
                    {
                        "text": "Store in a cambro.",
                        "position": 5
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "hdeta8wr90j",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of"
        ],
        "quantity": 1.5,
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
        "recipeItem": {
            "preparations": [
                {
                    "id": PreparationEnum.INSERT12.value,
                    "name": "INSERT12"
                }
            ],
            "quantity": 1.5,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NjQ3Mw==",
                "name": "Tofu Feta",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "Stage clear polycarbonate lexans for mixing and add brine for tofu feta.",
                        "position": 0
                    },
                    {
                        "text": "Dice Tofu into small 1/4\" diced bite sized squares and add to each lexan, mixing well with the brine for tofu feta, being sure all of the tofu is submerged.",
                        "position": 1
                    },
                    {
                        "text": "Let sit at least 4 hours, best overnight.",
                        "position": 2
                    },
                    {
                        "text": "Strain well before serving.",
                        "position": 3
                    }
                ],
                "dietaryFlagsWithUsages": [
                    {
                        "dietaryFlag": {
                            "id": DietaryFlagEnum.SOY_BEANS.value,
                            "name": "soybeans"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "trr5acd7ly",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of",
            "hdeta8wr90j"
        ],
        "quantity": 0.06696428565523334,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 25,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjIxNjA2MA==",
                "name": "Brine for \"Feta\"",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "Stage clear polycarbonate lexans for mixing. In each lexan combine all of the ingredients blend using an immersion blender.",
                        "position": 0
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "oz9yp3l0aek",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of",
            "hdeta8wr90j"
        ],
        "quantity": 0.09374999991732666,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 35,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE5MDA5MQ==",
                "name": "Small Diced Tofu (1/4\")",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "Start by opening the bags of firm tofu over perforated lexans to strain any liquid.",
                        "position": 0
                    },
                    {
                        "text": "Dice the tofu into 1/4\" pieces. Reserve in lexans.",
                        "position": 1
                    }
                ],
                "dietaryFlagsWithUsages": [
                    {
                        "dietaryFlag": {
                            "id": DietaryFlagEnum.SOY_BEANS.value,
                            "name": "soybeans"
                        }
                    }
                ]
            }
        }
    },
    {
        "id": "3oiimc548lt",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of"
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
        "recipeItem": {
            "preparations": [],
            "quantity": 2.5,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ1NjE=",
                "name": "lettuce, spring mix, SEND TO PLATE",
                "externalName": "Spring Mix Lettuce* or Seasonal Greens*\u00a7",
                "categoryValues": [
                    {
                        "id": "Y2F0ZWdvcnlWYWx1ZToxODQ3Mw==",
                        "name": "30",
                        "category": {
                            "id": IngredientCategoryTagTypeEnum.BIN_WEIGHT_TAG.value,
                            "name": "bin weight",
                            "itemType": "ingredient"
                        }
                    }
                ],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "8o8ode59qdc",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "k41l3crd8of"
        ],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 24.097094634999998,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 0.85,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.05312499995315176,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": UnitEnum.EACH.value,
                "name": "each"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNzQ4ODA=",
                "name": "crispy roasted chickpeas, 0.85 oz bag, SEND TO PLATE",
                "externalName": "Crispy Chickpeas (Chickpeas, Sunflower Oil, Sea Salt)",
                "categoryValues": [
                    {
                        "id": "Y2F0ZWdvcnlWYWx1ZToxODQ3NQ==",
                        "name": "40",
                        "category": {
                            "id": IngredientCategoryTagTypeEnum.BIN_WEIGHT_TAG.value,
                            "name": "bin weight",
                            "itemType": "ingredient"
                        }
                    }
                ],
                "dietaryFlags": [
                    {
                        "id": DietaryFlagEnum.SESAME_SEEDS.value,
                        "name": "sesame seeds"
                    },
                    {
                        "id": DietaryFlagEnum.TREE_NUTS.value,
                        "name": "tree nuts"
                    }

                ]
            },
            "subRecipe": None
        }
    },
    {
        "id": "p1izi6jy93l",
        "ancestorComponentIds": [
            "x5ccun97m7"
        ],
        "quantity": 3,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 3,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3MDU4NA==",
                "name": "Smashed Chickpea Salad - COOKED GARBANZOS",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "The hobart must be used for this task, do not mix by hand.",
                        "position": 0
                    },
                    {
                        "text": "Latch bowl into the hobart, ensuring it is secured. While it is lowered, add in the garbanzo beans, lemon juice, and olive oil.",
                        "position": 1
                    },
                    {
                        "text": "Equip the PADDLE attachment, and patiently press the up arrow to rise the bowl until locked in place. Slide over the safeguard.",
                        "position": 2
                    },
                    {
                        "text": "Mix on Level 1 for 2 minutes to mash the beans.",
                        "position": 3
                    },
                    {
                        "text": "Slide the safeguard back, and add the remaining ingredients to the mixture. Mix again for 1 minute until fully combined, while pausing every now and then to scrape down the sides and bottom of bowl with a rubber spatula.",
                        "position": 4
                    },
                    {
                        "text": "Lower the bowl, unlatch and grab a buddy to help pour mixture into a lexan.",
                        "position": 5
                    },
                    {
                        "text": "Clean the entire machine after each project, take the bowl and attachments back to the dishpit.",
                        "position": 6
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "lkjyq9qnvy",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "p1izi6jy93l"
        ],
        "quantity": 0.0014062499987599,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 0.75,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ4MzQ=",
                "name": "spice, sumac",
                "externalName": "Sumac",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "4n11rdaopm7",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "p1izi6jy93l"
        ],
        "quantity": 0.003749999996693066,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 2,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ3OTM=",
                "name": "spice, black pepper, ground",
                "externalName": "Black Pepper",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "t2xotugmk6p",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "p1izi6jy93l"
        ],
        "quantity": 0.14062499987598998,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 75,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NjQ4MA==",
                "name": "Cooked Garbanzo Beans",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "Start by straining and rinsing the beans. Sift through on sheet trays to make sure there aren\u2019t any rocks, discolored beans, or any other foreign objects.",
                        "position": 0
                    },
                    {
                        "text": "Transfer the sifted beans to a tilt skillet, no more than 75# at a time. Cover with about a foot of water and bring to a boil by setting the temperature to high. Flavor the beans now with salt.",
                        "position": 1
                    },
                    {
                        "text": "Once brought to a simmer, stir the beans and cover. Set a timer for 40 minutes and check in 5 minute increments afterwards for doneness. Season now with salt. To make sure the beans are cooked through, taste with a spoon. A cooked bean should be creamy on the inside with skin that is intact, not broken.",
                        "position": 2
                    },
                    {
                        "text": "Turn off the heat. Strain beans from their liquids to cool down on sheet trays.",
                        "position": 3
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "whkxj26090m",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "p1izi6jy93l",
            "t2xotugmk6p"
        ],
        "quantity": 0.07031249993799499,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 75,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQyODE=",
                "name": "beans, garbanzo, dry",
                "externalName": "Garbanzo Beans",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "22r2c3aruw4",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "p1izi6jy93l"
        ],
        "quantity": 0.0112499999900792,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 6,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ2MzA=",
                "name": "oil, olive",
                "externalName": "Extra Virgin Olive Oil",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "vyx5cb1ymt",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "p1izi6jy93l"
        ],
        "quantity": 0.0112499999900792,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 6,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ1MzU=",
                "name": "juice, lemon",
                "externalName": "Lemon Juice",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "sb4q527ncb",
        "ancestorComponentIds": [
            "x5ccun97m7"
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
        },
        "recipeItem": {
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": UnitEnum.EACH.value,
                "name": "each"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDU5MDM=",
                "name": "TS48 - 48oz Meal Boxes",
                "externalName": "48 oz Meal Boxes",
                "categoryValues": [
                    {
                        "id": IngredientCategoryValueEnum.FOOD_PACKAGE.value,
                        "name": "food pkg",
                        "category": {
                            "id": "Y2F0ZWdvcnk6MjQyMA==",
                            "name": "accounting group",
                            "itemType": "ingredient"
                        }
                    }
                ],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "9ty070197l",
        "ancestorComponentIds": [
            "x5ccun97m7"
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
        "recipeItem": {
            "preparations": [
                {
                    "id": PreparationEnum.TWO_OZ_WINPAK.value,
                    "name": "2 oz WINPAK"
                },
                {
                    "id": PreparationEnum.STANDALONE.value,
                    "name": "standalone"
                }
            ],
            "quantity": 2,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjIyMzU3MQ==",
                "name": "Red Wine Vinaigrette 2oz",
                "externalName": "Red Wine Vinaigrette",
                "categoryValues": [],
                "recipeInstructions": [],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "arlkvxgdzvv",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "9ty070197l"
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
        "recipeItem": {
            "preparations": [],
            "quantity": 2,
            "unit": {
                "id": UnitEnum.OZ.value,
                "name": "oz"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE3NDI4OA==",
                "name": "Red Wine Vinaigrette BASE",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "In blixer combine half of the liquids to break up the red onion and garlic.",
                        "position": 0
                    },
                    {
                        "text": "Slowly add in oil through opening on the lid until emulsified.",
                        "position": 1
                    },
                    {
                        "text": "Pour into lexans.",
                        "position": 2
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "jyoqmn9ieg",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "9ty070197l",
            "arlkvxgdzvv"
        ],
        "quantity": 0.022916666646457626,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 11,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ5MTE=",
                "name": "vinegar, red wine",
                "externalName": "Red Wine Vinegar",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "3v0evgbhdzf",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "9ty070197l",
            "arlkvxgdzvv"
        ],
        "quantity": 0.007291666660236518,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 3.5,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNDQ3NzA=",
                "name": "sauce, mustard, dijon",
                "externalName": "Dijon Mustard (Water, Mustard Seeds, Vinegar, Salt)",
                "categoryValues": [],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    },
    {
        "id": "4pf3lu669b",
        "ancestorComponentIds": [
            "x5ccun97m7",
            "9ty070197l",
            "arlkvxgdzvv"
        ],
        "quantity": 0.00520833332874037,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 2.5,
            "unit": {
                "id": UnitEnum.LB.value,
                "name": "lb"
            },
            "ingredient": None,
            "subRecipe": {
                "id": "cmVjaXBlOjE4NDY0Mg==",
                "name": "Minced Garlic",
                "externalName": None,
                "categoryValues": [],
                "recipeInstructions": [
                    {
                        "text": "Add the garlic cloves to the blixer to process.  Pulse until finely minced.",
                        "position": 0
                    },
                    {
                        "text": "Transfer to a cambro or lexan.",
                        "position": 1
                    }
                ],
                "dietaryFlagsWithUsages": []
            }
        }
    },
    {
        "id": "2shnflhm1zl",
        "ancestorComponentIds": [
            "x5ccun97m7"
        ],
        "quantity": 1,
        "unit": {
            "id": UnitEnum.EACH.value,
            "name": "each",
            "unitValues": [
                {
                    "value": 3.685438003,
                    "unit": {
                        "id": UnitEnum.G.value,
                        "name": "g"
                    }
                },
                {
                    "value": 0.13,
                    "unit": {
                        "id": UnitEnum.OZ.value,
                        "name": "oz"
                    }
                },
                {
                    "value": 0.008124999992834976,
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
        "recipeItem": {
            "preparations": [],
            "quantity": 1,
            "unit": {
                "id": UnitEnum.EACH.value,
                "name": "each"
            },
            "ingredient": {
                "locationVendorItems": [],
                "id": "aW5ncmVkaWVudDoyNzQ5NjA=",
                "name": "WINPAK Portion Cups",
                "externalName": "WIN2 - WINPAK Portion Cups 2oz WIN2",
                "categoryValues": [
                    {
                        "id": IngredientCategoryValueEnum.FOOD_PACKAGE.value,
                        "name": "food pkg",
                        "category": {
                            "id": "Y2F0ZWdvcnk6MjQyMA==",
                            "name": "accounting group",
                            "itemType": "ingredient"
                        }
                    }
                ],
                "dietaryFlags": []
            },
            "subRecipe": None
        }
    }
]


MOCK_FORMATTED_PRIMARY_RECIPE_COMPONENTS = [
    {
        "allergens": [],
        "binWeight": {
            "unit": "lb",
            "value": 50.0
        },
        "cuppingContainer": "2 oz RAM",
        "id": "cmVjaXBlOjE4OTcwNA==",
        "instructions": [
            {
                "id": 1,
                "text": "Stage lexans for mixing. With sleeved gloves, mix the cucumber, red bell pepper, olives, hemp seeds, parsley and scallions in the quinoa being sure to distribute each ingredient evenly."
            }
        ],
        "name": "Olive, Red Pepper & Cucumber Quinoa Pilaf",
        "quantityValues": [
            {
                "unit": "oz",
                "value": 4.0
            },
            {
                "unit": "lb",
                "value": 0.2499999997795377
            }
        ],
        "recipeComponents": [
            {
                "allergens": [],
                "id": "cmVjaXBlOjE4ODYwNg==",
                "name": "Cooked Rainbow Quinoa",
                "type": "recipe",
                "usage": {
                    "unit": "lb",
                    "value": 30
                }
            },
            {
                "allergens": [],
                "id": "aW5ncmVkaWVudDoyNDQ2Mzc=",
                "name": "olives, kalamata, sliced",
                "type": "ingredient",
                "usage": {
                    "unit": "lb",
                    "value": 7
                }
            },
            {
                "allergens": [],
                "id": "cmVjaXBlOjE3Mjk2NQ==",
                "name": "Sliced Scallion",
                "type": "recipe",
                "usage": {
                    "unit": "oz",
                    "value": 8
                }
            }
        ],
        "type": "recipe",
        "usage": {
            "unit": "oz",
            "value": 4
        }
    },
    {
        "allergens": [
            "soy"
        ],
        "binWeight": {
            "unit": "lb",
            "value": 60.0
        },
        "cuppingContainer": "INSERT12",
        "id": "cmVjaXBlOjE3NjQ3Mw==",
        "instructions": [
            {
                "id": 1,
                "text": "Stage clear polycarbonate lexans for mixing and add brine for tofu feta."
            },
            {
                "id": 2,
                "text": "Dice Tofu into small 1/4\" diced bite sized squares and add to each lexan, mixing well with the brine for tofu feta, being sure all of the tofu is submerged."
            },
            {
                "id": 3,
                "text": "Let sit at least 4 hours, best overnight."
            },
            {
                "id": 4,
                "text": "Strain well before serving."
            }
        ],
        "name": "Tofu Feta",
        "quantityValues": [
            {
                "unit": "oz",
                "value": 1.5
            },
            {
                "unit": "lb",
                "value": 0.09374999991732665
            }
        ],
        "recipeComponents": [
            {
                "allergens": [],
                "id": "cmVjaXBlOjIxNjA2MA==",
                "name": "Brine for \"Feta\"",
                "type": "recipe",
                "usage": {
                    "unit": "lb",
                    "value": 25
                }
            },
            {
                "allergens": [
                    "soy"
                ],
                "id": "cmVjaXBlOjE5MDA5MQ==",
                "name": "Small Diced Tofu (1/4\")",
                "type": "recipe",
                "usage": {
                    "unit": "lb",
                    "value": 35
                }
            }
        ],
        "type": "recipe",
        "usage": {
            "unit": "oz",
            "value": 1.5
        }
    },
    {
        "allergens": [],
        "binWeight": {
            "unit": "lb",
            "value": 30.0
        },
        "cuppingContainer": None,
        "id": "aW5ncmVkaWVudDoyNDQ1NjE=",
        "name": "lettuce, spring mix, SEND TO PLATE",
        "quantityValues": [
            {
                "unit": "oz",
                "value": 2.5
            },
            {
                "unit": "lb",
                "value": 0.15624999986221108
            }
        ],
        "type": "ingredient",
        "usage": {
            "unit": "oz",
            "value": 2.5
        }
    },
    {
        "allergens": [
            "sesame_seeds",
            "tree_nuts"
        ],
        "binWeight": {
            "unit": "lb",
            "value": 40.0
        },
        "cuppingContainer": None,
        "id": "aW5ncmVkaWVudDoyNzQ4ODA=",
        "name": "crispy roasted chickpeas, 0.85 oz bag, SEND TO PLATE",
        "quantityValues": [
            {
                "unit": "oz",
                "value": 0.85
            },
            {
                "unit": "lb",
                "value": 0.05312499995315176
            }
        ],
        "type": "ingredient",
        "usage": {
            "unit": "each",
            "value": 1
        }
    },
    {
        "allergens": [],
        "binWeight": {
            "unit": "lb",
            "value": 60.0
        },
        "cuppingContainer": None,
        "id": "cmVjaXBlOjE3MDU4NA==",
        "instructions": [
            {
                "id": 1,
                "text": "The hobart must be used for this task, do not mix by hand."
            },
            {
                "id": 2,
                "text": "Latch bowl into the hobart, ensuring it is secured. While it is lowered, add in the garbanzo beans, lemon juice, and olive oil."
            },
            {
                "id": 3,
                "text": "Equip the PADDLE attachment, and patiently press the up arrow to rise the bowl until locked in place. Slide over the safeguard."
            },
            {
                "id": 4,
                "text": "Mix on Level 1 for 2 minutes to mash the beans."
            },
            {
                "id": 5,
                "text": "Slide the safeguard back, and add the remaining ingredients to the mixture. Mix again for 1 minute until fully combined, while pausing every now and then to scrape down the sides and bottom of bowl with a rubber spatula."
            },
            {
                "id": 6,
                "text": "Lower the bowl, unlatch and grab a buddy to help pour mixture into a lexan."
            },
            {
                "id": 7,
                "text": "Clean the entire machine after each project, take the bowl and attachments back to the dishpit."
            }
        ],
        "name": "Smashed Chickpea Salad - COOKED GARBANZOS",
        "quantityValues": [
            {
                "unit": "oz",
                "value": 3.0
            },
            {
                "unit": "lb",
                "value": 0.1874999998346533
            }
        ],
        "recipeComponents": [
            {
                "allergens": [],
                "id": "aW5ncmVkaWVudDoyNDQ4MzQ=",
                "name": "spice, sumac",
                "type": "ingredient",
                "usage": {
                    "unit": "oz",
                    "value": 0.75
                }
            },
            {
                "allergens": [],
                "id": "aW5ncmVkaWVudDoyNDQ3OTM=",
                "name": "spice, black pepper, ground",
                "type": "ingredient",
                "usage": {
                    "unit": "oz",
                    "value": 2
                }
            },
            {
                "allergens": [],
                "id": "cmVjaXBlOjE3NjQ4MA==",
                "name": "Cooked Garbanzo Beans",
                "type": "recipe",
                "usage": {
                    "unit": "lb",
                    "value": 75
                }
            },
            {
                "allergens": [],
                "id": "aW5ncmVkaWVudDoyNDQ2MzA=",
                "name": "oil, olive",
                "type": "ingredient",
                "usage": {
                    "unit": "lb",
                    "value": 6
                }
            },
            {
                "allergens": [],
                "id": "aW5ncmVkaWVudDoyNDQ1MzU=",
                "name": "juice, lemon",
                "type": "ingredient",
                "usage": {
                    "unit": "lb",
                    "value": 6
                }
            }
        ],
        "type": "recipe",
        "usage": {
            "unit": "oz",
            "value": 3
        }
    },
    {
        "allergens": [],
        "binWeight": {
            "unit": "lb",
            "value": 60.0
        },
        "cuppingContainer": "2 oz WINPAK",
        "id": "cmVjaXBlOjIyMzU3MQ==",
        "instructions": [],
        "name": "Red Wine Vinaigrette 2oz",
        "quantityValues": [
            {
                "unit": "oz",
                "value": 2.0
            },
            {
                "unit": "lb",
                "value": 0.12499999988976886
            }
        ],
        "recipeComponents": [
            {
                "allergens": [],
                "id": "cmVjaXBlOjE3NDI4OA==",
                "name": "Red Wine Vinaigrette BASE",
                "type": "recipe",
                "usage": {
                    "unit": "oz",
                    "value": 2
                }
            }
        ],
        "type": "recipe",
        "usage": {
            "unit": "oz",
            "value": 2
        }
    }
]


def mock_ops_menu(date, location_name=DEFAULT_LOCATION, menu_type=DEFAULT_MENU_TYPE):
    return (
        {
            'name': f'{date} 1_2_3',
            'id': 'MENU123ABC-OPS',
            'date': f'{date}',
            'location': {
                'name': location_name,
            },
            'categoryValues': [
                {
                    'id': 1,
                    'name': menu_type,
                    'category': {
                        'id': MenuCategoryEnum.MENU_TYPE.value,
                        'itemType': 'menu',
                        'name': 'menu type'
                    },
                }
            ],
            'menuItems': [
                {
                    'id': 'MENUITEM1ABC-OPS',
                    'recipeId': 'RECIPE1ABC-OPS',
                    'categoryValues': [
                        {
                            'name': 'lm1',
                            'category': {
                                'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                                'itemType': 'menuItem',
                                'name': 'product_code'
                            }
                        }
                    ],
                    'recipe': {
                        'id': 'RECIPE1ABC-OPS',
                        'name': 'Test Recipe Name 1',
                        'categoryValues': [
                            {
                                'id': 'Y2F0ZWdvcnlWYWx1ZToxNTAzMg==',
                                'name': 'ts48',
                                'category': {
                                    'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                                    'name': 'meal container',
                                    'itemType': 'recipe'
                                }
                            }
                        ],
                        'files': {
                            'photos': [
                                {
                                    'caption': 'plating',
                                    'sourceUrl': 'https://cdn.filestackcontent.com/2X5ivrEYQvuEh30DyYot'
                                }
                            ]
                        },
                        'recipeTreeComponents': deepcopy(MOCK_RECIPE_TREE_COMPONENTS)
                    },
                    'volume': 923,
                    'unit': {
                        'name': 'each',
                        'id': 'unitIdEach123'
                    }
                },
                {
                    'id': 'MENUITEM2DEF-OPS',
                    'recipeId': 'RECIPE2DEF-OPS',
                    'categoryValues': [
                        {
                            'name': 'lv2',
                            'category': {
                                'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                                'itemType': 'menuItem',
                                'name': 'product_code'
                            }
                        }
                    ],
                    'recipe': {
                        'id': 'RECIPE2DEF-OPS',
                        'name': 'Test Recipe Name 2',
                        'categoryValues': [
                            {
                                'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                                'name': 'ts32',
                                'category': {
                                    'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                                    'name': 'meal container',
                                    'itemType': 'recipe'
                                },
                            }
                        ],
                        'files': {
                            'photos': [
                                {
                                    'caption': 'plating',
                                    'sourceUrl': 'https://cdn.filestackcontent.com/IQM3KcAkRye81xuN5JY4'
                                },
                                {
                                    'caption': 'menu',
                                    'sourceUrl': 'https://cdn.filestackcontent.com/4q9frUq1TBWnFaWfET5X'
                                }
                            ]
                        },
                        'recipeTreeComponents': deepcopy(MOCK_RECIPE_TREE_COMPONENTS)
                    },
                    'volume': 1228,
                    'unit': {
                        'name': 'each',
                        'id': 'unitIdEach123'
                    }
                },
                {
                    'id': 'MENUITEM3GHI-OPS',
                    'recipeId': 'RECIPE3GHI-OPS',
                    'categoryValues': [
                        {
                            'name': 'dv3',
                            'category': {
                                'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                                'itemType': 'menuItem',
                                'name': 'product_code'
                            }
                        }
                    ],
                    'recipe': {
                        'id': 'RECIPE3GHI-OPS',
                        'name': 'Test Recipe Name 3',
                        'categoryValues': [
                            {
                                'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                                'name': 'ts32',
                                'category': {
                                    'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                                    'name': 'meal container',
                                    'itemType': 'recipe'
                                },
                            }
                        ],
                        'files': {},
                        'recipeTreeComponents': deepcopy(MOCK_RECIPE_TREE_COMPONENTS)
                    },
                    'volume': 549,
                    'unit': {
                        'name': 'each',
                        'id': 'unitIdEach123'
                    }
                },
                {
                    'id': 'MENUITEM4JKL-OPS',
                    'recipeId': 'RECIPE4JKL-OPS',
                    'categoryValues': [
                        {
                            'name': 'ssa',
                            'category': {
                                'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                                'itemType': 'menuItem',
                                'name': 'product_code'
                            }
                        }
                    ],
                    'recipe': {
                        'id': 'RECIPE4JKL-OPS',
                        'name': 'Jar Salad 1',
                        'categoryValues': [
                            {
                                'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                                'name': 'ts32',
                                'category': {
                                    'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                                    'name': 'meal container',
                                    'itemType': 'recipe'
                                },
                            }
                        ],
                        'files': {},
                        'recipeTreeComponents': deepcopy(MOCK_RECIPE_TREE_COMPONENTS)
                    },
                    'volume': 123,
                    'unit': {
                        'name': 'each',
                        'id': 'unitIdEach123'
                    }
                },
                {
                    'id': 'MENUITEM5MNO-OPS',
                    'recipeId': 'RECIPE5MNO-OPS',
                    'categoryValues': [
                        {
                            'name': 'sch',
                            'category': {
                                'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                                'itemType': 'menuItem',
                                'name': 'product_code'
                            }
                        }
                    ],
                    'recipe': {
                        'id': 'RECIPE5MNO-OPS',
                        'name': 'Side Soup 4',
                        'categoryValues': [
                            {
                                'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                                'name': 'ts32',
                                'category': {
                                    'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                                    'name': 'meal container',
                                    'itemType': 'recipe'
                                },
                            }
                        ],
                        'files': {},
                        'recipeTreeComponents': deepcopy(MOCK_RECIPE_TREE_COMPONENTS)
                    },
                    'volume': 321,
                    'unit': {
                        'name': 'each',
                        'id': 'unitIdEach123'
                    }
                },
                {
                    'id': 'MENUITEM6PQR-OPS',
                    'recipeId': 'RECIPE6PQR-OPS',
                    'categoryValues': [
                        {
                            'name': 'av',
                            'category': {
                                'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                                'itemType': 'menuItem',
                                'name': 'product_code'
                            }
                        }
                    ],
                    'recipe': {
                        'id': 'RECIPE6PQR-OPS',
                        'name': 'Baby Avocado',
                        'categoryValues': [
                            {
                                'id': 'Y2F0ZWdvcnlWYWx1ZToxNTExNg==',
                                'name': 'ts32',
                                'category': {
                                    'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
                                    'name': 'meal container',
                                    'itemType': 'recipe'
                                },
                            }
                        ],
                        'files': {},
                        'recipeTreeComponents': []
                    },
                    'volume': 456,
                    'unit': {
                        'name': 'each',
                        'id': 'unitIdEach123'
                    }
                },
                {
                    'id': 'MENUITEM7STU-OPS',
                    'recipeId': 'RECIPE7STU-OPS',
                    'categoryValues': [
                        {
                            'name': 'hla',
                            'category': {
                                'id': MenuItemCategoryEnum.PRODUCT_CODE.value,
                                'itemType': 'menuItem',
                                'name': 'product_code'
                            }
                        }
                    ],
                    'recipe': {
                        'id': 'RECIPE7STU-OPS',
                        'name': 'Juice',
                        'categoryValues': [],
                        'files': {},
                        'recipeTreeComponents': []
                    },
                    'volume': 199,
                    'unit': {
                        'name': 'each',
                        'id': 'unitIdEach123'
                    }
                }
            ]
        }
    )

