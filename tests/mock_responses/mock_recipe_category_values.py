from galley.enums import RecipeCategoryTagTypeEnum


mock_data = [
    {
        'name': 'vegan',
        'category': {
            'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
            'itemType': 'recipe',
            'name': 'protein type'
        }
    },
    {
        'name': 'ts48',
        'category': {
            'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
            'itemType': 'recipe',
            'name': 'meal container'
        }
    },
    {
        'name': 'dinner',
        'category': {
            'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
            'itemType': 'recipe',
            'name': 'meal type'
        }
    },
    {
        'name': 'true',
        'category': {
            'id': "",
            'itemType': 'recipe',
            'name': 'is perishable'
        }
    },
    {
        'name': 'high-protein-legume',
        'category': {
            'id': RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value,
            'itemType': 'recipe',
            'name': 'protein addon'
        }
    },
    {
        'name': 'base-salad',
        'category': {
            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
            'itemType': 'recipe',
            'name': 'base meal slug'
        }
    },
    {
        'name': 'Base Salad Name',
        'category': {
            'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
            'itemType': 'recipe',
            'name': 'base meal'
        }
    },
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
]
