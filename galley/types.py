from os import name
from sgqlc.types import (
    ID,
    ArgDict,
    Enum,
    Field,
    Input,
    Int,
    Type,
    datetime as d,
    list_of
)


class CategoryItemTypeEnum(Enum):
    __choices__ = ('menuItem',
                   'ingredient',
                   'recipe',
                   'menu',
                   'vendorItem',
                   'purchaseOrder')


class Category(Type):
    id = Field(ID)
    name = str
    itemType = Field(CategoryItemTypeEnum)


class CategoryValue(Type):
    id = Field(ID)
    name = str
    category = Field(Category)


class Unit(Type):
    id = Field(ID)
    name = Field(str)


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


class Ingredient(Type):
    externalName = str
    categoryValues = Field(CategoryValue)


class SubRecipe(Type):
    id = Field(ID)
    allIngredients = str
    name = str
    externalName = str
    reconciledNutritionals = Field(Nutrition)



class Preparation(Type):
    id = Field(ID)
    name = str


class RecipeItem(Type):
    ingredient = Field(Ingredient)
    subRecipe = Field(SubRecipe)
    subRecipeId = str
    preparations = Field(Preparation)
    quantity = float
    unit = Field(Unit)


class UnitValue(Type):
    value = float
    unit = Field(Unit)


class RecipeTreeComponent(Type):
    id = Field(ID)
    quantityUnitValues = Field(UnitValue)
    recipeItem = Field(RecipeItem)


class Recipe(Type):
    id = str
    name = str
    externalName = str
    instructions = str
    notes = str
    description = str
    recipeTreeComponents = Field(RecipeTreeComponent, args=ArgDict(levels=list_of(Int)))
    reconciledNutritionals = Field(Nutrition)
    categoryValues = Field(CategoryValue)
    recipeItems = Field(RecipeItem)


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


class UnitInput(Input):
    name = str


class MenuItem(Type):
    id = str
    recipeId = str
    categoryValues = Field(CategoryValue)
    recipe = Field(Recipe)
    unit = Field(Unit)


class Menu(Type):
    id = str
    name = str
    date = d.Date
    location = Field(Location)
    menuItems = Field(MenuItem)
    categoryValues = Field(CategoryValue)


class MenuPayload(Type):
    menus = Field(Menu)


class MenuItemInput(Input):
    id = str
    recipeId = str
    volume = float
    unit = UnitInput


class MenuInput(Input):
    id = str
    recipeId = str
    menuItems = Field(list_of(MenuItemInput))

class BulkMenusInput(Input):
    menus = Field(list_of(MenuInput))


class FilterInput(Input):
    id = ID
    name = list_of(str)


class MenuFilterInput(Input):
    id = ID
    date = list_of(d.Date)
