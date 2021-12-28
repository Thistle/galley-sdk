import logging
from typing import Dict, List, Optional

from galley.enums import (IngredientCategoryTagTypeEnum,
                          IngredientCategoryValueEnum, MenuCategoryEnum,
                          MenuItemCategoryEnum, PreparationEnum,
                          RecipeCategoryTagTypeEnum)
from galley.queries import get_raw_menu_data, get_raw_recipes_data

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



class RecipeItem:
    def __init__(self, preparations: List[Dict[str, str]], ingredient=None,
                 quantity_unit_values=None, nutrition=None, subrecipe=None):
        self.category_values = ingredient.get('categoryValues', []) if ingredient else []
        self.preparations = preparations
        self.quantity_unit_values = quantity_unit_values
        self.nutrition = nutrition
        self.subrecipe = subrecipe

    def is_standalone(self):
        return any(prep.get('id') == PreparationEnum.STANDALONE.value for prep in self.preparations)

    def is_packaging(self):
        return any(
            cat_val.get('id') == IngredientCategoryValueEnum.FOOD_PACKAGE.value and
            cat_val.get('category', {}).get('id') == IngredientCategoryTagTypeEnum.ACCOUNTING_TAG.value for cat_val in self.category_values
        )

    def mass(self):
        if self.quantity_unit_values is None:
            raise Exception('Cannot calculate mass without unit values')
        return next(
            (value.get('value') for value in self.quantity_unit_values
             if value.get('unit', {'name': None}).get('name') == 'g'), 0
        )


class FormattedRecipe:
    def __init__(self, recipe_data):
        self.galleyId = recipe_data.get('id')
        self.externalName = get_external_name(recipe_data)
        self.notes = recipe_data.get('notes')
        self.description = recipe_data.get('description')
        self.nutrition = recipe_data.get('reconciledNutritionals', {})
        self.recipe_category_values = recipe_data.get('categoryValues', [])
        self.recipe_tags = get_recipe_category_tags(self.recipe_category_values)
        self.recipe_items = recipe_data.get('recipeItems', [])
        self.recipe_tree_components = recipe_data.get('recipeTreeComponents', [])
        self.formatted_recipe_tree_components_data = \
            format_recipe_tree_components_data(self.recipe_tree_components)


    def to_dict(self):
        return {
            'id': self.galleyId,
            'externalName': self.externalName,
            'notes': self.notes,
            'description': self.description,
            'nutrition': self.nutrition,
            'ingredients': ingredients_from_recipe_items(recipe_items=self.recipe_items),
            **self.formatted_recipe_tree_components_data,
            **self.recipe_tags
        }


def get_recipe_category_tags(recipe_category_values: List[Dict]) -> Optional[Dict]:
    recipe_tags: Dict = {}
    recipe_tag_labels: Dict = {
        RecipeCategoryTagTypeEnum.PROTEIN_TYPE_TAG.value: 'proteinType',
        RecipeCategoryTagTypeEnum.MEAL_TYPE_TAG.value: 'mealType',
        RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value: 'mealContainer',
        RecipeCategoryTagTypeEnum.PROTEIN_ADDON_TAG.value: 'proteinAddOn',
        RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value: 'baseMealSlug',
    }

    for recipe_category_value in recipe_category_values:
        tag_id = recipe_category_value.get('category', {}).get('id')
        label = recipe_tag_labels.get(tag_id)
        recipe_category_value_name = recipe_category_value.get('name')

        if label and recipe_category_value_name:
            recipe_tags.setdefault(label, recipe_category_value_name)
    return recipe_tags


def format_recipe_tree_components_data(recipe_tree_components: List[Dict]) -> Dict:
    """
    Returns a dictionary containing total weight of recipe and
    subrecipe details.
    """
    total_weight = 0
    standalone_recipe_items = []
    for recipe_tree_component in recipe_tree_components:
        recipe_item_dict = recipe_tree_component.get('recipeItem', {})
        if recipe_item_dict:
            recipe_item = RecipeItem(
                preparations=recipe_item_dict.get('preparations', []),
                ingredient=recipe_item_dict.get('ingredient', {}),
                quantity_unit_values=recipe_tree_component.get(
                    'quantityUnitValues', []),
                nutrition=recipe_item_dict.get('reconciledNutritionals'),
                subrecipe=recipe_item_dict.get('subRecipe')
            )

            if recipe_item.is_packaging():
                continue
            elif recipe_item.is_standalone():
                if recipe_item.subrecipe:
                    standalone_recipe_items.append(recipe_item)
            else:
                total_weight += recipe_item.mass() if recipe_item.mass() else 0

    standalone_recipe_item = standalone_recipe_items[0] if\
        standalone_recipe_items else None

    if len(standalone_recipe_items) > 1:
        logger.error("More than one standalone recipe items found for recipe"
                     f"tree component id {recipe_tree_component.get('id')}")

    standalone_data = {
        'standaloneRecipeId': None,
        'standaloneRecipeName': None,
        'standaloneNutrition': None,
        'standaloneIngredients': None,
        'standaloneWeight': None
    }

    if standalone_recipe_item:
        standalone_subrecipe = standalone_recipe_item.subrecipe
        if standalone_subrecipe:
            standalone_recipe_item_weight = standalone_recipe_item.mass()
            standalone_data['standaloneRecipeId'] = standalone_subrecipe.get('id')
            standalone_data['standaloneRecipeName'] = get_external_name(standalone_subrecipe)
            standalone_data['standaloneNutrition'] = standalone_subrecipe.get('reconciledNutritionals')
            standalone_data['standaloneIngredients'] = standalone_subrecipe.get('allIngredients')
            standalone_data['standaloneWeight'] = round(standalone_recipe_item_weight, 2) if standalone_recipe_item_weight else None

    return {
        'weight': round(total_weight, 2),
        **standalone_data
    }


