import re
import logging
from typing import Dict, List, Optional
from galley.queries import get_raw_menu_data, get_raw_recipes_data
from galley.enums import (
    DietaryFlagEnum,
    IngredientCategoryTagTypeEnum,
    IngredientCategoryValueEnum,
    MenuCategoryEnum,
    MenuItemCategoryEnum,
    PreparationEnum,
    QuantityUnitEnum,
    RecipeCategoryTagTypeEnum,
    RecipeMediaEnum,
    IngredientFormatOptionEnum as FormatIngredientEnum
)


logger = logging.getLogger(__name__)


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
        ingredient=None,
        subrecipe=None,
        nutrition=None,
        quantity_unit_values=None,
        preparations: Optional[List[Dict[str, str]]]=None
    ):
        self.category_values = ingredient.get('categoryValues', []) if ingredient else []
        self.quantity_unit_values = quantity_unit_values
        self.preparations = preparations
        self.nutrition = nutrition
        self.subrecipe = subrecipe

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

    def mass(self, unit: str='g'):
        if self.quantity_unit_values is None:
            raise Exception('Cannot calculate mass without quantity unit values')
        return next(
            (value.get('value') for value in self.quantity_unit_values
             if (value.get('unit') or {}).get('name') == unit), 0
        )

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
        if nutritionals_unit is not None and \
            self.quantity_unit_values is not None:
            return next(
                (value.get('value') for value in self.quantity_unit_values
                 if (value.get('unit') or {}).get('name') == nutritionals_unit), None
            )
        else:
            return None


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
        self.allIngredientsWithUsages = get_ingredients_usages(recipe_data.get('allIngredientsWithUsages', []))
        self.plate_photo_url = get_plate_photo_url(recipe_data.get('files', {}).get('photos', []))
        self.nutrition = recipe_data.get('reconciledNutritionals', {})
        self.recipe_category_values = recipe_data.get('categoryValues', [])
        self.recipe_tags = get_recipe_category_tags(self.recipe_category_values)
        self.recipe_items = recipe_data.get('recipeItems', [])
        self.recipe_tree_components = recipe_data.get('recipeTreeComponents', [])
        self.formatted_recipe_tree_components_data = format_recipe_tree_components_data(self.recipe_tree_components)
        self.standalone_usages = self.formatted_recipe_tree_components_data['standaloneIngredients']
        self.recipe_usages = self.recipe_ingredients_usages()
        self.allergens = get_recipe_allergens(recipe_dietry_flags=recipe_data.get('dietaryFlagsWithUsages', []))
        version_edges = recipe_data.get('versionConnection', {}).get('edges', [])
        self.version_id = version_edges[0].get('node', {}).get('id') if version_edges else None

    def format_options(self, options):
        return {
            FormatIngredientEnum.USAGES.value: False,
            FormatIngredientEnum.UNIT.value: 'oz',
            **options
        }

    def recipe_ingredients_usages(self):
        ingredients = self.allIngredientsWithUsages
        if self.standalone_usages:
            for ingredient, usage in self.standalone_usages.items():
                ingredients[ingredient] -= usage
                if ingredients[ingredient] <= 0:
                    del ingredients[ingredient]
        return ingredients

    def ingredients_by_usage(self, is_standalone):
        ingredients = self.standalone_usages if \
                      is_standalone else \
                      self.recipe_usages

        if not ingredients:
            return None

        sorted_usages = sorted(ingredients.items(),
                               key=lambda x: x[1],
                               reverse=True)
        return sorted_usages if \
               self.format[FormatIngredientEnum.USAGES.value] else \
               list(ingredient for ingredient, _ in sorted_usages)

    def to_dict(self):
        self.formatted_recipe_tree_components_data.update(dict(
            standaloneIngredients=self.ingredients_by_usage(1)
        ))
        return dict(id=self.galleyId,
                    externalName=self.externalName,
                    version=self.version_id,
                    notes=self.notes,
                    description=self.description,
                    menuPhotoUrl=self.menuPhotoUrl,
                    ingredients=self.ingredients_by_usage(0),
                    nutrition=self.nutrition,
                    **self.formatted_recipe_tree_components_data,
                    **self.recipe_tags,
                    **self.allergens)


