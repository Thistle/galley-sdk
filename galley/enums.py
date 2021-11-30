from enum import Enum


class MenuCategoryEnum(Enum):
    """
    Enum for categories, for item type menu <category name>: <category id>
    """
    MENU_TYPE = 'Y2F0ZWdvcnk6MjQ2NQ=='

class MenuItemCategoryEnum(Enum):
    """
    Enum for categories, for item type menu item <category name>: <category id>
    """
    PRODUCT_CODE = 'Y2F0ZWdvcnk6MjQ2Nw=='

class PreparationEnum(Enum):
    """
    Enum for preparations.  <preparation name>: <preparation id>
    """
    STANDALONE = 'cHJlcGFyYXRpb246MjgzMzQ='
    TWO_OUNCE_RAM = 'cHJlcGFyYXRpb246MjgxMTU='
    THREE_OUNCE_RAM = 'cHJlcGFyYXRpb246MjgxMTQ='


class IngredientCategoryValueEnum(Enum):
    """
    Enum for Ingredient CategoryValues. <categoryValue name>: <categoryValue id>
    """
    FOOD_PACKAGE = 'Y2F0ZWdvcnlWYWx1ZToxNDAxNQ=='


class IngredientCategoryTagTypeEnum(Enum):
    """
    Enum for category tag types at ingredient (itemType) level. <category name>: <category id>
    """
    ACCOUNTING_TAG = 'Y2F0ZWdvcnk6MjQyMA=='


class RecipeCategoryTagTypeEnum(Enum):
    """
    Enum for category tag types at recipe (itemType) level. <category name>: <category id>
    """
    PROTEIN_TYPE_TAG = 'Y2F0ZWdvcnk6MjUwOA=='
    MEAL_TYPE_TAG = 'Y2F0ZWdvcnk6MjQyMg=='
    MEAL_CONTAINER_TAG = 'Y2F0ZWdvcnk6MjU2Nw=='
    PROTEIN_ADDON_TAG = 'Y2F0ZWdvcnk6MjU4MQ=='
    BASE_MEAL_SLUG_TAG = 'Y2F0ZWdvcnk6MjYyMA=='

