import re
import logging
from typing import Dict, List, Optional
from galley.common import DEFAULT_LOCATION, DEFAULT_MENU_TYPE, GALLEY_ERROR_PREFIX
from galley.queries import get_raw_menu_data, get_raw_recipes_data
from galley.enums import (DietaryFlagEnum,
                          IngredientCategoryTagTypeEnum,
                          IngredientCategoryValueEnum,
                          MenuCategoryEnum,
                          MenuItemCategoryEnum,
                          PreparationEnum,
                          QuantityUnitEnum as UnitEnum,
                          RecipeCategoryTagTypeEnum,
                          RecipeMediaEnum,
                          IngredientFormatOptionEnum as FormatIngredientEnum)


logger = logging.getLogger(__name__)


def get_external_name_for_ingredient(data_dict):
    """
    Checks for locationVendorItem and vendorItem,and if present returns the ingredient externalName
    plus the vendorItem ingredientListStr for the vendorItem.
    If more than one vendorItem, uses the ingredientListStr for the vendorItem with priority.
    If no locationVendorItems or no ingredientListStr, returns externalName. If no externalName, returns name.
    """
    FIRST_AND_ONLY_ITEM = 0
    if 'externalName' in data_dict and data_dict['externalName'] is not None:
        if 'locationVendorItems' in data_dict and data_dict['locationVendorItems'] is not None:
            locationVendorItems = data_dict['locationVendorItems']
            if len(locationVendorItems) and locationVendorItems[FIRST_AND_ONLY_ITEM]['vendorItems']:
                vendorItems = locationVendorItems[FIRST_AND_ONLY_ITEM]['vendorItems']
                if len(vendorItems) > 1:
                    for vendorItem in vendorItems:
                        if vendorItem['priority'] == 0:
                            if vendorItem['ingredientListStr']:
                                return f"{data_dict['externalName']} ({vendorItem['ingredientListStr']})"
                            else:
                                return data_dict['externalName']
                else:
                    vendorItem = vendorItems[FIRST_AND_ONLY_ITEM]
                    if vendorItem['ingredientListStr']:
                        return f"{data_dict['externalName']} ({vendorItem['ingredientListStr']})"
                    else:
                        return data_dict['externalName']
        else:
            return data_dict['externalName']
    else:
         if 'name' in data_dict:
            return data_dict['name']
    return None


def get_external_name(data_dict):
    """
    Generic method to return external name for a recipe, menu etc.
    If external name is not present or set to null, returns name.
    """
    if 'externalName' in data_dict and data_dict['externalName'] is not None:
        return data_dict['externalName']
    else:
        if 'name' in data_dict:
            return data_dict['name']
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
        return usage_quantity/nutritionals_quantity
    else:
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
        return weight/number_of_servings
    else:
        return None


def format_suggested_serving(
    quantity: Optional[float],
    unit: Optional[str]
) -> Optional[str]:
    if quantity is not None and unit is not None:
        return "{} {}".format(quantity, unit)
    else:
        return None


