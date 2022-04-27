import logging
from re import M
from typing import Dict, List, Optional
from galley.formatted_queries import FormattedRecipe, get_category_menu_type, get_meal_code, get_external_name
from galley.enums import QuantityUnitEnum, PreparationEnum
from galley.queries import get_raw_menu_data


logger = logging.getLogger(__name__)


class FormattedTopLevelRecipeComponent:
    def __init__(self, rtc):
        self.quantityValues = rtc.get('quantityUnitValues') or []
        self.recipeItem = rtc.get('recipeItem') or {}
        self.subrecipe = self.recipeItem.get('subRecipe') or {}
        self.allergens = self.subrecipe.get('dietaryFlagsWithUsages') or []

    def to_dict(self):
        return {
            'name': get_external_name(self.recipeItem.get('subRecipe', {})),
            'id': self.recipeItem.get('subRecipe', {}).get('id'),
            'quantity': format_quantity_values(self.quantityValues),
            'allergens': format_allergens(self.allergens),
            'isBaseRecipe': self.is_base(),
            # 'recipeComponents':
        }

    def is_base(self):
        preparations = self.recipeItem.get('preparations', [])
        return any(prep.get('id') == PreparationEnum.BASE_RECIPE.value for prep in preparations)

    def format_recipe_components(self, recipe_tree_components):
        pass


def format_allergens(dietary_flags) -> Optional[List[str]]:
    allergens = []
    for dietary_flag in dietary_flags:
        allergen = dietary_flag.get('dietaryFlag', {}).get('name')
        if allergen:
            allergens.append(allergen)
    return allergens or None


def format_quantity_values(quantity_values) -> Optional[List[Dict]]:
    print(quantity_values, 'QV!!')
    quantities = []
    for quantity in quantity_values:
        if quantity.get('unit', {}).get('id') == QuantityUnitEnum.OZ.value or quantity.get('unit', {}).get('id') == QuantityUnitEnum.LB.value:
            quantities.append({
                'value': quantity['value'],
                'unit': quantity['unit']['name']
            })
    return quantities


def get_formatted_ops_menu_data(dates: List[str],
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
                'id': menu_item.get('id'),
                'mealCode': get_meal_code(menu_item['categoryValues']),
                'mealContainer': formatted_recipe.recipe_tags.get('mealContainer', ''),
                'platePhotoUrl': formatted_recipe.platePhotoUrl,
                'recipeId': menu_item.get('recipeId'),
                'recipeName': formatted_recipe.externalName,
                'topLevelComponents': format_ops_menu_rtc_data(formatted_recipe.recipe_tree_components),
                'totalCount': menu_item.get('volume')
            })
        formatted_menus.append(formatted_menu)
    return formatted_menus


def format_ops_menu_rtc_data(recipe_tree_components):
    formatted_components = []
    for rtc in recipe_tree_components:
        if rtc.get('recipeItem', {}).get('subRecipe'):
            formatted_components.append(FormattedTopLevelRecipeComponent(rtc).to_dict())
    return formatted_components
