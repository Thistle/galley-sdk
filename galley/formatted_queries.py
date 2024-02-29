import re
import logging
from copy import deepcopy
from typing import Dict, List, Optional
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE, GALLEY_ERROR_PREFIX
from galley.queries import get_raw_menu_data, get_raw_recipes_data
from galley.enums import (
    UnitEnum,
    EntityMediaEnum,
    DietaryFlagEnum,
    PreparationEnum,
    MenuCategoryEnum,
    MenuItemCategoryEnum,
    RecipeCategoryTagTypeEnum,
    IngredientCategoryValueEnum,
    IngredientCategoryTagTypeEnum,
)


logger = logging.getLogger(__name__)


ALLERGEN_LABELS = {
    DietaryFlagEnum.SMOKED_MEATS.name: 'smoked meats',
    DietaryFlagEnum.SHELLFISH.name: 'shellfish',
    DietaryFlagEnum.TREE_NUTS.name: 'tree nuts',
    DietaryFlagEnum.SOYBEANS.name: 'soy',
    DietaryFlagEnum.COCONUT.name: 'coconut',
    DietaryFlagEnum.PEANUTS.name: 'peanuts',
    DietaryFlagEnum.FISH.name: 'fish',
    DietaryFlagEnum.BEEF.name: 'beef',
    DietaryFlagEnum.LAMB.name: 'lamb',
    DietaryFlagEnum.PORK.name: 'pork',
}


def get_ingredient_name(ingredient: Dict) -> Optional[str]:
    name = ingredient.get("externalName") or ingredient.get("name")
    byname = (get_ingredient_primary_vendor_item(ingredient) or {}).get("ingredientListStr")
    return f"{name} ({byname})" if name and byname else name


def get_ingredient_primary_vendor_item(
    ingredient: Dict
) -> Optional[Dict]:
    locale: Dict = next(
        iter(ingredient.get('locationVendorItems') or []),
        {}
    )
    vendor_items: List = locale.get('vendorItems') or []
    return (
        next((
            vi for vi in vendor_items
            if vi['priority'] == 0 and vi['ingredientListStr']
        ), None) or
        next(iter(vendor_items), None)
    )


def get_external_name(data: Dict) -> Optional[str]:
    """
    Generic method to return external name for a recipe, menu etc.
    If external name is not present or set to null, returns name.
    """
    if 'externalName' in data and data['externalName'] is not None:
        return data['externalName']
    elif 'name' in data:
        return data['name']
    return None


def calculate_servings(
    usage_quantity: Optional[float],
    nutritionals_quantity: Optional[float]
) -> Optional[float]:
    """
    Given a usage quantity (how much of a given component
    is included in a recipe) and a nutritionals_quantity
    (the size of one serving of the component),
    returns a number representing how many servings of the component
    are included in the recipe.
    """
    if usage_quantity is not None and nutritionals_quantity is not None:
        return usage_quantity / nutritionals_quantity
    return None


def calculate_serving_size_weight(
    weight: Optional[float],
    number_of_servings: Optional[float]
) -> Optional[float]:
    """
    Given a weight (representing the total weight of the
    component included in a recipe) and a number of servings
    (how many servings of the component are included),
    returns a number representing the weight of
    just one serving of the component.
    """
    if weight is not None and number_of_servings is not None:
        return weight / number_of_servings
    return None


def format_suggested_serving(
    value: Optional[float],
    unit: Optional[Dict]
) -> Optional[str]:
    if unit and 'name' in unit and value is not None:
        return f"{value} {unit['name']}"
    return None


