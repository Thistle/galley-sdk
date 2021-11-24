from galley.enums import PreparationEnum


mock_data = [
    {
        'ingredient': None,
        'subRecipe': {
        'allIngredients': [
            'Unique 1',
            'Duplicate 1',
            'Duplicate 2',
            'Duplicate 3'
        ]
        },
        'preparations': []
    },
    {
        'ingredient': None,
        'subRecipe': {
        'allIngredients': [
            'Unique 2',
            'Duplicate 1',
            'Duplicate 2'
        ]
        },
        'preparations': []
    },
    {
        'ingredient': None,
        'subRecipe': {
            'allIngredients': [
                'Unique 3',
                'Duplicate 2',
                'Duplicate 3'
            ]
        },
        'preparations': [
            {
                'name': '2 oz RAM'
            },
            {
                'id': PreparationEnum.STANDALONE.value,
                'name': 'standalone'
            }
        ]
    },
    {
        'ingredient': {
        'externalName': 'Unique 4',
        'categoryValues': [
            {
                'name': 'send to plate',
                'category': {
                    'itemType': 'ingredient'
                }
            },
            {
                'name': None,           # Test empty categoryValue['name']
                'category': {
                    'itemType': None    # Test empty category['itemType']
                }
            }
        ]
        },
        'subRecipe': None,
        'preparations': [
        {
            'name': None            # Test empty preparations['name']
        }
        ]
    },
    {
        'ingredient': {
        'externalName': '32 oz Meal Boxes',
        'categoryValues': [
            {
            'name': 'food pkg',
            'category': {
                'itemType': 'ingredient'
            }
            }
        ]
        },
        'subRecipe': None,
        'preparations': []
    },

    # Test empty recipeItem
    {
        'ingredient': None,
        'subRecipe': None,
        'preparations': []
    }
]
