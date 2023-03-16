from galley.common import DEFAULT_MENU_TYPE
from galley.enums import MenuCategoryEnum, RecipeCategoryTagTypeEnum


MEAL_TYPE_CATEGORY_VALUE = {
    'name': 'dinner',
    'category': {
        'id': RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value,
        'itemType': 'recipe',
        'name': 'meal type'
    }
}

BASE_MEAL_CATEGORY_VALUE = {
    'name': 'Base Salad Name',
    'category': {
        'id': RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value,
        'itemType': 'recipe',
        'name': 'base meal'
    }
}

PROTEIN_TYPE_CATEGORY_VALUE = {
    'name': 'vegan',
    'category': {
        'id': RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value,
        'itemType': 'recipe',
        'name': 'protein type'
    }
}

PROTEIN_ADDON_CATEGORY_VALUE = {
    'name': 'high-protein-legume',
    'category': {
        'id': RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value,
        'itemType': 'recipe',
        'name': 'protein addon'
    }
}

HIGHLIGHT_ONE_CATEGORY_VALUE = {
    'name': 'new',
    'category': {
        'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_ONE_TAG.value,
        'itemType': 'recipe',
        'name': 'highlight_1'
    }
}

HIGHLIGHT_TWO_CATEGORY_VALUE = {
    'name': 'spicy',
    'category': {
        'id': RecipeCategoryTagTypeEnum.HIGHLIGHT_TWO_TAG.value,
        'itemType': 'recipe',
        'name': 'highlight_2'
    }
}

MISCELLANEOUS_CATEGORY_VALUE = {
    'name': 'true',
    'category': {
        'id': "",
        'itemType': 'recipe',
        'name': 'is perishable'
    }
}

MEAL_CONTAINER_CATEGORY_VALUE = {
    'name': 'ts48',
    'category': {
        'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value,
        'itemType': 'recipe',
        'name': 'meal container'
    }
}

BASE_MEAL_SLUG_CATEGORY_VALUE = {
    'name': 'base-salad',
    'category': {
        'id': RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value,
        'itemType': 'recipe',
        'name': 'base meal slug'
    }
}

MOCK_RECIPE_CATEGORY_VALUES = [
    MEAL_TYPE_CATEGORY_VALUE,
    BASE_MEAL_CATEGORY_VALUE,
    PROTEIN_TYPE_CATEGORY_VALUE,
    PROTEIN_ADDON_CATEGORY_VALUE,
    HIGHLIGHT_ONE_CATEGORY_VALUE,
    HIGHLIGHT_TWO_CATEGORY_VALUE,
    MISCELLANEOUS_CATEGORY_VALUE,
    MEAL_CONTAINER_CATEGORY_VALUE,
    BASE_MEAL_SLUG_CATEGORY_VALUE,
]