class RecipeItem:
    def __init__(self, recipe_item: Dict) -> None:
        recipe_item = deepcopy(recipe_item)
        self.recipe_id = recipe_item.get('recipeId')
        self.ingredient = recipe_item.get('ingredient') or {}
        self.subrecipe = recipe_item.get('subRecipe') or {}
        self.preparations = recipe_item.get('preparations') or []
        self.nutrition = recipe_item.get('reconciledNutritionals') or {}
        self.quantity = recipe_item.get('quantity')
        self.unit = recipe_item.get('unit') or {}
        self.usages = recipe_item.get('usages') or []
        self.unit_values = self.unit.pop('unitValues', [])
        self.category_values = self.ingredient.pop('categoryValues', [])
        self.id = self.ingredient.get('id') or self.subrecipe.get('id')

    def is_standalone(self):
        return any(prep.get('id') == PreparationEnum.STANDALONE.value for prep in self.preparations)

    def is_packaging(self):
        return any(
            cv.get('id') == IngredientCategoryValueEnum.FOOD_PACKAGE.value and
            cv.get('category', {}).get('id') == IngredientCategoryTagTypeEnum.ACCOUNTING_TAG.value
            for cv in self.category_values
        )

    def get_label_name(self) -> Optional[str]:
        for cv in self.category_values:
            if cv.get('id') == IngredientCategoryValueEnum.LABEL.value:
                return get_external_name(self.ingredient)
        return None

    def mass(self, unit: str = UnitEnum.G.value):
        if self.unit and self.unit.get('id') == unit:
            return self.quantity

        if self.unit and self.unit.get('id') != unit:
            if self.unit_values:
                value = next((
                    uv.get('value') for uv in self.unit_values
                    if (uv.get('unit') or {}).get('id') == unit
                ), None)

                base = next((
                    uv.get('value') for uv in self.unit_values
                    if (uv.get('unit') or {}).get('id') == self.unit.get('id')
                ), None)

                if value is not None and base is not None:
                    return value / base * self.quantity
        return None

    def has_standalone_subrecipe(self):
        return self.is_standalone() and bool(self.subrecipe)

    def standalone_nutritionals_unit(self):
        if self.has_standalone_subrecipe():
            return self.subrecipe.get('nutritionalsUnit')
        return None

    def standalone_nutritionals_quantity(self):
        if self.has_standalone_subrecipe():
            return self.subrecipe.get('nutritionalsQuantity')
        return None

    def standalone_usage_quantity(self):
        """
        Returns the recipe item's usage quantity (how much
        of a given component is included in a recipe) based
        on the type of unit specified by the nutritonal unit
        (i.e. "oz"). Returns None if there is no quantity
        available for the specified unit.
        """
        unit = self.standalone_nutritionals_unit()
        if unit and 'id' in unit:
            return self.mass(unit['id'])
        return None


class FormattedRecipe:
    def __init__(self, recipe_data):
        self.id = recipe_data.get('id')
        self.name = get_external_name(recipe_data)
        self.notes = recipe_data.get('notes')
        self.description = recipe_data.get('description')
        self.is_sellable = recipe_data.get('isDish')
        self.menu_photo_url = get_menu_photo_url(recipe_data.get('files', {}).get('photos', []))
        self.nutrition = recipe_data.get('reconciledNutritionals', {})
        self.tags = get_recipe_category_tags(recipe_data.get('categoryValues', []))
        self.label_and_weights = get_recipe_label_and_weights(recipe_data.get('recipeItems', []))
        self.ingredients_and_standalone = get_recipe_ingredients_and_standalone_data(recipe_data)
        version_edges = recipe_data.get('versionConnection', {}).get('edges', [])
        self.version_id = version_edges[0].get('node', {}).get('id') if version_edges else None
        # A combined list of allergens across the base recipe and standalone subrecipe, if any.
        self.allergens = get_allergens(recipe_data.get('dietaryFlagsWithUsages', []))

    def to_dict(self):
        return {
            'id': self.id,
            'externalName': self.name,
            'version': self.version_id,
            'notes': self.notes,
            'description': self.description,
            'menuPhotoUrl': self.menu_photo_url,
            'nutrition': self.nutrition,
            'allergens': self.allergens,
            'hasAllergen': bool(self.allergens),
            **self.label_and_weights,
            **self.ingredients_and_standalone,
            **self.tags,
        }


def get_allergens(dietary_flags: List[Dict]) -> List:
    allergens = set(
        ALLERGEN_LABELS[allergen] for df in dietary_flags
        if (allergen := (
            df.get('dietaryFlag', {}).get('name')
            or df.get('name')
        )) and allergen in ALLERGEN_LABELS
    )
    return sorted(allergens)


def get_recipe_label_and_weights(recipe_items: List[Dict]) -> Dict:
    """
    Returns a dictionary containing gross weight of entire
    sellable package, net weight of only the base recipe +
    protein addons (minus standalone component), and label
    name for packaging.
    """
    net_weight, gross_weight, label = 0, 0, None

    for ri in recipe_items:
        recipe_item = RecipeItem(ri)
        label = recipe_item.get_label_name() or label
        mass = recipe_item.mass() or 0
        if (
            not recipe_item.is_packaging()
            and not recipe_item.is_standalone()
        ):
            net_weight += mass
        gross_weight += mass
    return {
        'labelName': label,
        'netWeight': round(net_weight),
        'grossWeight': round(gross_weight),
    }


def get_recipe_category_tags(category_values: List[Dict]) -> Dict:
    tag_labels: Dict = {
        RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value: 'proteinType',
        RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value: 'mealType',
        RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value: 'mealContainer',
        RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value: 'proteinAddOn',
        RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value: 'baseMealSlug',
        RecipeCategoryTagTypeEnum.BASE_MEAL_TAG.value: 'baseMeal',
        RecipeCategoryTagTypeEnum.HIGHLIGHT_ONE_TAG.value: 'highlightOne',
        RecipeCategoryTagTypeEnum.HIGHLIGHT_TWO_TAG.value: 'highlightTwo',
        RecipeCategoryTagTypeEnum.NO_NUTRITION_ON_WEBSITE_TAG.value: 'noNutritionOnWebsite'
    }
    recipe_tags = {
        label: name for cv in category_values
        if (
            (label := tag_labels.get(cv.get('category', {}).get('id')))
            and (name := cv.get('name'))
        )
    }
    recipe_tags = handle_website_nutrition_tag(recipe_tags)
    recipe_tags = format_highlight_tags(recipe_tags)
    return recipe_tags