class RecipeItem:
    def __init__(
        self,
        subrecipe=None,
        nutrition=None,
        ingredient=None,
        unit_values=None,
        preparations: Optional[List[Dict[str, str]]]=None
    ):
        self.subrecipe = subrecipe
        self.nutrition = nutrition
        self.ingredient = ingredient
        self.unit_values = unit_values
        self.preparations = preparations
        self.category_values = ingredient.get('categoryValues', []) if ingredient else []
        self.usages = subrecipe.get('allIngredientsWithUsages', []) if subrecipe else []

    def is_standalone(self):
        return any(prep.get('id') == \
            PreparationEnum.STANDALONE.value for prep in self.preparations)

    def is_packaging(self):
        return any(
            cat_val.get('id') == \
                IngredientCategoryValueEnum.FOOD_PACKAGE.value and
            cat_val.get('category', {}).get('id') == \
                IngredientCategoryTagTypeEnum.ACCOUNTING_TAG.value \
                    for cat_val in self.category_values
        )

    def get_label_name(self) -> Optional[str]:
        for cat_val in self.category_values:
            if cat_val.get('id') == IngredientCategoryValueEnum.LABEL.value:
                external_name = self.ingredient.get('externalName')
                if external_name:
                    return external_name
                return self.ingredient.get('name')
        return None

    def mass(self, unit: str='g'):
        if self.unit_values is None:
            raise Exception('Cannot get mass without quantity unit values')
        return next((value.get('value') for value in self.unit_values
                     if (value.get('unit') or {}).get('name') == unit), 0)

    def has_standalone_subrecipe(self):
        return self.is_standalone and self.subrecipe is not None

    def standalone_nutritionals_unit(self):
        result = None
        if self.has_standalone_subrecipe:
            unit = self.subrecipe.get('nutritionalsUnit')
            if unit is not None:
                result = unit.get('name')
        return result

    def standalone_nutritionals_quantity(self):
        if self.has_standalone_subrecipe:
            return self.subrecipe.get('nutritionalsQuantity')
        else:
            return None

    def standalone_usage_quantity(self):
        """
        Returns the recipe item's usage quantity
        (how much of a given component is included in a recipe)
        based on the type of unit specified by the
        nutritonals_unit (i.e. "oz"). Returns None if there is
        not a quantity available for the specified unit.
        """
        nutritionals_unit = self.standalone_nutritionals_unit()
        if nutritionals_unit is not None and self.unit_values is not None:
            return next((value.get('value') for value in self.unit_values
                         if (value.get('unit') or {}).get('name') == nutritionals_unit), None)
        else:
            return None

    def get_ingredients_usages(self):
        ingredients = {}

        if self.ingredient:
            name = get_external_name_for_ingredient(self.ingredient)
            ingredients[name] = self.mass('oz')

        elif self.subrecipe:
            rtc = self.subrecipe.get('recipeTreeComponents') or {}

            if rtc:
                unit = rtc[0].get('unit') or {}
                rtc_item = RecipeItem(unit_values=rtc[0].get('quantityUnitValues'))
                max_batch = rtc[0].get('quantity') if \
                            unit.get('id') == UnitEnum.OZ.value else \
                            rtc_item.mass('oz')

                if self.usages:
                    for usage in self.usages:
                        unit = usage.get('unit') or {}
                        usage_item = RecipeItem(ingredient=usage.get('ingredient'),
                                                unit_values=usage.get('totalQuantityUnitValues'))
                        quantity = usage.get('totalQuantity') if \
                                   unit.get('id') == UnitEnum.OZ.value else \
                                   usage_item.mass('oz')
                        name = get_external_name_for_ingredient(usage_item.ingredient)
                        subquantity = quantity * (self.mass('oz') / max_batch)
                        ingredients[name] = ingredients.get(name, 0) + subquantity
        return ingredients

