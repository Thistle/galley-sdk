import logging
from re import M
from typing import Dict, List, Optional, Union

from galley.queries import get_raw_menu_data
from galley.formatted_queries import (
    FormattedRecipe,
    get_category_menu_type,
    get_meal_code,
    get_external_name
)
from galley.enums import (
    QuantityUnitEnum,
    PreparationEnum,
    DietaryFlagEnum,
    IngredientCategoryTagTypeEnum as IngredientCTagEnum,
    IngredientCategoryValueEnum as IngredientCValEnum,
    RecipeCategoryTagTypeEnum as RecipeCTagEnum,
)


logger = logging.getLogger(__name__)


DEFAULT_BIN_WEIGHT_VALUE = 60
DEFAULT_BIN_WEIGHT_UNIT = 'lb'


class FormattedRecipeComponent:
    def __init__(self, rtc):
        self.quantity_values = rtc.get('quantityUnitValues') or []
        self.ingredient = rtc.get('ingredient') or {}
        self.subrecipe = rtc.get('recipeItem').get('subRecipe') or {}
        self.rtc = self.subrecipe.get('recipeTreeComponents') or []

        if self.ingredient:
            self.type = 'ingredient'
            self.data = self.ingredient
            self.dietary_flags = self.data.get('dietaryFlags')
        else:
            self.type = 'recipe'
            self.data = self.subrecipe
            self.dietary_flags = self.data.get('dietaryFlagsWithUsages')

    def to_primary_component_dict(self):
        pcd = {
            'type': self.type,
            'id': self.data.get('id'),
            'name': get_external_name(self.data),
            'allergens': format_allergens(self.dietary_flags, is_recipe=(self.type=='recipe')),
            'quantity': format_quantity_values(self.quantity_values),
            'binWeight': format_bin_weight(self.data.get('categoryValues')),
        }
        if self.type == 'recipe':
            return {
                **pcd,
                'instructions': format_recipe_instructions(self.subrecipe.get('recipeInstructions')),
                'recipeComponents': [FormattedRecipeComponent(rtc).to_subcomponent_dict() for rtc in self.rtc]
            }
        return pcd

    def to_subcomponent_dict(self):
        return {
            'type': self.type,
            'id': self.data.get('id'),
            'name': format_name(self.data, is_recipe=(self.type=='recipe')),
            'allergens': format_allergens(self.dietary_flags, is_recipe=(self.type=='recipe')),
            'quantity': format_quantity_values(self.quantity_values)
        }


def format_name(data: Dict, is_recipe=True) -> Optional[str]:
    """
    Returns recipe 'externalName' if it exists, otherwise returns 'name'.
    Default returns 'name' for non-recipe (ingredient) types if 'name'
    exists. If 'name' doesn't exist, returns None.
    """
    if data.get('externalName') and is_recipe:
        return data['externalName']
    return data.get('name') or None


def format_recipe_instructions(instructions: List) -> List[Optional[Dict[str, Union[int, str]]]]:
    """
    Takes in a list of instructions and returns a formatted dict list
    of instruction text and its ordinal position at 1-based index.
    If empty list or None passed in, returns [].

    Example: [in] [{'text': 'instruction text', 'position': 0}, ...]
             [out] [{'id': 1, 'text': 'instruction text'}, ...]
    """
    return [
        {'id': 1 + i['position'], 'text': i['text']}
        for i in instructions
    ] if instructions else []


def format_allergens(dietary_flags: List, is_recipe=True) -> Optional[List[str]]:
    """
    Takes in a list of dietary flags (dfs) and returns a list of flagged
    allergens. Defaults to parse 'dietaryFlagsWithUsages' for a recipe,
    and parses 'dietaryFlags' for an ingredient when is_recipe=False.
    If dfs is an empty list or None, or no allergens exist, returns [].
    """
    df_mapping = {
        DietaryFlagEnum.TREE_NUTS.value: 'tree_nuts',
        DietaryFlagEnum.SOY_BEANS.value: "soy",
        DietaryFlagEnum.SHELLFISH.value: "shellfish",
        DietaryFlagEnum.PORK.value: "pork",
        DietaryFlagEnum.FISH.value: "fish",
        DietaryFlagEnum.COCONUT.value: "coconut",
        DietaryFlagEnum.PEANUTS.value: "peanuts",
        DietaryFlagEnum.LAMB.value: "lamb",
        DietaryFlagEnum.SMOKED_MEATS.value: "smoked_meats",
        DietaryFlagEnum.BEEF.value: "beef",
        DietaryFlagEnum.SESAME_SEEDS.value: "sesame_seeds",
    }
    allergens = []
    if dietary_flags:
        for df in dietary_flags:
            allergen = df.get('dietaryFlag', {}).get('id') if is_recipe else df.get('id')
            if allergen and allergen in df_mapping:
                allergens.append(df_mapping[allergen])
    return allergens


