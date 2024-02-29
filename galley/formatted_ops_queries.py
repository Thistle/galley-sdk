import re
import logging
from functools import reduce
from typing import Dict, List, Optional, Tuple
from galley.queries import get_raw_menu_data
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.formatted_queries import get_menu_type, get_item_code, get_external_name, get_recipe_category_tags
from galley.enums import (
    UnitEnum,
    ContainerEnum,
    DietaryFlagEnum,
    RecipeMediaEnum,
    PreparationEnum as PrepEnum,
    IngredientCategoryTagTypeEnum as IngredientCTagEnum,
    IngredientCategoryValueEnum as IngredientCVEnum,
    RecipeCategoryTagTypeEnum as RecipeCTagEnum
)


logger = logging.getLogger(__name__)


INGREDIENT = 'ingredient'
SUBRECIPE = 'recipe'

BASE_CODES = ['s', 'b', 'lv', 'lm', 'dv', 'dm']
BASE_MEALS = {f'{b}{n+1}' for b in BASE_CODES for n in range(6)}
JAR_SALADS = {'ssa', 'ssb', 'ssc', 'ssd'}
SIDE_SOUPS = {'scw', 'sp',  'sm',  'sch'}
MEAL_CODES_WHITELIST = BASE_MEALS | JAR_SALADS | SIDE_SOUPS

DEFAULT_BIN_WEIGHT_VALUE = 60
DEFAULT_BIN_WEIGHT_UNIT = 'lb'

ALLERGEN_LABELS = {
    DietaryFlagEnum.SESAME_SEEDS.name: 'sesame_seeds',
    DietaryFlagEnum.SMOKED_MEATS.name: 'smoked_meats',
    DietaryFlagEnum.SHELLFISH.name: 'shellfish',
    DietaryFlagEnum.TREE_NUTS.name: 'tree_nuts',
    DietaryFlagEnum.SOYBEANS.name: 'soy',
    DietaryFlagEnum.COCONUT.name: 'coconut',
    DietaryFlagEnum.PEANUTS.name: 'peanuts',
    DietaryFlagEnum.BEEF.name: 'beef',
    DietaryFlagEnum.FISH.name: 'fish',
    DietaryFlagEnum.LAMB.name: 'lamb',
    DietaryFlagEnum.PORK.name: 'pork',
}

class RecipeItem:
    def __init__(
        self,
        recipeitem: Dict,
        components: Optional[List] = None,
        quantity: Optional[float] = None,
        unit: Optional[Dict] = None,
    ) -> None:
        subrecipe, ingredient = recipeitem['subRecipe'], recipeitem['ingredient']

        self.data = subrecipe or ingredient or {}
        self.type = SUBRECIPE if subrecipe else INGREDIENT
        self.usage: Dict = dict(value=quantity or 0, unit=unit or {})
        self.preparations = recipeitem.pop('preparations', []) or []
        self.instructions = self.data.pop('recipeInstructions', []) or []
        self.unit_values = self.usage['unit'].pop('unitValues', []) or []
        self.category_values = self.data.pop('categoryValues', []) or []
        self.dietary_flags = self.data.pop('dietaryFlagsWithUsages', self.data.pop('dietaryFlags', [])) or []
        self.components = components or []

    def format_instructions(self) -> List[Dict]:
        return [{
            'id': instruction['position'] + 1,
            'text': instruction['text']
        } for instruction in self.instructions]

    def get_cupping_container(self) -> Optional[bool]:
        """
        Returns the cupping container preparation for a
        recipe component, otherwise returns None.
        """
        return next((
            prep['name'] for prep in self.preparations
            if prep['id'] in ContainerEnum.CUPPING.values
        ), None)

    def is_core_recipe(self) -> bool:
        """
        Returns True if a recipe component has a "Core
        Recipe" preparation.
        """
        return any(
            prep['id'] == PrepEnum.CORE_RECIPE.value
            for prep in self.preparations
        )

    def is_packaging(self) -> bool:
        """
        Returns True if item is a packaging ingredient.
        """
        return any(
            cv['id'] == IngredientCVEnum.FOOD_PACKAGE.value
            for cv in self.category_values
        )

    def format_bin_weight(self) -> Dict:
        """
        Returns a dict containing either a custom bin
        weight value pulled from Galley, or a default
        value if none exist. Unit always returns 'lb'.
        """
        tags = set([
            RecipeCTagEnum.BIN_WEIGHT_TAG.value,
            IngredientCTagEnum.BIN_WEIGHT_TAG.value
        ])
        value = next((
            cv['name'] for cv in self.category_values
            if cv['category']['id'] in tags
        ), DEFAULT_BIN_WEIGHT_VALUE)
        return {
            'value': float(value),
            'unit': DEFAULT_BIN_WEIGHT_UNIT
        }

    def format_name(self) -> Optional[str]:
        """
        Returns a recipe externalName if one exists, or
        returns name. Returns an ingredient name if one
        exists, or returns None.
        """
        if (
            self.data.get('externalName')
            and self.type == SUBRECIPE
        ):
            return self.data['externalName']
        return self.data.get('name') or None

    def format_allergens(self) -> List[str]:
        """
        Returns a flagged allergens list. Recipes use
        dietaryFlagsWithUsages, while ingredients use
        dietaryFlags. Returns [] if self.dietary_flags is
        empty or None.
        """
        allergens = set(
            allergen for df in self.dietary_flags
            if (allergen := ALLERGEN_LABELS.get(
                df.get('dietaryFlag', {}).get('name')
                or df.get('name')
            ))
        )
        return sorted(allergens)

    def format_quantity_values(self) -> List[Dict]:
        """
        Returns a list containing converted usage unit
        values in ounces (oz) and pounds (lb).
        """
        usage, unit = self.usage.values()
        units = set([UnitEnum.OZ.value, UnitEnum.LB.value])

        base = next((
            uv['value'] for uv in self.unit_values
            if uv['unit']['id'] == unit.get('id')
        ), None) or 0
        return [{
            'value': usage / base * uv['value'],
            'unit': uv['unit']['name']
        } for uv in self.unit_values if uv['unit']['id'] in units]

    def format_usage(self) -> Dict:
        value, unit = self.usage.values()
        return {
            'value': value,
            'unit': unit.get('name')
        }

    def to_primary_component_dict(self):
        component: Dict = {
            'allergens': self.format_allergens(),
            'binWeight': self.format_bin_weight(),
            'cuppingContainer': self.get_cupping_container(),
            'id': self.data.get('id'),
            'name': self.data.get('name'),
            'quantityValues': self.format_quantity_values(),
            'type': self.type,
            'usage': self.format_usage()
        }

        if self.type == SUBRECIPE:
            return {
                **component,
                'instructions': self.format_instructions(),
                'recipeComponents': [
                    RecipeItem(
                        component.get('recipeItem'),
                        component.get('components'),
                        component.get('recipeItem').get('quantity'),
                        component.get('recipeItem').get('unit')
                    ).to_subcomponent_dict()
                    for component in self.components
                    if component.get('recipeItem')
                ]
            }
        return component

    def to_subcomponent_dict(self):
        return {
            'allergens': self.format_allergens(),
            'id': self.data.get('id'),
            'name': self.format_name(),
            'type': self.type,
            'usage': self.format_usage()
        }