def handle_website_nutrition_tag(recipe_tags: Dict) -> Dict:
    """
    Sets a default value of True for the displayNutritionOnWebsite attribute
    unless the noNutritionOnWebsite tag has been applied to the recipe
    """
    display_nutrition_on_website = True
    no_nutrition_on_website = recipe_tags.get('noNutritionOnWebsite')

    if no_nutrition_on_website:
        display_nutrition_on_website = False

    recipe_tags.pop('noNutritionOnWebsite', None)
    recipe_tags.setdefault('displayNutritionOnWebsite', display_nutrition_on_website)
    return recipe_tags


def format_highlight_tags(recipe_tags: Dict) -> Dict:
    """
    Transforms two separate highlight tag values into an array
    returned via the highlightTags attribute
    """
    highlight_tag_values = []

    for key, value in recipe_tags.items():
        if key in ('highlightOne', 'highlightTwo'):
            highlight_tag_values.append(value)

    recipe_tags.pop('highlightOne', None)
    recipe_tags.pop('highlightTwo', None)
    recipe_tags.setdefault('highlightTags', highlight_tag_values)
    return recipe_tags


def get_recipe_ingredients_and_standalone_data(recipe: Dict) -> Dict:
    components_usages, standalone_usages = [], []
    standalone = None

    for ri in (recipe.get('recipeItems') or []):
        recipe_item = RecipeItem(ri)

        if recipe_item.has_standalone_subrecipe():
            if not standalone:
                standalone = recipe_item
            else:
                logger.error(
                    f"{GALLEY_ERROR_PREFIX} Found more than one "
                    f"standalone for recipe: {recipe_item.recipe_id}."
                )

    for iu in (recipe.get('ingredientsWithUsages') or []):
        ingredient = RecipeItem(iu)

        if not ingredient.is_packaging():
            for usage in ingredient.usages:
                ingredient_usage = {
                    'ingredient': ingredient.ingredient,
                    'quantity': usage.get('quantity'),
                    'unit': usage.get('unit'),
                }

                if any(
                    ancestor.get('id') == standalone.id
                    for ancestor in usage.get('ancestorRecipes') if standalone
                ):
                    standalone_usages.append(ingredient_usage)
                else:
                    components_usages.append(ingredient_usage)
    return {
        'ingredients': format_ingredients_usages(components_usages),
        'baseRecipeAllergens': _format_base_recipe_allergens(components_usages),
        **format_standalone_data(standalone, standalone_usages)
    }


def _format_base_recipe_allergens(ingredients_usages: List) -> List:
    allergens = set()
    for iu in ingredients_usages:
        allergens |= set(get_allergens(iu['ingredient']['dietaryFlags']))
    return sorted(allergens)


def format_ingredients_usages(ingredients_usages: List) -> List:
    ingredients: Dict = {}

    for iu in ingredients_usages:
        ingredient = RecipeItem(iu)
        name = get_ingredient_name(ingredient.ingredient)
        usage = ingredient.mass(UnitEnum.OZ.value) or 0
        ingredients[name] = ingredients.get(name, 0) + usage
    return [
        ingredient for ingredient, usage in sorted(
            ingredients.items(),
            key=lambda x: (-x[1], x[0])
        )
    ]


