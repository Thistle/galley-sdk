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


class IngredientCategoryEnum(Enum):
    """
    Enum for Ingredient Categories. <category name>: <category id>
    """
    FOOD_PACKAGE = "Y2F0ZWdvcnlWYWx1ZToxNDAxNQ=="

class TagTypeEnum(Enum):
    """
    """
    CATEGORY_TAG_TYPE = "Y2F0ZWdvcnk6MjQyMA=="
