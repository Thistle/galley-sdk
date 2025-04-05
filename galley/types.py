from sgqlc.types import ID, ArgDict, Enum, Field, Input, Int, Type, datetime as d, list_of
from sgqlc.types.relay import Connection, Node


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


class UnitValue(Type):
    value = float
    unit = Field('Unit')


class Unit(Type):
    id = Field(ID)
    name = Field(str)
    unitValues = Field(list_of(UnitValue))


class Nutrition(Type):
    addedSugarG = float
    addedSugarPercentDRV = float
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
    saturatedFatPercentDRV = float
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


class VendorItem(Type):
    name = str
    priority = int
    ingredientListStr = str


class LocationVendorItem(Type):
    vendorItems = Field(list_of(VendorItem))


class Ingredient(Type):
    id = Field(ID)
    name = str
    externalName = str
    categoryValues = Field(CategoryValue)
    dietaryFlags = Field('DietaryFlag')
    locationVendorItems = Field(list_of(LocationVendorItem), args=ArgDict(location_ids=list_of(ID)))


class RecipeInstruction(Type):
    text = str
    position = int


class RecipeItemPreparation(Type):
    id = Field(ID)
    recipeItemId = str
    preparationId = str
    recipeItem = Field('RecipeItem')


class Preparation(Type):
    id = Field(ID)
    name = str
    recipeItemPreparations = Field(list_of(RecipeItemPreparation))


class RecipeTreeComponent(Type):
    id = Field(ID)
    quantity = float
    unit = Field(Unit)
    quantityUnitValues = Field(UnitValue)
    ingredient = Field(Ingredient)
    recipeItem = Field('RecipeItem')
    ancestorComponentIds = Field(list_of(ID))


class AncestorRecipe(Type):
    id = Field(ID)
    name = str
    dietaryFlagsWithUsages = Field('DietaryFlagsWithUsages', args=ArgDict(location_id=ID))


class RecipeUsage(Type):
    ancestorRecipes = Field(list_of(AncestorRecipe))
    quantity = float
    unit = Field(Unit)


class IngredientWithUsages(Type):
    ingredient = Field(Ingredient)
    totalQuantity = float
    unit = Field(Unit)
    totalQuantityUnitValues = Field(UnitValue)
    usages = Field(list_of(RecipeUsage))


class SubRecipe(Type):
    id = Field(ID)
    allIngredients = str
    name = str
    externalName = str
    reconciledNutritionals = Field(Nutrition, args=ArgDict(location_id=ID))
    nutritionalsQuantity = float
    nutritionalsUnit = Field(Unit)
    recipeInstructions = Field(RecipeInstruction)
    recipeTreeComponents = Field(RecipeTreeComponent, args=ArgDict(levels=list_of(Int)))
    dietaryFlagsWithUsages = Field('DietaryFlagsWithUsages', args=ArgDict(location_id=ID))
    categoryValues = Field(CategoryValue)
    ingredientsWithUsages = Field(list_of(IngredientWithUsages), args=ArgDict(location_id=ID))


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
    reconciledNutritionals = Field(Nutrition, args=ArgDict(location_id=ID))


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
    reconciledNutritionals = Field(Nutrition, args=ArgDict(location_id=ID))
    versionConnection = Field(RecipeVersionConnection)
    categoryValues = Field(CategoryValue)
    recipeItems = Field(RecipeItem)
    files = Field(Files)
    isDish = bool
    totalYield = float
    dietaryFlagsWithUsages = Field(DietaryFlagsWithUsages, args=ArgDict(location_id=ID))
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
    reconciledNutritionals = Field(Nutrition, args=ArgDict(location_id=ID))
    versionConnection = Field(RecipeVersionConnection, args=ArgDict({'paginationOptions': PaginationOptions}))
    categoryValues = Field(CategoryValue)
    recipeItems = Field(RecipeItem)
    dietaryFlagsWithUsages = Field(DietaryFlagsWithUsages, args=ArgDict(location_id=ID))
    ingredientsWithUsages = Field(list_of(IngredientWithUsages))
    files = Field(Files)


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
    locationId = ID


class RecipeConnectionFilter(Input):
    id = list_of(str)
    name = str


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


class IngredientNode(Type):
    id = ID
    name = str
    usagesCount = int
    recipeItems = list_of(RecipeItem)


class IngredientEdge(Type):
    node = Field(IngredientNode)


class IngredientConnection(Connection):
    edges = list_of(IngredientEdge)
    pageInfo = Field(PageInfoType)
    totalCount = int


class IngredientConnectionSearch(Input):
    query = str


class IngredientConnectionFilter(Input):
    id = list_of(ID)
    name = str
    search = IngredientConnectionSearch


class PreparationConnectionEdge(Type):
    node = Field(Preparation)


class PreparationConnection(RecipeItemConnectionEdge):
    edges = list_of(PreparationConnectionEdge)
    pageInfo = Field(PageInfoType)
    totalCount = int


class PreparationConnectionPaginationOptions(Input):
    first = int
    startIndex = int


class PreparationConnectionFilter(Input):
    id = list_of(ID)
    name = str


class DeleteRecipeItemPreparationPayload(Type):
    recipeItem = Field(RecipeItem)


class DeleteRecipeItemPreparationInput(Input):
    recipeItemPreparationId = str
