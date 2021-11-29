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
