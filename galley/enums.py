from enum import Enum


class LocationEnum(Enum):
    """
    Enum for locations. <location name>: <location id>
    """
    VACAVILLE = 'bG9jYXRpb246MTkyOA=='
    BURLINGTON = 'bG9jYXRpb246Mzg1MQ=='


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
    CORE_RECIPE = 'cHJlcGFyYXRpb246MzEzNjk='
    STANDALONE = 'cHJlcGFyYXRpb246MjgzMzQ='
    INSERT = 'cHJlcGFyYXRpb246MjgyNzE='
    INSERT12 = 'cHJlcGFyYXRpb246MjgzODE='
    TWO_OZ_RAM = 'cHJlcGFyYXRpb246MjgxMTU='
    FOUR_OZ_RAM = 'cHJlcGFyYXRpb246MzAwMzE='
    THREE_OZ_RAM = 'cHJlcGFyYXRpb246MjgxMTQ='
    TWO_OZ_WINPAK = 'cHJlcGFyYXRpb246MzEwMjI='
    TWELVE_OZ_ROUND_INSERT = 'cHJlcGFyYXRpb246Mjg2MDY='
    DELIVER_TO_PRODUCTION = 'cHJlcGFyYXRpb246MTY1MTIy'
    DELIVER_TO_WASH = 'cHJlcGFyYXRpb246MTY1MTIz'


class ContainerEnum(set, Enum):  # type: ignore
    CUPPING = {
        PreparationEnum.INSERT,
        PreparationEnum.INSERT12,
        PreparationEnum.TWO_OZ_RAM,
        PreparationEnum.FOUR_OZ_RAM,
        PreparationEnum.THREE_OZ_RAM,
        PreparationEnum.TWO_OZ_WINPAK,
        PreparationEnum.TWELVE_OZ_ROUND_INSERT
    }

    @property
    def values(self):
        return set(enum.value for enum in self)


class IngredientCategoryValueEnum(Enum):
    """
    Enum for Ingredient CategoryValues. <categoryValue name>: <categoryValue id>
    """
    FOOD_PACKAGE = 'Y2F0ZWdvcnlWYWx1ZToxNDAxNQ=='
    LABEL = 'Y2F0ZWdvcnlWYWx1ZToyMjI3OA=='


class IngredientCategoryTagTypeEnum(Enum):
    """
    Enum for category tag types at ingredient (itemType) level. <category name>: <category id>
    """
    ACCOUNTING_TAG = 'Y2F0ZWdvcnk6MjQyMA=='
    # ingredient only tag, separate value used for recipe bin weight
    BIN_WEIGHT_TAG = 'Y2F0ZWdvcnk6MzExOA=='


class RecipeCategoryTagTypeEnum(Enum):
    """
    Enum for category tag types at recipe (itemType) level. <category name>: <category id>
    """
    PROTEIN_TYPE_TAG = 'Y2F0ZWdvcnk6MjUwOA=='
    MEAL_TYPE_TAG = 'Y2F0ZWdvcnk6MjQyMg=='
    MEAL_CONTAINER_TAG = 'Y2F0ZWdvcnk6MjU2Nw=='
    PROTEIN_ADDON_TAG = 'Y2F0ZWdvcnk6MjU4MQ=='
    BASE_MEAL_SLUG_TAG = 'Y2F0ZWdvcnk6MjYyMA=='
    BASE_MEAL_TAG = 'Y2F0ZWdvcnk6MjU4OQ=='
    HIGHLIGHT_ONE_TAG = 'Y2F0ZWdvcnk6MjU3OA=='
    HIGHLIGHT_TWO_TAG = 'Y2F0ZWdvcnk6MzA0OQ=='
    NO_NUTRITION_ON_WEBSITE_TAG = 'Y2F0ZWdvcnk6MzA2Ng=='
    # recipe only tag, separate value used for ingredient bin weight
    BIN_WEIGHT_TAG = 'Y2F0ZWdvcnk6MzExOQ=='


class EntityMediaEnum(Enum):
    """
    Enum for EntityMedia. <field name>: <field value>
    """
    MENU_CAPTION = 'menu'
    PLATE_CAPTION = 'plating'


class DietaryFlagEnum(Enum):
    # Enum for Dietary Flags
    # TODO: Remove or update the ids from the
    # enum since these are currently outdated
    BEEF = ('ZGlldGFyeUZsYWc6MTM3', 'beef')
    CELERY = ('ZGlldGFyeUZsYWc6MTA=', 'celery')
    COCONUT = ('ZGlldGFyeUZsYWc6OTc=', 'coconut')
    CRUSTANCEANS = ('ZGlldGFyeUZsYWc6MTQ=', 'crustaceans')
    EGGS = ('ZGlldGFyeUZsYWc6Mw==', 'eggs')
    FISH = ('ZGlldGFyeUZsYWc6Nw==', 'fish')
    GLUTEN = ('ZGlldGFyeUZsYWc6MTE=', 'gluten')
    LAMB = ('ZGlldGFyeUZsYWc6MTM1', 'lamb')
    LUPIN = ('ZGlldGFyeUZsYWc6MTI=', 'lupin')
    MILK = ('ZGlldGFyeUZsYWc6MQ==', 'milk')
    MOLLUSCS = ('ZGlldGFyeUZsYWc6MTM=', 'molluscs')
    MUSTARD = ('ZGlldGFyeUZsYWc6MTU=', 'mustard')
    NON_VEGAN = ('ZGlldGFyeUZsYWc6OTk=', 'non vegan')
    PEANUTS = ('ZGlldGFyeUZsYWc6NA==', 'peanuts')
    PORK = ('ZGlldGFyeUZsYWc6OTg=', 'pork')
    SESAME = ('ZGlldGFyeUZsYWc6MzI4', 'sesame')
    SESAME_SEEDS = ('ZGlldGFyeUZsYWc6MTY=', 'sesame seeds')
    SHELLFISH = ('ZGlldGFyeUZsYWc6OA==', 'shellfish')
    SMOKED_MEATS = ('ZGlldGFyeUZsYWc6MTM2', 'smoked meats')
    SOYBEANS = ('ZGlldGFyeUZsYWc6Ng==', 'soybeans')
    SULPHITES = ('ZGlldGFyeUZsYWc6MTc=', 'sulphites')
    TREE_NUTS = ('ZGlldGFyeUZsYWc6NQ==', 'tree nuts')
    WHEAT = ('ZGlldGFyeUZsYWc6Mg==', 'wheat')

    @property
    def id(self):
        return self.value[0]

    @property
    def name(self):
        return self.value[1]


class UnitEnum(Enum):
    EACH = 'dW5pdDoxNA=='
    OZ = 'dW5pdDoz'
    LB = 'dW5pdDo0'
    G = 'dW5pdDox'
