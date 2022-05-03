import logging
from re import M
from typing import Dict, List, Optional
from galley.formatted_queries import FormattedRecipe, get_category_menu_type, get_meal_code, get_external_name
from galley.enums import QuantityUnitEnum, PreparationEnum, DietaryFlagEnum, IngredientCategoryTagTypeEnum, IngredientCategoryValueEnum
from galley.queries import get_raw_menu_data
from pprint import pprint


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
                'allergens': format_allergens(self.subrecipe.get('dietaryFlagsWithUsages')),
                'quantity': format_quantity_values(self.quantity_values),
                'binWeight': { 'value': 60, 'unit': 'lb' }, # TODO: will dynamically pull from Galley when "Bin Weight" recipe tags are implmemented
                'instructions': format_recipe_instructions(self.subrecipe.get('recipeInstructions')),
                'recipeComponents': [FormattedRecipeComponent(rtc).to_subcomponent_dict() for rtc in self.recipe_tree_components]
            }
        else:
            return {
                'type': self.type,
                'id': self.ingredient.get('id'),
                'name': self.ingredient.get('name'),
                'allergens': format_allergens(self.ingredient.get('dietaryFlags'), is_recipe=False),
                'quantity': format_quantity_values(self.quantity_values),
                'binWeight': { 'value': 60, 'unit': 'lb' }, # TODO: will dynamically pull from Galley when "Bin Weight" ingredient tags are implmemented
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


def format_recipe_instructions(instructions: List) -> Optional[Dict]:
    return [{instruction['position'] + 1: instruction['text']} for instruction in instructions]


def format_allergens(dietary_flags, is_recipe=True) -> Optional[List[str]]:
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
    return allergens or None


def format_quantity_values(quantity_values: List) -> Optional[List[Dict]]:
    quantities = []
    for quantity in quantity_values:
        if quantity.get('unit', {}).get('id') == QuantityUnitEnum.OZ.value or quantity.get('unit', {}).get('id') == QuantityUnitEnum.LB.value:
            quantities.append({
                'value': quantity['value'],
                'unit': quantity['unit']['name']
            })
    return quantities


def is_base(rtc: Dict) -> bool:
    recipe_item = rtc.get('recipeItem') or {}
    preparations = recipe_item.get('preparations', [])
    return any(prep.get('id') == PreparationEnum.BASE_RECIPE.value for prep in preparations)


def filter_base_components(rtc: Dict) -> List:
    base = rtc.get('recipeItem').get('subRecipe') or {}
    return base.get('recipeTreeComponents') or []


def is_packaging(category_values: List) -> bool:
    return any(cat_val.get('id') == IngredientCategoryValueEnum.FOOD_PACKAGE.value for cat_val in category_values)


def filter_ingredients(rtc: Dict) -> bool:
    return not is_packaging(rtc.get('ingredient', {}).get('categoryValues', [])) if rtc.get('ingredient') else True


def format_ops_menu_rtc_data(rtc: List) -> List:
    components = []
    for c in rtc:
        if filter_ingredients(c):
            if is_base(c):
                components.extend(filter_base_components(c))
            else:
                components.append(c)
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