class FormattedRecipe:
    def __init__(
        self,
        recipe_data,
        **format_options
    ):
        self.format = self.format_options(format_options)
        self.galleyId = recipe_data.get('id')
        self.externalName = get_external_name(recipe_data)
        self.notes = recipe_data.get('notes')
        self.description = recipe_data.get('description')
        self.isSellable = recipe_data.get('isDish')
        self.menuPhotoUrl = get_menu_photo_url(recipe_data.get('media', []))
        self.plate_photo_url = get_plate_photo_url(recipe_data.get('files', {}).get('photos', []))
        self.nutrition = recipe_data.get('reconciledNutritionals', {})
        self.recipe_category_values = recipe_data.get('categoryValues', [])
        self.recipe_tags = get_recipe_category_tags(self.recipe_category_values)
        self.recipe_items = recipe_data.get('recipeItems', [])
        self.recipe_tree_components = recipe_data.get('recipeTreeComponents') or []
        self.formatted_recipe_tree_components_data = format_recipe_tree_components_data(self.recipe_tree_components)
        self.ingredients_usages = self.formatted_recipe_tree_components_data.get('ingredients')
        self.standalone_ingredients_usages = self.formatted_recipe_tree_components_data.get('standaloneIngredients')
        self.allergens = get_recipe_allergens(recipe_dietry_flags=recipe_data.get('dietaryFlagsWithUsages', []))
        version_edges = recipe_data.get('versionConnection', {}).get('edges', [])
        self.version_id = version_edges[0].get('node', {}).get('id') if version_edges else None

    def format_options(self, options):
        self.validate_format_options(options)
        return {
            FormatIngredientEnum.INCLUDE_USAGES.value: False,
            **options
        }

    def validate_format_options(self, options):
        validator = {
            FormatIngredientEnum.INCLUDE_USAGES.value: (bool, 'missing boolean value')
        }

        for option, value in options.items():
            if option in validator and type(value) != validator[option][0]:
                raise Exception(f'"{option}" {validator[option][1]}')
            elif option not in validator:
                raise Exception(f'"{option}" is not a valid option.')
        return None

    def format_ingredients(self):
        if self.format[FormatIngredientEnum.INCLUDE_USAGES.value] is False:
            if self.ingredients_usages:
                self.formatted_recipe_tree_components_data.update(dict(
                    ingredients=\
                        [ingredient for ingredient, _ in self.ingredients_usages]
                ))
            if self.standalone_ingredients_usages:
                self.formatted_recipe_tree_components_data.update(dict(
                    standaloneIngredients=\
                        [ingredient for ingredient, _ in self.standalone_ingredients_usages]
                ))


    def to_dict(self):
        self.format_ingredients()
        return dict(id=self.galleyId,
                    externalName=self.externalName,
                    version=self.version_id,
                    notes=self.notes,
                    description=self.description,
                    menuPhotoUrl=self.menuPhotoUrl,
                    nutrition=self.nutrition,
                    **self.formatted_recipe_tree_components_data,
                    **self.recipe_tags,
                    **self.allergens)


def get_recipe_allergens(recipe_dietry_flags: List[Dict]) -> Dict:
    dietary_flags_mapping = {
        DietaryFlagEnum.TREE_NUTS.value: 'tree nuts',
        DietaryFlagEnum.SOY_BEANS.value: 'soy',
        DietaryFlagEnum.SHELLFISH.value: 'shellfish',
        DietaryFlagEnum.PORK.value: 'pork',
        DietaryFlagEnum.FISH.value: 'fish',
        DietaryFlagEnum.COCONUT.value: 'coconut',
        DietaryFlagEnum.PEANUTS.value: 'peanuts',
        DietaryFlagEnum.LAMB.value: 'lamb',
        DietaryFlagEnum.SMOKED_MEATS.value: 'smoked meats',
        DietaryFlagEnum.BEEF.value: 'beef'
    }
    allergens = []

    for recipe_dietary_flag in recipe_dietry_flags:
        dietary_flag = recipe_dietary_flag.get('dietaryFlag', None)
        if dietary_flag and 'id' in dietary_flag:
            flag_id = dietary_flag.get('id')
            dietary_flag_name = dietary_flags_mapping.get(flag_id, None)
            if dietary_flag_name:
                allergens.append(dietary_flag_name)

    return dict(hasAllergen=True if len(allergens) > 0 else False,
                allergens=allergens)