def format_standalone_data(
    standalone: Optional[RecipeItem],
    standalone_usages: List
) -> Dict:
    standalone_data: Dict = {
        'hasStandalone': False,
        'standaloneRecipeId': None,
        'standaloneRecipeName': None,
        'standaloneNutrition': None,
        'standaloneIngredients': None,
        'standaloneNetWeight': None,
        'standaloneSuggestedServing': None,
        'standaloneServingSizeWeight': None,
        'standaloneServings': None,
        'standaloneAllergens': None,
    }

    if standalone and standalone.has_standalone_subrecipe():
        subrecipe = standalone.subrecipe
        standalone_recipe_item_net_weight = standalone.mass()
        standalone_nutritionals_quantity = standalone.standalone_nutritionals_quantity()
        standalone_nutritionals_unit = standalone.standalone_nutritionals_unit()
        standalone_usage_quantity = standalone.standalone_usage_quantity()
        standalone_servings = calculate_servings(standalone_usage_quantity, standalone_nutritionals_quantity)
        standalone_serving_size_weight = calculate_serving_size_weight(standalone_recipe_item_net_weight, standalone_servings)

        standalone_data['hasStandalone'] = standalone.is_standalone()
        standalone_data['standaloneRecipeId'] = standalone.id
        standalone_data['standaloneRecipeName'] = get_external_name(subrecipe)
        standalone_data['standaloneNutrition'] = subrecipe.get('reconciledNutritionals')
        standalone_data['standaloneAllergens'] = get_allergens(subrecipe.get('dietaryFlagsWithUsages', []))
        standalone_data['standaloneIngredients'] = format_ingredients_usages(standalone_usages)
        standalone_data['standaloneNetWeight'] = round(standalone_recipe_item_net_weight or 0) or None
        standalone_data['standaloneSuggestedServing'] = format_suggested_serving(standalone_nutritionals_quantity, standalone_nutritionals_unit)
        standalone_data['standaloneServingSizeWeight'] = round(standalone_serving_size_weight or 0) or None
        standalone_data['standaloneServings'] = standalone_servings or None
    return standalone_data


def format_title(text):
    return re.sub("(?<!\s)'S", "'s", text.title())


def get_meal_slug(menu_item: Dict) -> Optional[str]:
    categories = menu_item['recipe'].get('categoryValues', [])
    for category in categories:
        if category.get('category', {}).get('id', '') == RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value:
            return category['name']
    return None


def get_menu_photo_url(photos: List) -> Optional[str]:
    caption = rf'(?i){EntityMediaEnum.MENU_CAPTION.value}'
    return next((
        url for photo in photos
        if (
            bool(re.search(caption, photo.get('caption') or ''))
            and (url := photo.get('sourceUrl'))
        )
    ), None)


def get_item_code(menu_item: Dict) -> str:
    category_values = menu_item.get('categoryValues') or []
    for cv in category_values:
        if cv['category']['id'] == MenuItemCategoryEnum.PRODUCT_CODE.value:
            return cv['name']
    return ''


def get_menu_type(menu: Dict) -> str:
    category_values = menu.get('categoryValues') or []
    for cv in category_values:
        if cv['category']['id'] == MenuCategoryEnum.MENU_TYPE.value:
            return cv['name']
    return ''


# DATA TRANSFORMATION FUNCTIONS

def get_formatted_recipes_data(
    recipe_ids: List[str],
    location_name: str,
) -> Optional[List[Dict]]:
    if location_name is None:
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Location name required for recipe retrieval.")
    recipes_data = get_raw_recipes_data(recipe_ids, location_name) or []
    formatted_recipes = []
    for recipe_data in recipes_data:
        formatted_recipe = FormattedRecipe(recipe_data)
        formatted_recipes.append(formatted_recipe.to_dict())
    return formatted_recipes


def get_formatted_menu_data(
    dates: List[str],
    location_name: str = DEFAULT_LOCATION,
    menu_type: str = DEFAULT_MENU_TYPE,
    onlySellableMenuItems: bool = False
) -> Optional[List[Dict]]:
    menus = get_raw_menu_data(dates, location_name, menu_type)
    formatted_menus = []

    if not menus:
        return None

    for menu in menus:
        formatted_menu: Dict = {
            'name': menu.get('name'),
            'id': menu.get('id'),
            'date': menu.get('date'),
            'location': menu['location'].get('name'),
            'categoryMenuType': get_menu_type(menu),
            'menuItems': []
        }

        menu_items = menu.get('menuItems', [])
        for menu_item in menu_items:
            formatted_recipe = FormattedRecipe(recipe_data=menu_item.get('recipe', {}))
            formatted_recipe_dict = formatted_recipe.to_dict()

            if onlySellableMenuItems and not formatted_recipe.is_sellable:
                continue

            formatted_menu['menuItems'].append({
                'allergens': formatted_recipe_dict.get('allergens', []),
                'baseMeal': format_title(formatted_recipe.tags.get('baseMeal', '')),
                'deliveryDate': menu.get('date'),
                'hasAllergen': formatted_recipe_dict.get('hasAllergen', False),
                'highlightTags': formatted_recipe_dict.get('highlightTags', []),
                'id': menu_item.get('id'),
                'itemCode': get_item_code(menu_item),
                'mealSlug': get_meal_slug(menu_item),
                'recipeId': menu_item.get('recipeId'),
                'recipeMealType': formatted_recipe_dict.get('mealType', ''),
                'recipeMenuPhotoUrl': formatted_recipe_dict.get('menuPhotoUrl', ''),
                'recipeName': formatted_recipe_dict.get('externalName', ''),
                'recipeProteinType': formatted_recipe_dict.get('proteinType', ''),
            })
        formatted_menus.append(formatted_menu)
    return formatted_menus
