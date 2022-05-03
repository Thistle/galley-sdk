import logging
from re import M
from typing import Dict, List, Optional
from galley.formatted_queries import FormattedRecipe, get_category_menu_type, get_meal_code, get_external_name
from galley.enums import QuantityUnitEnum, PreparationEnum, DietaryFlagEnum, IngredientCategoryTagTypeEnum, IngredientCategoryValueEnum, RecipeCategoryTagTypeEnum
from galley.queries import get_raw_menu_data


logger = logging.getLogger(__name__)


class FormattedRecipeComponent:
    def __init__(self, rtc):
        self.recipe_item = rtc.get('recipeItem') or {}
        self.subrecipe = self.recipe_item.get('subRecipe') or {}
        self.recipe_tree_components = self.subrecipe.get('recipeTreeComponents') or []
        self.ingredient = rtc.get('ingredient') or {}
        self.type = 'ingredient' if self.ingredient else 'recipe'
        self.quantity_values = rtc.get('quantityUnitValues') or []

    def to_primary_component_dict(self):
        if self.type == 'recipe':
            return {
                'type': self.type,
                'id': self.subrecipe.get('id'),
                'name': get_external_name(self.subrecipe),
                'allergens': format_allergens(self.subrecipe.get('dietaryFlagsWithUsages', [])),
                'quantity': format_quantity_values(self.quantity_values),
                'binWeight': format_bin_weight(self.subrecipe.get('categoryValues', [])),
                'instructions': format_recipe_instructions(self.subrecipe.get('recipeInstructions', [])),
                'recipeComponents': [FormattedRecipeComponent(rtc).to_subcomponent_dict() for rtc in self.recipe_tree_components]
            }
        else:
            return {
                'type': self.type,
                'id': self.ingredient.get('id'),
                'name': self.ingredient.get('name'),
                'allergens': format_allergens(self.ingredient.get('dietaryFlags', []), is_recipe=False),
                'quantity': format_quantity_values(self.quantity_values),
                'binWeight': format_bin_weight(self.ingredient.get('categoryValues', [])),
            }

    def to_subcomponent_dict(self):
        if self.type == 'recipe':
            return {
                'type': self.type,
                'id': self.subrecipe.get('id'),
                'name': get_external_name(self.subrecipe),
                'allergens': format_allergens(self.subrecipe.get('dietaryFlagsWithUsages')),
                'quantity': format_quantity_values(self.quantity_values),
            }
        else:
            return {
                'type': self.type,
                'id': self.ingredient.get('id'),
                'name': self.ingredient.get('name'),
                'allergens': format_allergens(self.ingredient.get('dietaryFlags'), is_recipe=False),
                'quantity': format_quantity_values(self.quantity_values),
            }


def format_recipe_instructions(instructions: List) -> Optional[List[Dict]]:
    return [{'id': i['position'] + 1, 'text': i['text']} for i in instructions] if instructions else []


def format_allergens(dietary_flags: List, is_recipe=True) -> Optional[List[str]]:
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
    for dietary_flag in dietary_flags:
        allergen = dietary_flag.get('dietaryFlag', {}).get('id') if is_recipe else dietary_flag.get('id')
        if allergen and allergen in df_mapping:
            allergens.append(df_mapping[allergen])
    return allergens


def format_bin_weight(category_values: List) -> Dict:
    weight = { 'value': 60, 'unit': 'lb' }
    tags = set([RecipeCategoryTagTypeEnum.BIN_WEIGHT.value, IngredientCategoryTagTypeEnum.BIN_WEIGHT.value])
    for cv in category_values:
        if cv.get('category', {}).get('id') in tags:
            weight['value'] = float(cv['name'])
    return weight


def format_quantity_values(quantity_values: List) -> Optional[List[Dict]]:
    quantities = []
    units = set([QuantityUnitEnum.OZ.value, QuantityUnitEnum.LB.value])
    for quantity in quantity_values:
        if quantity.get('unit', {}).get('id') in units:
            quantities.append({'value': quantity['value'], 'unit': quantity['unit']['name']})
    return quantities


def is_core_recipe(rtc: Dict) -> bool:
    preparations = rtc.get('recipeItem', {}).get('preparations', [])
    return any(prep.get('id') == PreparationEnum.CORE_RECIPE.value for prep in preparations)


def filter_core_recipe_components(rtc: Dict) -> List:
    return rtc.get('recipeItem', {}).get('subRecipe', {}).get('recipeTreeComponents') or []


def is_packaging(category_values: List) -> bool:
    return any(cv.get('id') == IngredientCategoryValueEnum.FOOD_PACKAGE.value for cv in category_values)


def is_ingredient(rtc: Dict) -> bool:
    return not is_packaging(rtc.get('ingredient', {}).get('categoryValues')) if rtc.get('ingredient') else True


def format_ops_menu_rtc_data(rtc: List) -> List:
    components = []
    for rc in rtc:
        if rc.get('ingredient') and not is_ingredient(rc):
            continue
        if rc.get('recipeItem', {}).get('subRecipe') and is_core_recipe(rc):
            components.extend(filter_core_recipe_components(rc))
        else:
            components.append(rc)
    return [FormattedRecipeComponent(c).to_primary_component_dict() for c in components]


def get_formatted_ops_menu_data(
    dates: List[str],
    location_name: str="Vacaville",
    menu_type: str="production",
) -> Optional[List[Dict]]:
    menus = get_raw_menu_data(dates, location_name, menu_type, is_ops=True)
    formatted_menus = []

    if not menus:
        return None

    for menu in menus:
        formatted_menu = {
            'name': menu.get('name'),
            'id': menu.get('id'),
            'date': menu.get('date'),
            'location': menu['location'].get('name'),
            'categoryMenuType': get_category_menu_type(menu['categoryValues']),
            'menuItems': []
        } # type: Dict

        menu_items = menu.get('menuItems', [])
        for menu_item in menu_items:
            formatted_recipe = FormattedRecipe(menu_item.get('recipe', {}))
            formatted_menu['menuItems'].append({
                'mealCode': get_meal_code(menu_item['categoryValues']),
                'recipeId': menu_item.get('recipeId'),
                'recipeName': formatted_recipe.externalName,
                'mealContainer': formatted_recipe.recipe_tags.get('mealContainer', ''),
                'platePhotoUrl': formatted_recipe.plate_photo_url,
                'totalCount': menu_item.get('volume'),
                'primaryRecipeComponents': format_ops_menu_rtc_data(formatted_recipe.recipe_tree_components)
            })
        formatted_menus.append(formatted_menu)
    return formatted_menus
