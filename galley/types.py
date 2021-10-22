from sgqlc.types import Field, Type, Input, datetime as d, Enum


class Nutrition(Type):
    addedSugarG = float
    calciumMg = float
    calciumPercentRDI = float
    caloriesKCal = float
    carbsG = float
    carbsPercentDRV = float
    cholesterolMg = float
    cholesterolPercentDRV = float
    copperMg = float
    copperPercentRDI = float
    fiberG = float
    fiberPercentDRV = float
    folateMcg = float
    folatePercentRDI = float
    ironMg = float
    ironPercentRDI = float
    magnesiumMg = float
    magnesiumPercentRDI = float
    manganeseMg = float
    manganesePercentRDI = float
    niacinMg = float
    niacinPercentRDI = float
    pantothenicAcidMg = float
    phosphorusMg = float
    phosphorusPercentRDI = float
    potassiumMg = float
    potassiumPercentRDI = float
    proteinG = float
    proteinPercentRDI = float
    riboflavinMg = float
    riboflavinPercentRDI = float
    saturatedFatG = float
    seleniumMcg = float
    seleniumPercentRDI = float
    sodiumMg = float
    sodiumPercentDRV = float
    sugarG = float
    sugarPercentDRV = float
    thiaminMg = float
    thiaminPercentRDI = float
    totalFatG = float
    totalFatPercentDRV = float
    transFatG = float
    vitaminAMcg = float
    vitaminAPercentRDI = float
    vitaminB12Mcg = float
    vitaminB12PercentRDI = float
    vitaminB6Mg = float
    vitaminB6PercentRDI = float
    vitaminCMg = float
    vitaminCPercentRDI = float
    vitaminDMcg = float
    vitaminDPercentRDI = float
    vitaminEMg = float
    vitaminEPercentRDI = float
    vitaminKMcg = float
    vitaminKPercentRDI = float
    zincMg = float
    zincPercentRDI = float


class Recipe(Type):
    id = str
    externalName = str
    instructions = str
    notes = str
    description = str
    reconciledNutritionals = Field(Nutrition)


class RecipeInstruction(Type):
    id = str
    text = str
    position = int
    recipeId = str


class InstructionInput(Input):
    text = str
    position = int


class RecipeInstructionInput(Input):
    recipeId = str
    recipeInstruction = InstructionInput


class RecipeInstructionPayload(Type):
    recipeInstruction = Field(RecipeInstruction)


class Location(Type):
    name = str


class CategoryItemTypeEnum(Enum):
    __choices__ = ('menuItem',
                   'ingredient',
                   'recipe',
                   'menu',
                   'vendorItem',
                   'purchaseOrder')


class Category(Type):
    name = str
    itemType = Field(CategoryItemTypeEnum)


class CategoryValue(Type):
    name = str
    category = Field(Category)


class MenuItem(Type):
    recipeId = str
    categoryValues = Field(CategoryValue)


class Menu(Type):
    id = str
    name = str
    date = d.Date
    location = Field(Location)
    menuItems = Field(MenuItem)


class MenuNameInput(Input):
    name = str