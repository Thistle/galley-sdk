# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Any, List, Optional

from .base_model import BaseModel
from .fragments import CategoryFields, UnitFields


class GetOpsMenuData(BaseModel):
    viewer: "GetOpsMenuDataViewer"


class GetOpsMenuDataViewer(BaseModel):
    menuConnection: "GetOpsMenuDataViewerMenuConnection"


class GetOpsMenuDataViewerMenuConnection(BaseModel):
    edges: List["GetOpsMenuDataViewerMenuConnectionEdges"]
    pageInfo: "GetOpsMenuDataViewerMenuConnectionPageInfo"
    totalCount: int


class GetOpsMenuDataViewerMenuConnectionEdges(BaseModel):
    node: "GetOpsMenuDataViewerMenuConnectionEdgesNode"


class GetOpsMenuDataViewerMenuConnectionEdgesNode(BaseModel):
    id: str
    name: str
    date: Optional[Any]
    location: "GetOpsMenuDataViewerMenuConnectionEdgesNodeLocation"
    categoryValues: List["GetOpsMenuDataViewerMenuConnectionEdgesNodeCategoryValues"]
    menuItems: List["GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItems"]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeLocation(BaseModel):
    name: str


class GetOpsMenuDataViewerMenuConnectionEdgesNodeCategoryValues(CategoryFields):
    pass


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItems(BaseModel):
    id: str
    recipeId: str
    categoryValues: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsCategoryValues"
    ]
    volume: Optional[float]
    unit: Optional["GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsUnit"]
    recipe: "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipe"


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsCategoryValues(
    CategoryFields
):
    pass


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsUnit(BaseModel):
    id: str
    name: str


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipe(BaseModel):
    name: str
    id: str
    categoryValues: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeCategoryValues"
    ]
    media: List["GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeMedia"]
    recipeTreeComponents: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponents"
    ]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeCategoryValues(
    CategoryFields
):
    pass


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeMedia(BaseModel):
    altText: Optional[str]
    caption: Optional[str]
    sourceUrl: Optional[str]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponents(
    BaseModel
):
    id: str
    ancestorComponentIds: List[str]
    quantity: Optional[float]
    unit: Optional[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsUnit"
    ]
    recipeItem: Optional[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItem"
    ]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsUnit(
    UnitFields
):
    pass


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItem(
    BaseModel
):
    preparations: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemPreparations"
    ]
    quantity: Optional[float]
    unit: Optional[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemUnit"
    ]
    ingredient: Optional[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredient"
    ]
    subRecipe: Optional[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipe"
    ]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemPreparations(
    BaseModel
):
    id: str
    name: str


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemUnit(
    BaseModel
):
    id: str
    name: str


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredient(
    BaseModel
):
    locationVendorItems: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientLocationVendorItems"
    ]
    id: str
    name: str
    externalName: str
    categoryValues: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientCategoryValues"
    ]
    dietaryFlags: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientDietaryFlags"
    ]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientLocationVendorItems(
    BaseModel
):
    vendorItems: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientLocationVendorItemsVendorItems"
    ]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientLocationVendorItemsVendorItems(
    BaseModel
):
    name: str
    priority: Optional[int]
    ingredientListStr: Optional[str]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientCategoryValues(
    CategoryFields
):
    pass


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemIngredientDietaryFlags(
    BaseModel
):
    id: str
    name: str


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipe(
    BaseModel
):
    id: str
    name: str
    externalName: Optional[str]
    categoryValues: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeCategoryValues"
    ]
    recipeInstructions: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeRecipeInstructions"
    ]
    dietaryFlagsWithUsages: List[
        "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeDietaryFlagsWithUsages"
    ]


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeCategoryValues(
    CategoryFields
):
    pass


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeRecipeInstructions(
    BaseModel
):
    text: str
    position: int


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeDietaryFlagsWithUsages(
    BaseModel
):
    dietaryFlag: "GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeDietaryFlagsWithUsagesDietaryFlag"


class GetOpsMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeRecipeTreeComponentsRecipeItemSubRecipeDietaryFlagsWithUsagesDietaryFlag(
    BaseModel
):
    id: str
    name: str


class GetOpsMenuDataViewerMenuConnectionPageInfo(BaseModel):
    startIndex: Optional[int]
    endIndex: Optional[int]
    hasPreviousPage: Optional[bool]
    hasNextPage: Optional[bool]
