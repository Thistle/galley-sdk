from sgqlc.types import (ID, ArgDict, Enum, Field, Input, Int, Type, datetime
                         as d, list_of)
from sgqlc.types.relay import (Connection, Node)


class CategoryItemTypeEnum(Enum):
    __choices__ = ('menuItem', 'ingredient', 'recipe', 'menu', 'vendorItem', 'purchaseOrder')


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
    id = Field(ID)
    name = str
    externalName = str
    categoryValues = Field(CategoryValue)
    dietaryFlags = Field('DietaryFlag')


class RecipeInstruction(Type):
    text = str
    position = int


class Preparation(Type):
    id = Field(ID)
    name = str


class UnitValue(Type):
    value = float
    unit = Field(Unit)


class RecipeTreeComponent(Type):
    id = Field(ID)
    quantity = float
    unit = Field(Unit)
    quantityUnitValues = Field(UnitValue)
    ingredient = Field(Ingredient)
    recipeItem = Field('RecipeItem')


class SubRecipe(Type):
    id = Field(ID)
    allIngredients = str
    name = str
    externalName = str
    reconciledNutritionals = Field(Nutrition)
    nutritionalsQuantity = float
    nutritionalsUnit = Field(Unit)
    recipeInstructions = Field(RecipeInstruction)
    recipeTreeComponents = Field(RecipeTreeComponent, args=ArgDict(levels=list_of(Int)))
    dietaryFlagsWithUsages = Field('DietaryFlagsWithUsages')
    categoryValues = Field(CategoryValue)


class RecipeItem(Type):
    id = ID
    recipe = Field("Recipe")
    ingredient = Field(Ingredient)
    subRecipe = Field(SubRecipe)
    recipeId = str
    subRecipeId = str
    preparations = Field(Preparation)
    quantity = float
    unit = Field(Unit)
    reconciledNutritionals = Field(Nutrition)


class RecipeMedia(Type):
    altText = str
    caption = str
    sourceUrl = str


class EntityMedia(Type):
    caption = str
    sourceUrl = str


class Files(Type):
    photos = Field(EntityMedia)


class DietaryFlag(Type):
    id = str
    name = str


class DietaryFlagsWithUsages(Type):
    dietaryFlag = Field(DietaryFlag)


class PageInfoType(Type):
    endIndex = int
    hasNextPage = bool
    hasPreviousPage = bool
    startIndex = int


class VersionNode(Node):
    id = Field(ID)


class RecipeVersionConnectionEdge(Type):
    node = Field(VersionNode)


class RecipeVersionConnection(Connection):
    edges = Field(RecipeVersionConnectionEdge)
    pageInfo = Field(PageInfoType)
    totalCount = int


class Recipe(Type):
    id = str
    name = str
    externalName = str
    instructions = str
    recipeInstructions = Field(RecipeInstruction)
    notes = str
    description = str
    recipeTreeComponents = Field(RecipeTreeComponent, args=ArgDict(levels=list_of(Int)))
    reconciledNutritionals = Field(Nutrition)
    versionConnection = Field(RecipeVersionConnection)
    categoryValues = Field(CategoryValue)
    recipeItems = Field(RecipeItem)
    media = Field(RecipeMedia)
    files = Field(Files)
    isDish = bool
    totalYield = float
    dietaryFlagsWithUsages = Field(DietaryFlagsWithUsages)
    parentRecipeItems = Field(list_of(RecipeItem))


class SortDirection(str, Enum):
    asc = 'asc'
    desc = 'desc'


class PaginationOptions(Input):
    first = int
    orderBy = str
    sortDirection = SortDirection
    startIndex = int


class RecipeNode(Node):
    id = str
    name = str
    externalName = str
    instructions = str
    notes = str
    description = str
    recipeTreeComponents = Field(RecipeTreeComponent, args=ArgDict(levels=list_of(Int)))
    reconciledNutritionals = Field(Nutrition)
    versionConnection = Field(RecipeVersionConnection, args=ArgDict({'paginationOptions': PaginationOptions}))
    categoryValues = Field(CategoryValue)
    recipeItems = Field(RecipeItem)
    media = Field(RecipeMedia)
    dietaryFlagsWithUsages = Field(DietaryFlagsWithUsages)


class RecipeEdge(Type):
    node = Field(RecipeNode)


class RecipeConnection(Connection):
    edges = list_of(RecipeEdge)
    pageInfo = Field(PageInfoType)
    totalCount = int


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
    volume = float


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
    id = list_of(ID)
    name = list_of(str)


class MenuFilterInput(Input):
    id = ID
    date = list_of(d.Date)


class RecipeConnectionFilter(Input):
    id = list_of(str)


class RecipeItemInput(Input):
    preparationIds = Field(list_of(str))


class BulkUpdateRecipeItemsInput(Input):
    ids = Field(list_of(ID))
    attrs = Field(RecipeItemInput)


class BulkUpdateRecipeItemsPayload(Type):
    recipeItems = Field(list_of(RecipeItem))


class RecipeItemConnectionEdge(Type):
    index = int
    node = Field(RecipeItem)


class RecipeItemConnectionOrderByEnum(Enum):
    __choices__ = ('CreatedAt', 'RecipeName')


class SortDirectionEnum(Enum):
    __choices__ = ('asc', 'desc')


class RecipeItemConnection(Connection):
    edges = list_of(RecipeItemConnectionEdge)
    pageInfo = Field(PageInfoType)
    totalCount = int


class RecipeItemConnectionFilter(Input):
    ingredients = list_of(str)
    recipeIds = list_of(str)
    subRecipeIds = list_of(str)


class RecipeItemConnectionPaginationOptions(Input):
    first = int
    orderBy = RecipeItemConnectionOrderByEnum
    sortDirection = SortDirectionEnum
    startIndex = int
