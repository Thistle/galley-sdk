from galley.enums import MenuCategoryEnum, MenuItemCategoryEnum, PreparationEnum, RecipeCategoryTagTypeEnum, IngredientCategoryValueEnum, DietaryFlagEnum

mock_recipeTreeComponents = [
    {
        'quantity': 8.85,
        'unit': {
            'id': 'dW5pdDoz',
            'name': 'oz'
        },
        'quantityUnitValues': [
            {
                'unit': { 'id': 'dW5pdDox', 'name': 'g' },
                'value': 250.893279435
            },
            {
                'unit': { 'id': 'dW5pdDoy', 'name': 'kg' },
                'value': 0.250893279435
            },
            {
                'unit': { 'id': 'dW5pdDoz', 'name': 'oz' },
                'value': 8.85
            },
            {
                'unit': { 'id': 'dW5pdDo0', 'name': 'lb' },
                'value': 0.5531249995122273
            },
            {
                'unit': { 'id': 'dW5pdDoxNA==','name': 'each' },
                'value': 1
            }
        ],
        'ingredient': None,
        'recipeItem': {
            'preparations': [
                {
                    'id': PreparationEnum.CORE_RECIPE.value,
                    'name': 'Base Recipe'
                }
            ],
            'subRecipe': {
                'externalName': None,
                'id': 'cmVjaXBlOjE5MjY1NA==',
                'name': 'Greek Salad with Crispy Chickpeas BASE',
                'recipeInstructions': [],
                'categoryValues': [],
                'dietaryFlagsWithUsages': [
                    {
                        'dietaryFlag': {
                            'id': 'ZGlldGFyeUZsYWc6Ng==',
                            'name': 'soy beans'
                        }
                    }
                ],
                'recipeTreeComponents': [
                    {
                        'ingredient': None,
                        'quantity': 4,
                        'unit': {
                            'id': 'dW5pdDoz',
                            'name': 'oz'
                        },
                        'quantityUnitValues': [
                            {
                                'unit': { 'id': 'dW5pdDox', 'name': 'g'},
                                'value': 113.3980924
                            },
                            {
                                'unit': { 'id': 'dW5pdDoy', 'name': 'kg' },
                                'value': 0.1133980924
                            },
                            {
                                'unit': { 'id': 'dW5pdDoz', 'name': 'oz' },
                                'value': 4
                            },
                            {
                                'unit': { 'id': 'dW5pdDo0', 'name': 'lb' },
                                'value': 0.2499999997795377
                            },
                            {
                                'unit': { 'id': 'dW5pdDo4NDI0ODk=', 'name': 'batch' },
                                'value': 0.004166666662992295
                            },
                            {
                                'unit': { 'id': 'dW5pdDo5MjU0MjU=', 'name': 'min batch' },
                                'value': 0.024999999977953772
                            },
                            {
                                'unit': { 'id': 'dW5pdDo5MjU0MjY=', 'name': 'max batch' },
                                'value': 0.004166666662992295
                            }
                        ],
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': {
                                'externalName': None,
                                'id':'cmVjaXBlOjE4OTcwNA==',
                                'name': 'Olive Red Pepper & Cucumber Quinoa Pilaf',
                                'dietaryFlagsWithUsages': [],
                                "categoryValues": [
                                    {
                                        "id": "Y2F0ZWdvcnlWYWx1ZToxODQ3NA==",
                                        "name": "50",
                                        "category": {
                                            "id": "Y2F0ZWdvcnk6MzExOQ==",
                                            "name": "bin weight",
                                            "itemType": "recipe"
                                        }
                                    }
                                ],
                                'recipeInstructions': [
                                    {
                                        'position': 0,
                                        'text': 'Stage lexans for mixing. With sleeved gloves, mix the cucumber, red bell pepper, olives, hemp seeds, parsley and scallions in the quinoa being sure to distribute each ingredient evenly.'
                                    }
                                ],
                                'recipeTreeComponents': [
                                    {
                                        'quantity': 30,
                                        'unit': {
                                            'id': 'dW5pdDo0',
                                            'name': 'lb'
                                        },
                                        'ingredient': None,
                                        'recipeItem': {
                                            'subRecipe': {
                                                'id': 'cmVjaXBlOjE4ODYwNg==',
                                                'name': 'Cooked Rainbow Quinoa',
                                                'externalName': None,
                                                'dietaryFlagsWithUsages': [],
                                                'recipeInstructions': [
                                                    {
                                                        'position': 0,
                                                        'text': 'Bring water in tilt skillet to a boil. Add quinoa to tilt skillet, no more than 75 lbs at a time.'
                                                    },
                                                    {
                                                        'position': 1,
                                                        'text': 'Simmer, close lid, and cook until tender, stirring occasionally to prevent dry spots in the corners.'
                                                    },
                                                    {
                                                        'position': 2,
                                                        'text': 'After 10 minutes turn off heat and let steam for 5 minutes.'
                                                    },
                                                    {
                                                        'position': 3,
                                                        'text': 'Scoop quinoa onto sheet trays to cool down.'
                                                    }
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        'quantity': 7,
                                        'unit': {
                                            'id': 'dW5pdDo0',
                                            'name': 'lb'
                                        },
                                        'ingredient': {
                                            'id': 'aW5ncmVkaWVudDoyNDQ2Mzc=',
                                            'name': 'olives, kalamata, sliced',
                                            'externalName': 'Kalamata Olives',
                                            'dietaryFlags': []
                                        },
                                        'recipeItem': {
                                            'subRecipe': None
                                        }
                                    },
                                    {
                                        'quantity': 8,
                                        'unit': {
                                            'id': 'dW5pdDoz',
                                            'name': 'oz'
                                        },
                                        'ingredient': None,
                                        'recipeItem': {
                                            'subRecipe': {
                                                'id': 'cmVjaXBlOjE3Mjk2NQ==',
                                                'name': 'Sliced Scallion',
                                                'externalName': None,
                                                'dietaryFlagsWithUsages': [],
                                                'recipeInstructions': [
                                                    {
                                                        'position': 0,
                                                        'text': 'Pick off any stickers, twisty ties, or rubber bands from any bunched herbs.'
                                                    },
                                                    {
                                                        'position': 1,
                                                        'text': 'Using the 2 compartment sink, wash the produce well using a diluted veg wash solution.'
                                                    },
                                                    {
                                                        'position': 2,
                                                        'text': 'Once rinsed and visibly clean, strain onto perforated sheet trays.'
                                                    },
                                                    {
                                                        'position': 3,
                                                        'text': 'Let air dry on speed rack or spin dry using the electric spinner.'
                                                    },
                                                    {
                                                        'position': 4,
                                                        'text': 'Trim the tips of the scallions. Gather the scallions within your hand and line them up evenly slice across to make thin slices.'
                                                    },
                                                    {
                                                        'position': 5,
                                                        'text': 'Store in a cambro.'
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    {
                        'ingredient': None,
                        'quantity': 1.5,
                        'unit': {
                            'id': 'dW5pdDoz',
                            'name': 'oz'
                        },
                        'quantityUnitValues': [
                            {
                                'unit': { 'id': 'dW5pdDox', 'name': 'g' },
                                'value': 42.52428465
                            },
                            {
                                'unit': { 'id': 'dW5pdDoy', 'name': 'kg' },
                                'value': 0.04252428465
                            },
                            {
                                'unit': { 'id': 'dW5pdDoz', 'name': 'oz' },
                                'value': 1.5
                            },
                            {
                                'unit': { 'id': 'dW5pdDo0', 'name': 'lb' },
                                'value': 0.09374999991732665
                            },
                            {
                                'unit': { 'id': 'dW5pdDo5MjU0Mjc=', 'name': 'min batch' },
                                'value': 0.009374999991732665
                            },
                            {
                                'unit': { 'id': 'dW5pdDo5MjU0Mjg=', 'name': 'max batch' },
                                'value': 0.0015624999986221107
                            }
                        ],
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': {
                                'externalName': None,
                                'id': 'cmVjaXBlOjE3NjQ3Mw==',
                                'name': 'Tofu Feta',
                                'categoryValues': [],
                                'dietaryFlagsWithUsages': [
                                    {
                                        'dietaryFlag': {
                                            'id': 'ZGlldGFyeUZsYWc6Ng==',
                                            'name': 'soy beans'
                                        }
                                    }
                                ],
                                'recipeInstructions': [
                                    {
                                        'position': 0,
                                        'text': 'Stage clear polycarbonate lexans for mixing and add brine for tofu feta.'
                                    },
                                    {
                                        'position': 1,
                                        'text': 'Dice Tofu into small 1/4" diced bite sized squares and add to each lexan, mixing well with the brine for tofu feta, being sure all of the tofu is submerged.'
                                    },
                                    {
                                        'position': 2,
                                        'text': 'Let sit at least 4 hours, best overnight.'
                                    },
                                    {
                                        'position': 3,
                                        'text': 'Strain well before serving.'
                                    }
                                ],
                                'recipeTreeComponents': [
                                    {
                                        'quantity': 56,
                                        'unit': {
                                            'id': 'dW5pdDo0',
                                            'name': 'lb'
                                        },
                                        'ingredient': None,
                                        'recipeItem': {
                                            'subRecipe': {
                                                'id': 'cmVjaXBlOjE5MDA5MQ==',
                                                'name': 'Small Diced Tofu (1/4")',
                                                'externalName': None,
                                                'dietaryFlagsWithUsages': [
                                                    {
                                                        'dietaryFlag': {
                                                            'id': 'ZGlldGFyeUZsYWc6Ng==',
                                                            'name': 'soy beans'
                                                        }
                                                    }
                                                ],
                                                'recipeInstructions': [
                                                    {
                                                        'position': 0,
                                                        'text': 'Start by opening the bags of firm tofu over perforated lexans to strain any liquid.'
                                                    },
                                                    {
                                                        'position': 1,
                                                        'text': 'Dice the tofu into 1/4" pieces. Reserve in lexans.'
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ],
                            }
                        }
                    },
                    {
                        'ingredient': {
                            'externalName': 'Spring Mix Lettuce*',
                            'id': 'aW5ncmVkaWVudDoyNDQ1NjE=',
                            'name': 'lettuce, spring mix, SEND TO PLATE',
                            'categoryValues': [
                                {
                                    "id": "Y2F0ZWdvcnlWYWx1ZToxODQ3Mw==",
                                    "name": "30",
                                    "category": {
                                        "id": "Y2F0ZWdvcnk6MzExOA==",
                                        "name": "bin weight",
                                        "itemType": "ingredient"
                                    }
                                }
                            ],
                            'dietaryFlags': []
                        },
                        'quantity': 2.5,
                        'unit': {
                            'id': 'dW5pdDoz',
                            'name': 'oz'
                        },
                        'quantityUnitValues': [
                            {
                                'unit': { 'id': 'dW5pdDoz', 'name': 'oz' },
                                'value': 2.5
                            },
                            {
                                'unit': { 'id': 'dW5pdDo1', 'name': 'l' },
                                'value': 0.4657752582200901
                            },
                            {
                                'unit': { 'id': 'dW5pdDo2', 'name': 'ml' },
                                'value': 465.7752582200901
                            },
                            {
                                'unit': { 'id': 'dW5pdDo3', 'name': 'tsp' },
                                'value': 94.49841062091676
                            },
                            {
                                'unit': { 'id': 'dW5pdDo4', 'name': 'tbsp' },
                                'value': 31.49947027087968
                            },
                            {
                                'unit': { 'id': 'dW5pdDo0', 'name': 'lb' },
                                'value': 0.15624999986221108
                            }
                        ],
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': None
                        }
                    },
                    {
                        'ingredient': {
                            'externalName': 'Crispy Chickpeas (Chickpeas, Sunflower Oil, Sea Salt)',
                            'id': 'aW5ncmVkaWVudDoyNzQ4ODA=',
                            'name': 'crispy roasted chickpeas, 0.85 oz bag',
                            'categoryValues': [
                                {
                                    "id": "Y2F0ZWdvcnlWYWx1ZToxODQ3NQ==",
                                    "name": "40",
                                    "category": {
                                        "id": "Y2F0ZWdvcnk6MzExOA==",
                                        "name": "bin weight",
                                        "itemType": "ingredient"
                                    }
                                }
                            ],
                            'dietaryFlags': [
                                {
                                    'id': DietaryFlagEnum.SESAME_SEEDS.value,
                                    'name': 'sesame seeds'
                                },
                                {
                                    'id': DietaryFlagEnum.TREE_NUTS.value,
                                    'name': 'tree nuts'
                                }
                            ]
                        },
                        'quantity': 0.85,
                        'unit': {
                            'id': 'dW5pdDoz',
                            'name': 'oz'
                        },
                        'quantityUnitValues': [
                            {
                                'unit': { 'id': 'dW5pdDox', 'name': 'g'},
                                'value': 24.097094634999998
                            },
                            {
                                'unit': { 'id': 'dW5pdDoy', 'name': 'kg'},
                                'value': 0.024097094634999996
                            },
                            {
                                'unit': { 'id': 'dW5pdDoz', 'name': 'oz'},
                                'value': 0.85
                            },
                            {
                                'unit': { 'id': 'dW5pdDo0', 'name': 'lb'},
                                'value': 0.05312499995315176
                            },
                            {
                                'unit': { 'id': 'dW5pdDoxNA==', 'name': 'each'},
                                'value': 1
                            }
                        ],
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': None
                        }
                    }
                ]
            }
        }
    },
    {
        'quantity': 3,
        'unit': {
            'id': 'dW5pdDoz',
            'name': 'oz'
        },
        'quantityUnitValues': [
            {
                'unit': { 'id': 'dW5pdDoz', 'name': 'oz' },
                'value': 3
            },
            {
                'unit': { 'id': 'dW5pdDo0', 'name': 'lb' },
                'value': 0.1874999998346533
            },
            {
                'unit': { 'id': 'dW5pdDo5MzY4MzI=', 'name': 'max batch' },
                'value': 0.0018749999983465329
            },
            {
                'unit': { 'id': 'dW5pdDo5MzY4MzM=', 'name': 'min batch' },
                'value': 0.012499999988976886
            }
        ],
        'ingredient': None,
        'recipeItem': {
            'preparations': [],
            'subRecipe': {
                'externalName': None,
                'id': 'cmVjaXBlOjE3MDU4NA==',
                'name': 'Smashed Chickpea Salad - COOKED GARBANZOS',
                'recipeInstructions': [
                    {
                        'position': 0,
                        'text': 'The hobart must be used for this task, do not mix by hand.'
                    },
                    {
                        'position': 1,
                        'text': 'Latch bowl into the hobart, ensuring it is secured. While it is lowered, add in the garbanzo beans, lemon juice, and olive oil.'
                    },
                    {
                        'position': 2,
                        'text': 'Equip the PADDLE attachment, and patiently press the up arrow to rise the bowl until locked in place. Slide over the safeguard.'
                    },
                    {
                        'position': 3,
                        'text': 'Mix on Level 1 for 2 minutes to mash the beans.'
                    },
                    {
                        'position': 4,
                        'text': 'Slide the safeguard back, and add the remaining ingredients to the mixture. Mix again for 1 minute until fully combined, while pausing every now and then to scrape down the sides and bottom of bowl with a rubber spatula.'
                    },
                    {
                        'position': 5,
                        'text': 'Lower the bowl, unlatch and grab a buddy to help pour mixture into a lexan.'
                    },
                    {
                        'position': 6,
                        'text': 'Clean the entire machine after each project, take the bowl and attachments back to the dishpit.'
                    }
                ],
                'categoryValues': [
                    {
                        "id": "Y2F0ZWdvcnlWYWx1ZToxODQ3Ng==",
                        "name": "60",
                        "category": {
                            "id": "Y2F0ZWdvcnk6MzExOQ==",
                            "name": "bin weight",
                            "itemType": "recipe"
                        }
                    }
                ],
                'dietaryFlagsWithUsages': [],
                'recipeTreeComponents': [
                    {
                        'ingredient': {
                            'externalName': 'Sumac',
                            'id': 'aW5ncmVkaWVudDoyNDQ4MzQ=',
                            'name': 'spice sumac',
                            'categoryValues': [],
                            'dietaryFlags': []
                        },
                        'quantity': 0.75,
                        'unit': {
                            'id': 'dW5pdDoz',
                            'name': 'oz'
                        },
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': None
                        }
                    },
                    {
                        'ingredient': {
                            'externalName': 'Black Pepper',
                            'id': 'aW5ncmVkaWVudDoyNDQ3OTM=',
                            'name': 'spice, black pepper, ground',
                            'categoryValues': [],
                            'dietaryFlags': []
                        },
                        'quantity': 2,
                        'unit': {
                            'id': 'dW5pdDoz',
                            'name': 'oz'
                        },
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': None
                        }
                    },
                    {
                        'ingredient': None,
                        'quantity': 75,
                        'unit': {
                            'id': 'dW5pdDo0',
                            'name': 'lb'
                        },
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': {
                                'externalName': None,
                                'id': 'cmVjaXBlOjE3NjQ4MA==',
                                'name': 'Cooked Garbanzo Beans',
                                'categoryValues': [],
                                'dietaryFlagsWithUsages': [],
                                'recipeInstructions': [
                                    {
                                        'position': 0,
                                        'text': 'Start by straining and rinsing the beans. Sift through on sheet trays to make sure there aren’t any rocks, discolored beans, or any other foreign objects.'
                                    },
                                    {
                                        'position': 1,
                                        'text': 'Transfer the sifted beans to a tilt skillet, no more than 75# at a time. Cover with about a foot of water and bring to a boil by setting the temperature to high. Flavor the beans now with salt and the addition of a sachet of mirepoix.'
                                    },
                                    {
                                        'position': 2,
                                        'text': 'Once brought to a simmer, stir the beans and cover. Set a timer for 40 minutes and check in 5 minute increments afterwards for doneness. Season now with salt. To make sure the beans are cooked through, taste with a spoon. A cooked bean should be creamy on the inside with skin that is intact, not broken.'
                                    },
                                    {
                                        'position': 3,
                                        'text': 'Turn off the heat and pick out the sachet. Strain beans from their liquids to cool down on sheet trays.'
                                    }
                                ],
                                'recipeTreeComponents': [
                                    {
                                        'quantity': 5.125,
                                        'unit': {
                                            'id': 'dW5pdDo0',
                                            'name': 'lb'
                                        },
                                        'ingredient': None,
                                        'recipeItem': {
                                            'subRecipe': {
                                                'id': 'cmVjaXBlOjIwMjM5OA==',
                                                'name': 'Mirepoix Sachet',
                                                'externalName': None,
                                                'dietaryFlagsWithUsages': [],
                                                'recipeInstructions': [
                                                    {
                                                        'position': 0,
                                                        'text': 'Place the onion, carrot, celery, garlic heads, and bay leaves in the center of the square of cheesecloth. Gather the corners together to make a small pouch, tying it tightly with twine.'
                                                    },
                                                    {
                                                        'position': 1,
                                                        'text': 'Keep one length of the twine long enough to tie to one of the pot handles, for easy removal.'
                                                    }
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        'quantity': 75,
                                        'unit': {
                                            'id': 'dW5pdDo0',
                                            'name': 'lb'
                                        },
                                        'ingredient': {
                                            'id': 'aW5ncmVkaWVudDoyNDQyODE=',
                                            'name': 'beans, garbanzo, dry',
                                            'externalName': 'Garbanzo Beans',
                                            'dietaryFlags': []
                                        },
                                        'recipeItem': {
                                            'subRecipe': None
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    {
                        'ingredient': {
                            'externalName': 'Extra Virgin Olive Oil',
                            'id': 'aW5ncmVkaWVudDoyNDQ2MzA=',
                            'name': 'oil, olive',
                            'categoryValues': [],
                            'dietaryFlags': [],
                        },
                        'quantity': 6,
                        'unit': {
                            'id': 'dW5pdDo0',
                            'name': 'lb'
                        },
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': None
                        }
                    },
                    {
                        'ingredient': {
                            'externalName': 'Lemon Juice',
                            'id': 'aW5ncmVkaWVudDoyNDQ1MzU=',
                            'name': 'juice, lemon',
                            'categoryValues': [],
                            'dietaryFlags': []
                        },
                        'quantity': 6,
                        'unit': {
                            'id': 'dW5pdDo0',
                            'name': 'lb'
                        },
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': None
                        }
                    }
                ],
            }
        }
    },
    {
        'quantity': 2.3,
        'unit': {
            'id': 'dW5pdDoz',
            'name': 'oz'
        },
        'quantityUnitValues': [
            {
                'unit': { 'id': 'dW5pdDoz', 'name': 'oz' },
                'value': 2.3
            },
            {
                'unit': { 'id': 'dW5pdDo0', 'name': 'lb' },
                'value': 0.14374999987323417
            },
            {
                'unit': { 'id': 'dW5pdDoxNA==', 'name': 'each' },
                'value': 1
            },
            {
                'unit': { 'id': 'dW5pdDo3ODA1MzM=', 'name': 'case' },
                'value': 0.006666666666666667
            }
        ],
        'ingredient': {
            'id': 'aW5ncmVkaWVudDoyNDQ4OTQ=',
            'name': 'TS20 - 20oz Meal Boxes',
            'externalName': 'TS20',
            'dietaryFlags': [],
            'categoryValues': [
                {
                  'id': 'Y2F0ZWdvcnlWYWx1ZToxNDgwMg==',
                  'name': 'warehouse - packaging'
                },
                {
                  'id': IngredientCategoryValueEnum.FOOD_PACKAGE.value,
                  'name': 'food pkg'
                }
            ],
        },
        'recipeItem': {
            'preparations': [],
            'subRecipe': None
        }
    },
    {
        'quantity': 2,
        'unit': {
            'id': 'dW5pdDoz',
            'name': 'oz'
        },
         'quantityUnitValues': [
            {
                'unit': { 'id': 'dW5pdDox', 'name': 'g'},
                'value': 56.6990462
            },
            {
                'unit': { 'id': 'dW5pdDoy', 'name': 'kg'},
                'value': 0.0566990462
            },
            {
                'unit': { 'id': 'dW5pdDoz', 'name': 'oz'},
                'value': 2
            },
            {
                'unit': { 'id': 'dW5pdDo0', 'name': 'lb'},
                'value': 0.12499999988976886
            }
        ],
        'ingredient': None,
        'recipeItem': {
            'preparations': [
                {
                    'id': 'cHJlcGFyYXRpb246MzEwMjI=',
                    'name': '2 oz WINPAK'
                },
                {
                    'id': 'cHJlcGFyYXRpb246MjgzMzQ=',
                    'name': 'standalone'
                }
            ],
            'subRecipe': {
                'externalName': 'Red Wine Vinaigrette',
                'id': 'cmVjaXBlOjIyMzU3MQ==',
                'name': 'Red Wine Vinaigrette 2oz',
                'recipeInstructions': [],
                'categoryValues': [],
                'dietaryFlagsWithUsages': [],
                'recipeTreeComponents': [
                    {
                        'ingredient': None,
                        'quantity': 2,
                        'unit': {
                            'id': 'dW5pdDoz',
                            'name': 'oz'
                        },
                        'quantityUnitValues': [
                            {
                                'unit': { 'id': 'dW5pdDoz', 'name': 'oz' },
                                'value': 2
                            },
                            {
                                'unit': { 'id': 'dW5pdDo0', 'name': 'lb' },
                                'value': 0.12499999988976886
                            },
                            {
                                'unit': { 'id': 'dW5pdDo3NTU1MjQ=', 'name': 'batch' },
                                'value': 0.0020833333314961475
                            },
                            {
                                'unit': { 'id': 'dW5pdDo5MzUzMzg=', 'name': 'max batch' },
                                'value': 0.0020833333314961475
                            },
                            {
                                'unit': { 'id': 'dW5pdDo5MzUzMzk=', 'name': 'min batch' },
                                'value': 0.012499999988976886
                            }
                        ],
                        'recipeItem': {
                            'preparations': [],
                            'subRecipe': {
                                'externalName': None,
                                'id': 'cmVjaXBlOjE3NDI4OA==',
                                'name': 'Red Wine Vinaigrette BASE',
                                'categoryValues': [],
                                'dietaryFlagsWithUsages': [],
                                'recipeInstructions': [
                                    {
                                        'position': 0,
                                        'text': 'Please keep in mind the tamper seal from bottled containers can fall into the recipe you are making. Be sure to discard any tamper seals immediately after breaking the seal.'
                                    },
                                    {
                                        'position': 1,
                                        'text': 'In blixer combine half of the liquids to break up the red onion and garlic. Add the remaining liquids (except oil) and blend.'
                                    },
                                    {
                                        'position': 2,
                                        'text': 'Slowly add in oil through opening on the lid until emulsified.'
                                    },
                                    {
                                        'position': 3,
                                        'text': 'Pour into lexans.'
                                    }
                                ],
                                'recipeTreeComponents': []
                            }
                        }
                    }
                ]
            }
        }
    }
]


mock_formatted_primaryRecipeComponents = [
    {
        'type': 'recipe',
        'id': 'cmVjaXBlOjE4OTcwNA==',
        'name': 'Olive Red Pepper & Cucumber Quinoa Pilaf',
        'allergens': [],
        'usage': {
            'value': 4,
            'unit': 'oz'
        },
        'quantity': {
            'value': 0.2499999997795377,
            'unit': 'lb'
        },
        'binWeight': {
            'value': 50.0,
            'unit': 'lb'
        },
        'instructions':  [
            {
                'id': 1,
                'text': 'Stage lexans for mixing. With sleeved gloves, mix the cucumber, red bell pepper, olives, hemp seeds, parsley and scallions in the quinoa being sure to distribute each ingredient evenly.'
            }
        ],
        'recipeComponents': [
            {
                'type': 'recipe',
                'id': 'cmVjaXBlOjE4ODYwNg==',
                'name': 'Cooked Rainbow Quinoa',
                'allergens': [],
                'usage': {
                    'value': 30,
                    'unit': 'lb'
                }
            },
            {
                'type': 'ingredient',
                'id': 'aW5ncmVkaWVudDoyNDQ2Mzc=',
                'name': 'olives, kalamata, sliced',
                'allergens': [],
                'usage': {
                    'value': 7,
                    'unit': 'lb'
                }
            },
            {
                'type': 'recipe',
                'id': 'cmVjaXBlOjE3Mjk2NQ==',
                'name': 'Sliced Scallion',
                'allergens': [],
                'usage': {
                    'value': 8,
                    'unit': 'oz'
                }
            },
        ],
    },
    {
        'type': 'recipe',
        'id': 'cmVjaXBlOjE3NjQ3Mw==',
        'name': 'Tofu Feta',
        'allergens': ['soy'],
        'usage': {
            'value': 1.5,
            'unit': 'oz'
        },
        'quantity': {
            'value': 0.09374999991732665,
            'unit': 'lb'
        },
        'binWeight': {
            'value': 60.0,
            'unit': 'lb'
        },
        'instructions': [
            {
                'id': 1,
                'text': 'Stage clear polycarbonate lexans for mixing and add brine for tofu feta.'
            },
            {
                'id': 2,
                'text': 'Dice Tofu into small 1/4" diced bite sized squares and add to each lexan, mixing well with the brine for tofu feta, being sure all of the tofu is submerged.'
            },
            {
                'id': 3,
                'text': 'Let sit at least 4 hours, best overnight.'
            },
            {
                'id': 4,
                'text': 'Strain well before serving.'
            }
        ],
        'recipeComponents': [
            {
                'type': 'recipe',
                'id': 'cmVjaXBlOjE5MDA5MQ==',
                'name': 'Small Diced Tofu (1/4")',
                'allergens': ['soy'],
                'usage': {
                    'value': 56,
                    'unit': 'lb'
                }
            }
        ],
    },
    {
        'type': 'ingredient',
        'id': 'aW5ncmVkaWVudDoyNDQ1NjE=',
        'name': 'Spring Mix Lettuce*',
        'allergens': [],
        'usage': {
            'value': 2.5,
            'unit': 'oz'
        },
        'quantity': {
            'value': 0.15624999986221108,
            'unit': 'lb'
        },
        'binWeight': {
            'value': 30.0,
            'unit': 'lb'
        }
    },
    {
        'type': 'ingredient',
        'id': 'aW5ncmVkaWVudDoyNzQ4ODA=',
        'name': 'Crispy Chickpeas (Chickpeas, Sunflower Oil, Sea Salt)',
        'allergens': ['sesame_seeds', 'tree_nuts'],
        'usage': {
            'value': 0.85,
            'unit': 'oz'
        },
        'quantity': {
            'value': 0.05312499995315176,
            'unit': 'lb'
        },
        'binWeight': {
            'value': 40.0,
            'unit': 'lb'
        },
    },
    {
        'type': 'recipe',
        'id': 'cmVjaXBlOjE3MDU4NA==',
        'name': 'Smashed Chickpea Salad - COOKED GARBANZOS',
        'allergens': [],
        'usage': {
            'value': 3,
            'unit': 'oz'
        },
        'quantity': {
            'value': 0.1874999998346533,
            'unit': 'lb'
        },
        'binWeight': {
            'value': 60.0,
            'unit': 'lb'
        },
        'instructions': [
            {
                'id': 1,
                'text': 'The hobart must be used for this task, do not mix by hand.'
            },
            {
                'id': 2,
                'text': 'Latch bowl into the hobart, ensuring it is secured. While it is lowered, add in the garbanzo beans, lemon juice, and olive oil.'
            },
            {
                'id': 3,
                'text': 'Equip the PADDLE attachment, and patiently press the up arrow to rise the bowl until locked in place. Slide over the safeguard.'
            },
            {
                'id': 4,
                'text': 'Mix on Level 1 for 2 minutes to mash the beans.'
            },
            {
                'id': 5,
                'text': 'Slide the safeguard back, and add the remaining ingredients to the mixture. Mix again for 1 minute until fully combined, while pausing every now and then to scrape down the sides and bottom of bowl with a rubber spatula.'
            },
            {
                'id': 6,
                'text': 'Lower the bowl, unlatch and grab a buddy to help pour mixture into a lexan.'
            },
            {
                'id': 7,
                'text': 'Clean the entire machine after each project, take the bowl and attachments back to the dishpit.'
            }
        ],
        'recipeComponents': [
            {
                'type': 'ingredient',
                'id': 'aW5ncmVkaWVudDoyNDQ4MzQ=',
                'name': 'spice sumac',
                'allergens': [],
                'usage': {
                    'value': 0.75,
                    'unit': 'oz'
                }
            },
            {
                'type': 'ingredient',
                'id': 'aW5ncmVkaWVudDoyNDQ3OTM=',
                'name': 'spice, black pepper, ground',
                'allergens': [],
                'usage': {
                    'value': 2,
                    'unit': 'oz'
                }
            },
            {
                'type': 'recipe',
                'id': 'cmVjaXBlOjE3NjQ4MA==',
                'name': 'Cooked Garbanzo Beans',
                'allergens': [],
                'usage': {
                    'value': 75,
                    'unit': 'lb'
                }
            },
            {
                'type': 'ingredient',
                'id': 'aW5ncmVkaWVudDoyNDQ2MzA=',
                'name': 'oil, olive',
                'allergens': [],
                'usage': {
                    'value': 6,
                    'unit': 'lb'
                }
            },
            {
                'type': 'ingredient',
                'id': 'aW5ncmVkaWVudDoyNDQ1MzU=',
                'name': 'juice, lemon',
                'allergens': [],
                'usage': {
                    'value': 6,
                    'unit': 'lb'
                }
            },
        ],
    },
    {
        'type': 'recipe',
        'id': 'cmVjaXBlOjIyMzU3MQ==',
        'name': 'Red Wine Vinaigrette',
        'allergens': [],
        'usage': {
            'value': 2,
            'unit': 'oz'
        },
        'quantity': {
            'value': 0.12499999988976886,
            'unit': 'lb'
        },
        'binWeight': {
            'value': 60,
            'unit': 'lb'
        },
        'instructions': [],
        'recipeComponents': [
            {
                'type': 'recipe',
                'id': 'cmVjaXBlOjE3NDI4OA==',
                'name': 'Red Wine Vinaigrette BASE',
                'allergens': [],
                'usage': {
                    'value': 2,
                    'unit': 'oz'
                }
            }
        ],
    }
]


def mock_ops_menu(date, location_name='Vacaville', menu_type='production'):
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
                        'recipeTreeComponents': mock_recipeTreeComponents
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
                        'recipeTreeComponents': mock_recipeTreeComponents
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
                        'recipeTreeComponents': mock_recipeTreeComponents
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
                        'recipeTreeComponents': mock_recipeTreeComponents
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
                        'recipeTreeComponents': mock_recipeTreeComponents
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
                        'recipeTreeComponents': mock_recipeTreeComponents
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
                        'recipeTreeComponents': mock_recipeTreeComponents
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