def get_recipe_category_tags(
    recipe_category_values: List[Dict]
) -> Dict:
    recipe_tags: Dict = {}
    recipe_tag_labels: Dict = {
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

    for recipe_category_value in recipe_category_values:
        tag_id = recipe_category_value.get('category', {}).get('id')
        label = recipe_tag_labels.get(tag_id)
        recipe_category_value_name = recipe_category_value.get('name')

        if label and recipe_category_value_name:
            recipe_tags.setdefault(label, recipe_category_value_name)

    recipe_tags = handle_website_nutrition_tag(recipe_tags)
    recipe_tags = format_highlight_tags(recipe_tags)
    return recipe_tags


def handle_website_nutrition_tag(
    recipe_tags: Dict
) -> Dict:
    """
    Sets a default value of True for the displayNutritionOnWebsite attribute
    unless the noNutritionOnWebsite tag has been applied to the recipe
    """
    display_nutrition_on_website = True
    no_nutrition_on_website = recipe_tags.get('noNutritionOnWebsite', None)

    if no_nutrition_on_website:
        display_nutrition_on_website = False

    recipe_tags.pop('noNutritionOnWebsite', None)
    recipe_tags.setdefault('displayNutritionOnWebsite', display_nutrition_on_website)
    return recipe_tags


def format_highlight_tags(
    recipe_tags: Dict
) -> Dict:
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


def format_recipe_tree_components_data(
    recipe_tree_components: List[Dict]
) -> Dict:
    """
    Returns a dictionary containing total weight of recipe and
    subrecipe details.
    """
    net_weight, gross_weight = 0, 0
    subcomponents, standalones = [], []

    label_name = None
    for recipe_tree_component in recipe_tree_components:
        recipe_item = recipe_tree_component.get('recipeItem') or {}
        if recipe_item:
            recipe_item = RecipeItem(
                unit_values=recipe_tree_component.get('quantityUnitValues', []),
                preparations=recipe_item.get('preparations', []),
                ingredient=recipe_item.get('ingredient', {}),
                nutrition=recipe_item.get('reconciledNutritionals'),
                subrecipe=recipe_item.get('subRecipe'),
            )
            mass = recipe_item.mass() if recipe_item.mass() else 0

            component_label_name = recipe_item.get_label_name()
            if component_label_name:
                label_name = component_label_name

            if recipe_item.is_packaging():
                gross_weight += mass
            elif recipe_item.is_standalone():
                if recipe_item.subrecipe:
                    gross_weight += mass
                    standalones.append(recipe_item)
            else:
                net_weight += mass
                gross_weight += mass
                subcomponents.append(recipe_item)

    standalone = standalones[0] if standalones else None

    if len(standalones) > 1:
        logger.error(f"More than one standalone recipe items found for recipe "
                     f"tree component id {recipe_tree_component.get('id')}")

    return dict(ingredients=get_ingredients_data(subcomponents),
                netWeight=round(net_weight),
                grossWeight=round(gross_weight),
                hasStandalone=bool(standalones),
                labelName=label_name,
                **format_standalone_data(standalone))


def get_ingredients_data(data: List):
    ingredients: Dict = {}

    for item in data:
        usages = item.get_ingredients_usages()
        for ingredient, usage in usages.items():
            ingredients[ingredient] = ingredients.get(ingredient, 0) + usage
    return sorted(ingredients.items(), key=lambda x: (-x[1], x[0]))


def format_standalone_data(standalone_data):
    standalone = {
        'standaloneRecipeId': None,
        'standaloneRecipeName': None,
        'standaloneNutrition': None,
        'standaloneIngredients': None,
        'standaloneNetWeight': None,
        'standaloneSuggestedServing': None,
        'standaloneServingSizeWeight': None,
        'standaloneServings': None
    }

    if standalone_data:
        subrecipe = standalone_data.subrecipe
        if subrecipe:
            standalone_recipe_item_net_weight = standalone_data.mass()
            standalone_nutritionals_quantity = standalone_data.standalone_nutritionals_quantity()
            standalone_nutritionals_unit = standalone_data.standalone_nutritionals_unit()
            standalone_usage_quantity = standalone_data.standalone_usage_quantity()
            standalone_servings = calculate_servings(standalone_usage_quantity, standalone_nutritionals_quantity)
            standalone_serving_size_weight = calculate_serving_size_weight(standalone_recipe_item_net_weight, standalone_servings)

            standalone['standaloneRecipeId'] = subrecipe.get('id')
            standalone['standaloneRecipeName'] = get_external_name(subrecipe)
            standalone['standaloneNutrition'] = subrecipe.get('reconciledNutritionals')
            standalone['standaloneIngredients'] = get_ingredients_data([standalone_data])
            standalone['standaloneNetWeight'] = round(standalone_recipe_item_net_weight) if standalone_recipe_item_net_weight else None
            standalone['standaloneSuggestedServing'] = format_suggested_serving(standalone_nutritionals_quantity, standalone_nutritionals_unit)
            standalone['standaloneServingSizeWeight'] = round(standalone_serving_size_weight) if standalone_serving_size_weight else None
            standalone['standaloneServings'] = standalone_servings if standalone_servings else None
    return standalone


def format_title(text):
    return re.sub("(?<!\s)'S", "'s", text.title())


def get_meal_slug(menu_item: Dict) -> Optional[str]:
    categories = menu_item['recipe'].get('categoryValues', [])
    for category in categories:
        if category.get('category', {}).get('id', '') == RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value:
            return category['name']
    return None


def get_menu_photo_url(media: List) -> Optional[str]:
    for photo in media:
        if photo.get('caption', '') == RecipeMediaEnum.MENU_CAPTION.value and photo.get('sourceUrl', None):
            return photo.get('sourceUrl')
    return None


def get_plate_photo_url(photos: List) -> Optional[str]:
    for photo in photos:
        if photo.get('caption') == RecipeMediaEnum.PLATE_CAPTION.value and photo.get('sourceUrl'):
            return photo.get('sourceUrl')
    return None


def get_meal_code(menu_item_category_values) -> str:
    if menu_item_category_values:
        for category_value in menu_item_category_values:
            if (category_value['category']['id'] == MenuItemCategoryEnum.PRODUCT_CODE.value):
                return category_value['name']
    return ''


def get_category_menu_type(menu_category_values) -> str:
    if menu_category_values:
        for category_value in menu_category_values:
            if (category_value['category']['id'] == MenuCategoryEnum.MENU_TYPE.value):
                return category_value['name']
    return ''


# DATA TRANSFORMATION FUNCTIONS

def get_formatted_recipes_data(
    recipe_ids: List[str],
    location_name: str,
    **format_options: Dict
) -> Optional[List[Dict]]:
    if location_name is None:
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Location name required for recipe retrieval.")
    recipes_data = get_raw_recipes_data(recipe_ids=recipe_ids, location_name=location_name) or []
    formatted_recipes = []
    for recipe_data in recipes_data:
        formatted_recipe = FormattedRecipe(recipe_data, **format_options)
        formatted_recipes.append(formatted_recipe.to_dict())
    return formatted_recipes


def get_formatted_menu_data(
    dates: List[str],
    location_name: str=DEFAULT_LOCATION,
    menu_type: str=DEFAULT_MENU_TYPE,
    onlySellableMenuItems: bool=False
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
            'menuItems': []
        }

        categoryValues = menu['categoryValues']
        for categoryValue in categoryValues:
            if (categoryValue['category']['id'] == MenuCategoryEnum.MENU_TYPE.value):
                formatted_menu['categoryMenuType'] = categoryValue['name']

        menu_items = menu.get('menuItems', [])
        for menu_item in menu_items:
            formatted_recipe = FormattedRecipe(recipe_data=menu_item.get('recipe', {}))
            formatted_recipe_dict = formatted_recipe.to_dict()
            itemCode = ''
            categoryValues = menu_item['categoryValues']
            for categoryValue in categoryValues:
                if (categoryValue['category']['id'] == MenuItemCategoryEnum.PRODUCT_CODE.value):
                    itemCode = categoryValue['name']

            if onlySellableMenuItems and not formatted_recipe.isSellable:
                continue

            formatted_menu['menuItems'].append({
                'allergens': formatted_recipe_dict.get('allergens', []),
                'baseMeal': format_title(formatted_recipe.recipe_tags.get('baseMeal', '')),
                'deliveryDate': menu.get('date'),
                'hasAllergen': formatted_recipe_dict.get('hasAllergen', False),
                'highlightTags': formatted_recipe_dict.get('highlightTags', []),
                'id': menu_item.get('id'),
                'itemCode': itemCode,
                'mealSlug': get_meal_slug(menu_item),
                'recipeId': menu_item.get('recipeId'),
                'recipeMealType': formatted_recipe_dict.get('mealType', ''),
                'recipeMenuPhotoUrl': formatted_recipe_dict.get('menuPhotoUrl', ''),
                'recipeName': formatted_recipe_dict.get('externalName', ''),
                'recipeProteinType': formatted_recipe_dict.get('proteinType', ''),
            })
        formatted_menus.append(formatted_menu)
    return formatted_menus
