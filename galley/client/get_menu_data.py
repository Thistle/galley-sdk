# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Any, List, Optional

from .base_model import BaseModel
from .fragments import CategoryFields


class GetMenuData(BaseModel):
    viewer: "GetMenuDataViewer"


class GetMenuDataViewer(BaseModel):
    menuConnection: "GetMenuDataViewerMenuConnection"


class GetMenuDataViewerMenuConnection(BaseModel):
    edges: List["GetMenuDataViewerMenuConnectionEdges"]
    pageInfo: "GetMenuDataViewerMenuConnectionPageInfo"
    totalCount: int


class GetMenuDataViewerMenuConnectionEdges(BaseModel):
    node: "GetMenuDataViewerMenuConnectionEdgesNode"


class GetMenuDataViewerMenuConnectionEdgesNode(BaseModel):
    id: str
    name: str
    date: Optional[Any]
    location: "GetMenuDataViewerMenuConnectionEdgesNodeLocation"
    categoryValues: List["GetMenuDataViewerMenuConnectionEdgesNodeCategoryValues"]
    menuItems: List["GetMenuDataViewerMenuConnectionEdgesNodeMenuItems"]


class GetMenuDataViewerMenuConnectionEdgesNodeLocation(BaseModel):
    name: str


class GetMenuDataViewerMenuConnectionEdgesNodeCategoryValues(CategoryFields):
    pass


class GetMenuDataViewerMenuConnectionEdgesNodeMenuItems(BaseModel):
    id: str
    recipeId: str
    categoryValues: List[
        "GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsCategoryValues"
    ]
    recipe: "GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipe"


class GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsCategoryValues(CategoryFields):
    pass


class GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipe(BaseModel):
    name: str
    externalName: Optional[str]
    categoryValues: List[
        "GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeCategoryValues"
    ]
    media: List["GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeMedia"]
    isDish: Optional[bool]
    dietaryFlagsWithUsages: List[
        "GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeDietaryFlagsWithUsages"
    ]


class GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeCategoryValues(
    CategoryFields
):
    pass


class GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeMedia(BaseModel):
    altText: Optional[str]
    caption: Optional[str]
    sourceUrl: Optional[str]


class GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeDietaryFlagsWithUsages(
    BaseModel
):
    dietaryFlag: "GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeDietaryFlagsWithUsagesDietaryFlag"


class GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeDietaryFlagsWithUsagesDietaryFlag(
    BaseModel
):
    id: str
    name: str


class GetMenuDataViewerMenuConnectionPageInfo(BaseModel):
    startIndex: Optional[int]
    endIndex: Optional[int]
    hasPreviousPage: Optional[bool]
    hasNextPage: Optional[bool]


GetMenuData.model_rebuild()
GetMenuDataViewer.model_rebuild()
GetMenuDataViewerMenuConnection.model_rebuild()
GetMenuDataViewerMenuConnectionEdges.model_rebuild()
GetMenuDataViewerMenuConnectionEdgesNode.model_rebuild()
GetMenuDataViewerMenuConnectionEdgesNodeMenuItems.model_rebuild()
GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipe.model_rebuild()
GetMenuDataViewerMenuConnectionEdgesNodeMenuItemsRecipeDietaryFlagsWithUsages.model_rebuild()
