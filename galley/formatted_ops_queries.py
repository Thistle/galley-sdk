import logging
from re import M
from typing import Dict, List, Optional
from galley.formatted_queries import FormattedRecipe, get_category_menu_type, get_meal_code, get_external_name
from galley.enums import QuantityUnitEnum, PreparationEnum, DietaryFlagEnum, IngredientCategoryTagTypeEnum, IngredientCategoryValueEnum
from galley.queries import get_raw_menu_data


logger = logging.getLogger(__name__)


class FormattedPrimaryRecipeComponent:
    def __init__(self, rtc):
        self.recipe_item = rtc.get('recipeItem') or {}
        self.subrecipe = self.recipe_item.get('subRecipe') or {}
        self.ingredient = rtc.get('ingredient') or {}
        self.quantity_values = rtc.get('quantityUnitValues') or []
        self.allergens = self.subrecipe.get('dietaryFlagsWithUsages') or []
        self.is_base_recipe = self.is_base()
        self.type = 'ingredient' if self.ingredient else 'recipe'

    def to_dict(self):
        if self.type == 'recipe':
            return {
                'id': self.recipe_item.get('subRecipe', {}).get('id'),
                'name': get_external_name(self.recipe_item.get('subRecipe', {})),
                'isBase': self.is_base_recipe,
                'allergens': format_allergens(self.allergens),
                'quantity': format_quantity_values(self.quantity_values),
                'batchYield': format_quantity_values(self.subrecipe.get('batchYield', [])),
                'recipeComponents': self.format_recipe_components(self.subrecipe.get('recipeTreeComponents', [])),
            }
        else:
            return {
                'id': self.ingredient.get('id'),
                'name': self.ingredient.get('name'),
                'isBase': False,
                'allergens': format_allergens(self.allergens, is_recipe=False),
                'quantity': format_quantity_values(self.quantity_values),
            }

    def is_base(self):
        preparations = self.recipe_item.get('preparations', [])
        return any(prep.get('id') == PreparationEnum.BASE_RECIPE.value for prep in preparations)

    def format_recipe_components(self, recipe_components):
        components = []
        for rc in recipe_components:
            _type = 'ingredient' if rc.get('ingredient') else 'recipe'
            component = self.format_ingredient(rc) if _type == 'ingredient' else self.format_recipe(rc)
            components.append(component)
        return components

    def format_ingredient(self, data):
        ingredient = data.get('ingredient')
        return {
            'type': 'ingredient',
            'id': ingredient.get('id'),
            'name': ingredient.get('name'),
            'allergens': format_allergens(ingredient.get('dietaryFlags'), is_recipe=False),
            'quantity': format_quantity_values(data.get('quantityUnitValues'))
        }

    def format_recipe(self, data):
        recipe = data.get('recipeItem', {}).get('subRecipe', {})
        component = {
            'type': 'recipe',
            'id': recipe.get('id'),
            'name': get_external_name(recipe),
            'allergens': format_allergens(recipe.get('dietaryFlagsWithUsages')),
            'quantity': format_quantity_values(data.get('quantityUnitValues')),
        }
        if self.is_base_recipe:
            batch_yield = format_quantity_values(recipe.get('batchYield', []))
            subcomponents = self.format_recipe_components(recipe.get('recipeTreeComponents', []))
            if batch_yield: component['batchYield'] = batch_yield
            if subcomponents: component['recipeComponents'] = subcomponents
        return component


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


def is_packaging(category_values):
    return any(cat_val.get('id') == IngredientCategoryValueEnum.FOOD_PACKAGE.value for cat_val in category_values)


def filter_rtc(rtc):
    return not is_packaging(rtc.get('ingredient', {}).get('categoryValues', [])) if rtc.get('ingredient') else True


def format_ops_menu_rtc_data(rtc: List) -> List:
    rtc = list(filter(filter_rtc, rtc))
    return [FormattedPrimaryRecipeComponent(c).to_dict() for c in rtc]


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
                'platePhotoUrl': formatted_recipe.platePhotoUrl,
                'totalCount': menu_item.get('volume'),
                'primaryRecipeComponents': format_ops_menu_rtc_data(formatted_recipe.recipe_tree_components)
            })
        formatted_menus.append(formatted_menu)
    return formatted_menus