def format_bin_weight(category_values: List) -> Dict:
    """
    Takes in a list of recipe or ingredient category values and returns a
    dict containing either a bin weight value (in lb) pulled from Galley,
    or DEFAULT_BIN_WEIGHT_VALUE if none exists. Bin weight unit always
    returns 'lb'.
    """
    tags = set([RecipeCTagEnum.BIN_WEIGHT_TAG.value, IngredientCTagEnum.BIN_WEIGHT_TAG.value])
    weight = {
        'value': DEFAULT_BIN_WEIGHT_VALUE,
        'unit': DEFAULT_BIN_WEIGHT_UNIT
    }
    if category_values:
        for cv in category_values:
            if cv.get('category', {}).get('id') in tags:
                value = float(cv['name'])
                return weight | {'value': value} # type: ignore
    return weight


def format_quantity_values(quantity_values: List) -> Optional[List[Dict]]:
    """
    Filters a list of quantity values to return only unit values in
    ounces (oz) and pounds (lb).
    """
    units = set([QuantityUnitEnum.OZ.value, QuantityUnitEnum.LB.value])
    return [
        {'value': qv['value'], 'unit': qv['unit']['name']}
        for qv in quantity_values
        if qv.get('unit', {}).get('id') in units
    ]


def is_core_recipe(component: Dict) -> bool:
    """
    Returns True if a recipe component contains a "Core Recipe"
    preparation.
    """
    preparations = component.get('recipeItem', {}).get('preparations') or []
    return any(prep.get('id') == PreparationEnum.CORE_RECIPE.value for prep in preparations)


def is_packaging(component: Dict) -> bool:
    """
    Checks and returns True if an ingredient-typed component is a food
    package item.
    """
    cvs = component.get('ingredient', {}).get('categoryValues') or []
    return any(cv.get('id') == IngredientCValEnum.FOOD_PACKAGE.value for cv in cvs)


def format_ops_menu_rtc_data(recipe_tree_components: List) -> List[Optional[Dict]]:
    components: List = []
    for rtc in recipe_tree_components:
        ingredient = rtc.get('ingredient') or {}
        subrecipe = rtc.get('recipeItem', {}).get('subRecipe') or {}

        if ingredient and is_packaging(rtc):
            continue

        if subrecipe and is_core_recipe(rtc):
            components.extend(subrecipe.get('recipeTreeComponents') or [])
        else:
            components.append(rtc)
    return [FormattedRecipeComponent(c).to_primary_component_dict() for c in components]


def get_formatted_ops_menu_data(
    dates: List[str],
    location_name: str="Vacaville",
    menu_type: str="production",
) -> Optional[List[Dict]]:
    menus = get_raw_menu_data(dates, location_name, menu_type, is_ops=True)

    if not menus:
        return None

    formatted_menus = []
    for menu in menus:
        formatted_menu: Dict = {
            'name': menu.get('name'),
            'id': menu.get('id'),
            'date': menu.get('date'),
            'location': menu['location'].get('name'),
            'categoryMenuType': get_category_menu_type(menu.get('categoryValues')),
            'menuItems': []
        }

        menu_items = menu.get('menuItems') or []
        for menu_item in menu_items:
            formatted_recipe = FormattedRecipe(menu_item.get('recipe') or {})
            formatted_menu['menuItems'].append({
                'menuItemId': menu_item.get('id'),
                'mealCode': get_meal_code(menu_item.get('categoryValues')),
                'recipeId': menu_item.get('recipeId'),
                'recipeName': formatted_recipe.externalName,
                'mealContainer': formatted_recipe.recipe_tags.get('mealContainer', ''),
                'platePhotoUrl': formatted_recipe.plate_photo_url,
                'totalCount': menu_item.get('volume'),
                'primaryRecipeComponents': format_ops_menu_rtc_data(formatted_recipe.recipe_tree_components)
            })
        formatted_menus.append(formatted_menu)
    return formatted_menus