def get_plate_photo_url(photos: List) -> Optional[str]:
    caption = rf'(?i){RecipeMediaEnum.PLATE_CAPTION.value}'
    return next((
        url for photo in photos
        if (
            bool(re.search(caption, photo.get('caption') or ''))
            and (url := photo.get('sourceUrl'))
        )
    ), None)


def build_recipe_tree(acc: Tuple[Dict, Dict], rtc: Dict) -> Tuple[Dict, Dict]:
    ancestors = rtc['ancestorComponentIds']
    tree, components = acc
    components[rtc['id']] = rtc

    if len(ancestors) == 0:
        tree['recipe'] = rtc
    else:
        parent = components[ancestors[-1]]
        parent.setdefault('components', []).append(rtc)
    return acc


def format_components(rtc: List) -> List[Dict]:
    tree, _ = reduce(build_recipe_tree, rtc, ({}, {}))  # type: Tuple[Dict, Dict]
    primary_components = []

    for component in tree['recipe']['components']:
        if not component['recipeItem']:
            continue

        recipeitem = RecipeItem(
            component.get('recipeItem'),
            component.get('components'),
            component.get('quantity'),
            component.get('unit')
        )
        if (
            recipeitem.type == INGREDIENT
            and recipeitem.is_packaging()
        ):
            continue
        if (
            recipeitem.type == SUBRECIPE
            and recipeitem.is_core_recipe()
        ):
            primary_components += [
                RecipeItem(
                    c.get('recipeItem'),
                    c.get('components'),
                    c.get('quantity'),
                    c.get('unit')
                ) for c in component['components']
            ]
        else:
            primary_components += [recipeitem]
    return [
        pc.to_primary_component_dict()
        for pc in primary_components
    ]


def get_formatted_ops_menu_data(
    dates: List[str],
    location_name: str = DEFAULT_LOCATION,
    menu_type: str = DEFAULT_MENU_TYPE,
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
            'categoryMenuType': get_menu_type(menu),
            'menuItems': []
        }

        menu_items = menu.get('menuItems') or []
        for menu_item in menu_items:
            meal_code = get_item_code(menu_item)
            if meal_code.lower() in MEAL_CODES_WHITELIST:
                recipe = menu_item.get('recipe') or {}
                formatted_menu['menuItems'].append({
                    'menuItemId': menu_item.get('id'),
                    'mealCode': meal_code,
                    'recipeId': menu_item.get('recipeId'),
                    'recipeName': get_external_name(recipe),
                    'mealContainer': get_recipe_category_tags(recipe.get('categoryValues') or []).get('mealContainer'),
                    'platePhotoUrl': get_plate_photo_url(recipe.get('files', {}).get('photos') or []),
                    'totalCount': menu_item.get('volume'),
                    'totalCountUnit': menu_item.get('unit', {}).get('name'),
                    'primaryRecipeComponents': format_components(recipe.get('recipeTreeComponents') or [])
                })
        formatted_menus.append(formatted_menu)
    return formatted_menus
