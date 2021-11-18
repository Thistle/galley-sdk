from typing import Dict, Optional, List

from galley.queries import MenuCategoryEnum, get_raw_recipes_data, get_raw_menu_data
from galley.pagination import paginate_results

FOOD_PACKAGING = 'food pkg'
STANDALONE = 'standalone'


class RecipeItem:
    def __init__(self, preparations: List[Dict[str, str]], ingredient=None, quantity_unit_values=None):
        self.category_values = ingredient.get('categoryValues', []) if ingredient else []
        self.preparations = preparations
        self.quantity_unit_values = quantity_unit_values

    def is_standalone(self):
        return any(prep.get('name') == STANDALONE for prep in self.preparations)

    def is_packaging(self):
        return any(cat_val.get('name') == FOOD_PACKAGING for cat_val in self.category_values)

    def mass(self):
        if self.quantity_unit_values is None:
            raise Exception('Cannot calculate mass without unit values')
        return next(
            (value.get('value') for value in self.quantity_unit_values
             if value.get('unit', {'name': None}).get('name') == 'g'), 0
        )


class FormattedRecipe:
    mealContainer = None
    mealType = None
    proteinType = None

    def __init__(self, recipe_data):
        self.galleyId = recipe_data.get('id')
        self.externalName = recipe_data.get('externalName')
        self.notes = recipe_data.get('notes')
        self.description = recipe_data.get('description')
        self.nutrition = recipe_data.get('reconciledNutritionals', {})

        self.recipe_category_values = recipe_data.get('categoryValues', [])
        for recipe_category_value in self.recipe_category_values:
            category_name = recipe_category_value.get('category', {}).get('name')
            category_value = recipe_category_value.get('name')
            if category_name == 'protein type':
                self.proteinType = category_value
            elif category_name == 'meal type':
                self.mealType = category_value
            elif category_name == 'meal container':
                self.mealContainer = category_value

        self.recipe_items = recipe_data.get('recipeItems', [])
        self.ingredients = ingredients_from_recipe_items(recipe_items=self.recipe_items)
        self.recipe_tree_components = recipe_data.get('recipeTreeComponents', [])

    def total_weight(self):
        total_weight = 0
        for recipe_tree_component in self.recipe_tree_components:
            recipeItem = recipe_tree_component.get('recipeItem', {})
            ingredient = recipeItem.get('ingredient', {}) if recipeItem else None
            if recipeItem:
                recipe_item = RecipeItem(
                    preparations=recipeItem.get('preparations', []),
                    ingredient=ingredient if ingredient else None,
                    quantity_unit_values=recipe_tree_component.get('quantityUnitValues', [])
                )
                if recipe_item.is_standalone() or recipe_item.is_packaging():
                    continue
                total_weight += recipe_item.mass() if recipe_item.mass() else 0

        return total_weight

    def to_dict(self):
        return {
            'id': self.galleyId,
            'externalName': self.externalName,
            'notes': self.notes,
            'description': self.description,
            'nutrition': self.nutrition,
            'proteinType': self.proteinType,
            'mealContainer': self.mealContainer,
            'mealType': self.mealType,
            'ingredients': self.ingredients,
            'totalWeight': self.total_weight()
        }


def ingredients_from_recipe_items(recipe_items: List[Dict]) -> Optional[List]:
    ingredients: List[str] = []

    for recipe_item in recipe_items:
        ingredient = recipe_item.get('ingredient')
        sub_recipe = recipe_item.get('subRecipe')
        recipe_item = RecipeItem(
            ingredient=ingredient if ingredient else None,
            preparations=recipe_item.get('preparations', [])
        )

        # Top Level Ingredient
        if ingredient:
            external_name = ingredient.get('externalName')
            if not recipe_item.is_packaging() and external_name not in ingredients:
                ingredients.append(external_name)

        # SubRecipe Ingredients
        elif sub_recipe:
            if not recipe_item.is_standalone():
                for i in sub_recipe.get('allIngredients'):
                    if i not in ingredients:
                        ingredients.append(i)

    return ingredients


# Returns the subRecipeId if any 'standalone' item exists within recipeItems, else returns None
# It is assumed that there is a max of ONE standalone item within the list of recipeItems, if any.
def get_standalone(recipe_items):
    for recipe_item in recipe_items:
        preparations = recipe_item.get('preparations', [])
        is_standalone = any(prep['name'] == STANDALONE for prep in preparations)

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
        formatted_menu = ({
            'name': menu.get('name'),
            'id': menu.get('id'),
            'date': menu.get('date'),
            'location': menu['location'].get('name'),
            'menuItems': []
        }) # type: Dict

        categoryValues = menu['categoryValues']
        for categoryValue in categoryValues:
            if (categoryValue['category']['id'] ==
                    MenuCategoryEnum.MENU_TYPE.value):
                formatted_menu['categoryMenuType'] = categoryValue['name']

        menu_items = menu.get('menuItems', [])
        for menu_item in menu_items:
            recipe_items = menu_item.get('recipe', {}).get('recipeItems', [])

            formatted_menu['menuItems'].append({
                'itemCode': next((cv.get('name') for cv in menu_item['categoryValues']), None),
                'recipeId': menu_item.get('recipeId'),
                'standaloneRecipeId': get_standalone(recipe_items)
            })

        formatted_menus.append(formatted_menu)
    return formatted_menus