def get_ingredients_usages(data: List[Dict]) -> Dict:
    ingredients = {}

    for usage in data:
        unit = usage.get('unit') or {}
        ingredient = usage.get('ingredient') or {}
        quantities = usage.get('totalQuantityUnitValues') or []
        recipe_item = RecipeItem(ingredient=ingredient,
                                 quantity_unit_values=quantities)

        name = get_external_name(ingredient)
        quantity = usage.get('totalQuantity') \
                   if unit.get('id') == QuantityUnitEnum.OZ.value \
                   else recipe_item.mass('oz')

        if not recipe_item.is_packaging():
            ingredients[name] = ingredients.get(name, 0) + quantity
    return ingredients


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
        RecipeCategoryTagTypeEnum.NO_NUTRITION_ON_WEBSITE_TAG.value: 'noNutritionOnWebsite',
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
    net_weight = 0
    gross_weight = 0
    standalone_recipe_items = []
    for recipe_tree_component in recipe_tree_components:
        recipe_item_dict = recipe_tree_component.get('recipeItem', {})
        if recipe_item_dict:
            recipe_item = RecipeItem(
                preparations=recipe_item_dict.get('preparations', []),
                ingredient=recipe_item_dict.get('ingredient', {}),
                quantity_unit_values=recipe_tree_component.get('quantityUnitValues', []),
                nutrition=recipe_item_dict.get('reconciledNutritionals'),
                subrecipe=recipe_item_dict.get('subRecipe')
            )

            item_weight = recipe_item.mass() if recipe_item.mass() else 0

            if recipe_item.is_packaging():
                gross_weight += item_weight
            elif recipe_item.is_standalone():
                if recipe_item.subrecipe:
                    standalone_recipe_items.append(recipe_item)
                    gross_weight += item_weight
            else:
                net_weight += item_weight
                gross_weight += item_weight

    standalone_recipe_item = standalone_recipe_items[0] if\
        standalone_recipe_items else None

    if len(standalone_recipe_items) > 1:
        logger.error("More than one standalone recipe items found for recipe"
                     f"tree component id {recipe_tree_component.get('id')}")

    standalone_data = format_standalone_data(standalone_recipe_item)

    return dict(netWeight=round(net_weight),
                grossWeight=round(gross_weight),
                hasStandalone=True if standalone_recipe_item else False,
                **standalone_data)


def format_standalone_data(standalone_recipe_item):
    standalone_data = {
        'standaloneRecipeId': None,
        'standaloneRecipeName': None,
        'standaloneIngredients': None,
        'standaloneNutrition': None,
        'standaloneNetWeight': None,
        'standaloneSuggestedServing': None,
        'standaloneServingSizeWeight': None,
        'standaloneServings': None
    }

    if standalone_recipe_item:
        standalone_subrecipe = standalone_recipe_item.subrecipe
        if standalone_subrecipe:
            standalone_recipe_item_net_weight = standalone_recipe_item.mass()
            standalone_nutritionals_quantity = standalone_recipe_item.standalone_nutritionals_quantity()
            standalone_nutritionals_unit = standalone_recipe_item.standalone_nutritionals_unit()
            standalone_usage_quantity = standalone_recipe_item.standalone_usage_quantity()
            standalone_servings = calculate_servings(standalone_usage_quantity, standalone_nutritionals_quantity)
            standalone_serving_size_weight = calculate_serving_size_weight(standalone_recipe_item_net_weight, standalone_servings)

            standalone_data['standaloneRecipeId'] = standalone_subrecipe.get('id')
            standalone_data['standaloneRecipeName'] = get_external_name(standalone_subrecipe)
            standalone_data['standaloneIngredients'] = get_ingredients_usages(standalone_subrecipe.get('allIngredientsWithUsages'))
            standalone_data['standaloneNutrition'] = standalone_subrecipe.get('reconciledNutritionals')
            standalone_data['standaloneNetWeight'] = round(standalone_recipe_item_net_weight) if standalone_recipe_item_net_weight else None
            standalone_data['standaloneSuggestedServing'] = format_suggested_serving(standalone_nutritionals_quantity, standalone_nutritionals_unit)
            standalone_data['standaloneServingSizeWeight'] = round(standalone_serving_size_weight) if standalone_serving_size_weight else None
            standalone_data['standaloneServings'] = standalone_servings if standalone_servings else None
    return standalone_data


def format_title(text):
  return re.sub("(?<!\s)'S", "'s", text.title())


# def ingredients_from_recipe_items(recipe_items: List[Dict]) -> Optional[List]:
#     ingredients: List[str] = []

#     for recipeItem in recipe_items:
#         ingredient = recipeItem.get('ingredient')
#         sub_recipe = recipeItem.get('subRecipe')
#         recipe_item = RecipeItem(
#             ingredient=ingredient if ingredient else None,
#             preparations=recipeItem.get('preparations', [])
#         )

#         # Top Level Ingredient
#         if ingredient:
#             external_name = get_external_name(ingredient)
#             if not recipe_item.is_packaging() and external_name not in ingredients:
#                 ingredients.append(external_name)

#         # SubRecipe Ingredients
#         elif sub_recipe:
#             if not recipe_item.is_standalone():
#                 for _ingredient in sub_recipe.get('allIngredients'):
#                     if _ingredient not in ingredients:
#                         ingredients.append(_ingredient)
#     return ingredients


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
    **formatOptions: Dict
) -> Optional[List[Dict]]:
    recipes_data = get_raw_recipes_data(recipe_ids=recipe_ids) or []
    formatted_recipes = []
    for recipe_data in recipes_data:
        formatted_recipe = FormattedRecipe(recipe_data=recipe_data, **formatOptions)
        formatted_recipes.append(formatted_recipe.to_dict())
    return formatted_recipes


def get_formatted_menu_data(
    dates: List[str],
    location_name: str="Vacaville",
    menu_type: str="production",
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