def ingredients_from_recipe_items(recipe_items: List[Dict]) -> Optional[List]:
    ingredients: List[str] = []

    for recipeItem in recipe_items:
        ingredient = recipeItem.get('ingredient')
        sub_recipe = recipeItem.get('subRecipe')
        recipe_item = RecipeItem(
            ingredient=ingredient if ingredient else None,
            preparations=recipeItem.get('preparations', [])
        )

        # Top Level Ingredient
        if ingredient:
            external_name = get_external_name(ingredient)
            if not recipe_item.is_packaging() and external_name not in ingredients:
                ingredients.append(external_name)

        # SubRecipe Ingredients
        elif sub_recipe:
            if not recipe_item.is_standalone():
                for _ingredient in sub_recipe.get('allIngredients'):
                    if _ingredient not in ingredients:
                        ingredients.append(_ingredient)

    return ingredients


# Returns the subRecipeId if any 'standalone' item exists within recipeItems, else returns None
# It is assumed that there is a max of ONE standalone item within the list of recipeItems, if any.
def get_standalone(recipe_items: List[Dict]) -> Optional[str]:
    for recipe_item in recipe_items:
        preparations = recipe_item.get('preparations', [])
        is_standalone = any(prep['id'] == PreparationEnum.STANDALONE.value for prep in preparations)

        if is_standalone:
            return recipe_item.get('subRecipeId')
    return None

def get_meal_slug(menu_item: Dict) -> Optional[str]:
    categories = menu_item['recipe'].get('categoryValues', [])
    for category in categories:
        if category.get('category', {}).get('id', '') == RecipeCategoryTagTypeEnum.BASE_MEAL_SLUG_TAG.value:
            return category['name']
    return None


# DATA TRANSFORMATION FUNCTIONS

def get_formatted_recipes_data(recipe_ids: List[str]) -> Optional[List[Dict]]:
    recipes_data = get_raw_recipes_data(recipe_ids=recipe_ids) or []
    formatted_recipes = []
    for recipe_data in recipes_data:
        formatted_recipe = FormattedRecipe(recipe_data=recipe_data)
        formatted_recipes.append(formatted_recipe.to_dict())
    return formatted_recipes


def get_formatted_menu_data(dates: List[str],
                            location_name: str="Vacaville",
                            menu_type: str="production"
                            ) -> Optional[List[Dict]]:
    menus = get_raw_menu_data(dates, location_name, menu_type)
    formatted_menus = []

    if not menus:
        return None

    for menu in menus:
        formatted_menu = {
            'name': menu.get('name'),
            'id': menu.get('id'),
            'date': menu.get('date'),
            'location': menu['location'].get('name'),
            'menuItems': []
        } # type: Dict

        categoryValues = menu['categoryValues']
        for categoryValue in categoryValues:
            if (categoryValue['category']['id'] ==
                    MenuCategoryEnum.MENU_TYPE.value):
                formatted_menu['categoryMenuType'] = categoryValue['name']

        menu_items = menu.get('menuItems', [])
        for menu_item in menu_items:
            recipe_items = menu_item.get('recipe', {}).get('recipeItems', [])

            categoryValues = menu_item['categoryValues']
            for categoryValue in categoryValues:
                if (categoryValue['category']['id'] ==
                        MenuItemCategoryEnum.PRODUCT_CODE.value):
                    itemCode = categoryValue['name']

            formatted_menu['menuItems'].append({
                'id': menu_item.get('id'),
                'itemCode': itemCode,
                'mealSlug': get_meal_slug(menu_item),
                'recipeId': menu_item.get('recipeId'),
                'standaloneRecipeId': get_standalone(recipe_items)
            })

        formatted_menus.append(formatted_menu)
    return formatted_menus
