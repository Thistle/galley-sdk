import re
import logging
from functools import reduce
from typing import Any, Dict, List, Optional, Tuple, Set, Union
from galley.queries import get_raw_menu_data
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE
from galley.formatted_queries import get_menu_type, get_item_code, get_external_name, get_recipe_category_tags
from galley.enums import (
    UnitEnum,
    ContainerEnum,
    DietaryFlagEnum,
    EntityMediaEnum,
    PreparationEnum as PrepEnum,
    IngredientCategoryTagTypeEnum as IngredientCTagEnum,
    IngredientCategoryValueEnum as IngredientCVEnum,
    RecipeCategoryTagTypeEnum as RecipeCTagEnum
)


logger = logging.getLogger(__name__)


INGREDIENT = 'ingredient'
SUBRECIPE = 'recipe'

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
        self.all_ingredients = self.data.pop('allIngredientsWithUsages', []) or []
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

    def format_ingredients(self) -> List[Dict]:
        return [
            ingredient.get('name') for item in self.all_ingredients if (ingredient := item.get('ingredient', {}))
        ]

    def to_primary_component_dict(self) -> dict[str, Any]:
        component: Dict = {
            'allergens': self.format_allergens(),
            'binWeight': self.format_bin_weight(),
            'cuppingContainer': self.get_cupping_container(),
            'id': self.data.get('id'),
            # Contains the ingredients list for pre-fab ingredients
            'label': self.data.get('externalName'),
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
                        component.get('recipeItem').get('unit'),
                    ).to_subcomponent_dict()
                    for component in self.components
                    if component.get('recipeItem')
                ],
                'ingredients': self.format_ingredients(),
            }
        return component

    def to_subcomponent_dict(self):
        subcomponent = {
            'allergens': self.format_allergens(),
            'id': self.data.get('id'),
            # Contains the ingredients list for pre-fab ingredients
            'label': self.data.get('externalName'),
            'name': self.format_name(),
            'type': self.type,
            'usage': self.format_usage(),
        }
        if self.type == SUBRECIPE:
            subcomponent['ingredients'] = self.format_ingredients()
        return subcomponent


def get_photo_url(photos: List, caption: str) -> Optional[str]:
    caption_regex = rf'(?i){caption}'
    return next((
        url for photo in photos
        if (
            bool(re.search(caption_regex, photo.get('caption') or ''))
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
    product_codes_filter: Union[Set[str], List[str]],
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
            product_code = get_item_code(menu_item)
            if product_code.lower() in product_codes_filter:
                recipe = menu_item.get('recipe') or {}
                formatted_menu['menuItems'].append({
                    'menuItemId': menu_item.get('id'),
                    'mealCode': product_code,
                    'recipeId': menu_item.get('recipeId'),
                    'recipeName': get_external_name(recipe),
                    'mealContainer': get_recipe_category_tags(recipe.get('categoryValues') or []).get('mealContainer'),
                    'platePhotoUrl': get_photo_url(photos=recipe.get('files', {}).get('photos') or [], caption=EntityMediaEnum.PLATE_CAPTION.value),
                    'platePlanogramUrl': get_photo_url(photos=recipe.get('files', {}).get('photos') or [], caption=EntityMediaEnum.PLANOGRAM_CAPTION.value),
                    'totalCount': menu_item.get('volume'),
                    'totalCountUnit': menu_item.get('unit', {}).get('name'),
                    'primaryRecipeComponents': format_components(recipe.get('recipeTreeComponents') or [])
                })
        formatted_menus.append(formatted_menu)
    return formatted_menus
