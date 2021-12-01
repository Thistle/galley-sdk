from typing import Dict, Optional, List

from galley.enums import IngredientCategoryValueEnum, MenuCategoryEnum, MenuItemCategoryEnum, PreparationEnum, IngredientCategoryTagTypeEnum, RecipeCategoryTagTypeEnum
from galley.pagination import paginate_results
from galley.queries import get_raw_recipes_data, get_raw_menu_data

import logging
logger = logging.getLogger(__name__)

class RecipeItem:
    def __init__(self, preparations: List[Dict[str, str]], ingredient=None, quantity_unit_values=None):
        self.category_values = ingredient.get('categoryValues', []) if ingredient else []
        self.preparations = preparations
        self.quantity_unit_values = quantity_unit_values

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
        self.externalName = recipe_data.get('externalName')
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
        recipe_data = {
            'id': self.galleyId,
            'externalName': self.externalName,
            'notes': self.notes,
            'description': self.description,
            'nutrition': self.nutrition,
            'ingredients': ingredients_from_recipe_items(recipe_items=self.recipe_items),
            **self.formatted_recipe_tree_components_data
        }
        return {**recipe_data, **self.recipe_tags}


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
    standalone_subrecipes = []
    for recipe_tree_component in recipe_tree_components:
        recipe_item_dict = recipe_tree_component.get('recipeItem', {})
        if recipe_item_dict:
            recipe_item = RecipeItem(
                preparations=recipe_item_dict.get('preparations', []),
                ingredient=recipe_item_dict.get('ingredient', {}),
                quantity_unit_values=recipe_tree_component.get(
                    'quantityUnitValues', [])
            )

            if recipe_item.is_packaging():
                continue
            elif recipe_item.is_standalone():
                subrecipe_dict = recipe_item_dict.get('subRecipe', {})
                standalone_subrecipes.append(subrecipe_dict)
            else:
                total_weight += recipe_item.mass() if recipe_item.mass() else 0

    standalone_subrecipe = standalone_subrecipes[0] if\
        standalone_subrecipes else {}

    if len(standalone_subrecipes) > 1:
        logger.warning("More than one standalone subrecipe found for recipe"
                       f"tree component id {recipe_tree_component.get('id')}")

    return {
        'weight': round(total_weight, 2),
        'standaloneRecipeId': standalone_subrecipe.get('id'),
        'standaloneRecipeName': standalone_subrecipe.get('externalName'),
        'standaloneNutrition': standalone_subrecipe.get(
                                                    'reconciledNutritionals'),
        'standaloneIngredients': standalone_subrecipe.get('allIngredients'),
        'standaloneWeight': standalone_subrecipe.get('weight'),
        'standaloneWeightUnit': standalone_subrecipe.get('unit', {}).get('name')
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
            external_name = ingredient.get('externalName')
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


# DATA TRANSFORMATION FUNCTIONS

@paginate_results()
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
                'recipeId': menu_item.get('recipeId'),
                'standaloneRecipeId': get_standalone(recipe_items)
            })

        formatted_menus.append(formatted_menu)
    return formatted_menus
