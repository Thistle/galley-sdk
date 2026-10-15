import logging
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

from galley.enums import IngredientCategoryValueEnum, LabelIngredientEnum, RecipeCategoryTagTypeEnum
from galley.mutations import bulk_update_recipe_item_data, delete_recipe_item_preparation, upsert_preparation
from galley.queries import get_preparations, get_raw_sellable_recipes_recipe_items_data
from galley.scripts.custom_preparation_utils import generate_csv_from_dict_list


logger = logging.getLogger(__name__)


# Label template preparations tag each label ingredient usage on a sellable
# recipe with the label-workflow templates to print on that label's paper
# stock. Each preparation is named after its label-workflow template
# (lib/label_render_html/label_type/meal_labels.py).
AUTOLABEL_TOP_TEMPLATE = '275x4625-autolabel-top-label'
AUTOLABEL_BOTTOM_TEMPLATE = '275x3500-autolabel-bottom-label'
HORIZONTAL_MEAL_TEMPLATE = '8000x275-horizontal-meal-label'
HUMMUS_ONE_COLOR_TEMPLATE = '275x4625-hummus-one-color-label'
HUMMUS_TWO_COLOR_TEMPLATE = '275x4625-hummus-two-color-label'
MUFFIN_SMOOTHIE_TEMPLATE = '275x5541-muffin-smoothie-label'
SOUP_TEMPLATE = '5875x175-soup-label'
JAR_SALAD_TEMPLATE = '5875x175-jar-salad-label'

# Preparations with these names are label templates, whether or not they're
# mapped below, so a template that is no longer expected gets replaced.
LABEL_TEMPLATES = {
    AUTOLABEL_TOP_TEMPLATE,
    AUTOLABEL_BOTTOM_TEMPLATE,
    HORIZONTAL_MEAL_TEMPLATE,
    HUMMUS_ONE_COLOR_TEMPLATE,
    HUMMUS_TWO_COLOR_TEMPLATE,
    MUFFIN_SMOOTHIE_TEMPLATE,
    SOUP_TEMPLATE,
    JAR_SALAD_TEMPLATE,
}

# Meal container tag values that mean no container has been chosen
UNSET_MEAL_CONTAINERS = {'not set'}

BULK_UPDATE_BATCH_SIZE = 100

AUTOLABEL_CONTAINERS = ('ts20', 'ts24', 'ts32', 'ts48', 'jar32')
MUFFIN_SMOOTHIE_CONTAINERS = ('ts8', 'ts8ccr', 'ts12ccr', 'jar12clr', 'jar16')
HUMMUS_CONTAINERS = ('tssb1r', 'tssb3r')

# (meal container tag value, label ingredient id): label template preparation names
LABEL_TEMPLATE_PREPARATIONS: Dict[Tuple[str, str], Tuple[str, ...]] = {
    **{
        (container, LabelIngredientEnum.AUTOLABELER_TOP.value): (AUTOLABEL_TOP_TEMPLATE,)
        for container in AUTOLABEL_CONTAINERS
    },
    **{
        (container, LabelIngredientEnum.AUTOLABELER_BOTTOM.value): (AUTOLABEL_BOTTOM_TEMPLATE,)
        for container in AUTOLABEL_CONTAINERS
    },
    **{
        (container, LabelIngredientEnum.MUFFIN_AND_SMOOTHIE_CIRCLE.value): (MUFFIN_SMOOTHIE_TEMPLATE,)
        for container in MUFFIN_SMOOTHIE_CONTAINERS
    },
    ('jar12clr', LabelIngredientEnum.SOUPS.value): (SOUP_TEMPLATE,),
    # There's no one color hummus label ingredient, so both templates generate
    **{
        (container, LabelIngredientEnum.HUMMUS_RECTANGLE.value): (HUMMUS_ONE_COLOR_TEMPLATE, HUMMUS_TWO_COLOR_TEMPLATE)
        for container in HUMMUS_CONTAINERS
    },
}


def is_label_recipe_item(recipe_item: Dict) -> bool:
    ingredient = recipe_item.get('ingredient') or {}
    return any(
        cv.get('id') == IngredientCategoryValueEnum.LABEL.value
        for cv in ingredient.get('categoryValues') or []
    )


def get_meal_containers(recipe: Dict) -> List[str]:
    return [
        cv['name'] for cv in recipe.get('categoryValues') or []
        if (
            (cv.get('category') or {}).get('id') == RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value
            and cv.get('name') not in UNSET_MEAL_CONTAINERS
        )
    ]


def get_label_template_assignments(recipes: List[Dict]) -> List[Dict]:
    """
    Returns one row per label recipe item on the given sellable recipes with
    the label template preparations it should have and the changes needed to
    get there. A mapped label item ends up with exactly its expected
    templates: any other or duplicate template preparations on it are marked
    for deletion. Skipped items are reported but never changed, even if they
    already have a template preparation.
    """
    assignments = []

    for recipe in recipes:
        containers = get_meal_containers(recipe)

        for recipe_item in recipe.get('recipeItems') or []:
            if not is_label_recipe_item(recipe_item):
                continue

            ingredient = recipe_item['ingredient']
            template_preparations = [
                rip for rip in recipe_item.get('recipeItemPreparations') or []
                if (rip.get('preparation') or {}).get('name') in LABEL_TEMPLATES
            ]
            templates: Tuple[str, ...] = ()
            templates_to_add: List[str] = []
            delete: List[Dict] = []

            if not containers:
                action = 'skip: no meal container'
            elif len(containers) > 1:
                action = 'skip: multiple meal containers'
            elif not (templates := LABEL_TEMPLATE_PREPARATIONS.get((containers[0], ingredient['id']), ())):
                action = 'skip: no template mapped'
            else:
                keep: Dict[str, Dict] = {}
                for rip in template_preparations:
                    name = rip['preparation']['name']
                    if name in templates and name not in keep:
                        keep[name] = rip
                    else:
                        delete.append(rip)
                templates_to_add = [name for name in templates if name not in keep]
                action = 'replace' if delete else 'add' if templates_to_add else 'ok'

            assignments.append({
                'recipe_id': recipe.get('id'),
                'recipe_name': recipe.get('name'),
                'meal_container': '|'.join(containers),
                'recipe_item_id': recipe_item.get('id'),
                'label_ingredient_id': ingredient.get('id'),
                'label_ingredient_name': ingredient.get('name'),
                'current_templates': '|'.join(rip['preparation']['name'] for rip in template_preparations),
                'templates': '|'.join(templates),
                'action': action,
                'templates_to_add': '|'.join(templates_to_add),
                'recipe_item_preparation_ids_to_delete': ','.join(rip['id'] for rip in delete),
                'recipe_link': f'https://app.galleysolutions.com/recipes/{recipe.get("id")}',
            })
    return assignments


def get_label_template_assignments_from_galley() -> List[Dict]:
    recipes = get_raw_sellable_recipes_recipe_items_data()
    assignments = get_label_template_assignments(recipes)

    logger.warning(
        f"Found {len(assignments)} label recipe items on {len(recipes)} sellable recipes: "
        f"{dict(Counter(a['action'] for a in assignments))}"
    )
    return assignments


def create_label_template_preparations(dry_run: bool = True) -> Dict[str, str]:
    """
    Creates any label template preparations from LABEL_TEMPLATE_PREPARATIONS,
    plus the jar salad template, that don't exist in Galley yet. Returns
    template names mapped to their preparation ids (templates not yet created
    are omitted).
    """
    preparation_ids = {p['name']: p['id'] for p in get_preparations()}
    # Jar salads still use the pre-printed stock, but create their template for when they switch
    templates = sorted(
        {name for names in LABEL_TEMPLATE_PREPARATIONS.values() for name in names}
        | {JAR_SALAD_TEMPLATE}
    )
    missing = [name for name in templates if name not in preparation_ids]

    logger.warning(f"Creating {len(missing)} of {len(templates)} label template preparations: {missing}")

    if not dry_run:
        for name in missing:
            preparation_ids[name] = upsert_preparation(name)['id']
            logger.warning(f"Created label template preparation {name} ({preparation_ids[name]})")
    return {name: preparation_ids[name] for name in templates if name in preparation_ids}


def generate_csv_for_label_template_assignments(filename: str = 'label_template_assignments.csv') -> None:
    """
    Writes a csv of every label recipe item on a sellable recipe with its
    meal container, current and expected label templates, and the action
    assign_label_template_preparations would take.
    """
    generate_csv_from_dict_list(get_label_template_assignments_from_galley(), filename)


def assign_label_template_preparations(dry_run: bool = True) -> None:
    """
    Tags each label recipe item on a sellable recipe with the label template
    preparations for its recipe's meal container, replacing any other label
    template preparations on that item. Run create_label_template_preparations
    first so every template exists in Galley.
    """
    preparation_ids = {p['name']: p['id'] for p in get_preparations()}
    changes = [
        a for a in get_label_template_assignments_from_galley()
        if a['action'] in ('add', 'replace')
    ]

    delete_bin = [
        recipe_item_preparation_id
        for a in changes
        for recipe_item_preparation_id in a['recipe_item_preparation_ids_to_delete'].split(',')
        if recipe_item_preparation_id
    ]
    recipe_items_by_template: Dict[str, List[str]] = defaultdict(list)
    for a in changes:
        for template in a['templates_to_add'].split('|'):
            if template:
                recipe_items_by_template[template].append(a['recipe_item_id'])

    missing = sorted(template for template in recipe_items_by_template if template not in preparation_ids)
    if missing:
        message = (
            f"Label template preparations missing from Galley, run "
            f"create_label_template_preparations first: {missing}"
        )
        if not dry_run:
            raise ValueError(message)
        logger.warning(message)

    logger.warning(f"Deleting {len(delete_bin)} replaced label template recipe item preparations.")
    for template, recipe_item_ids in sorted(recipe_items_by_template.items()):
        logger.warning(f"Adding {template} ({preparation_ids.get(template)}) to {len(recipe_item_ids)} label recipe items.")

    if dry_run:
        return

    for recipe_item_preparation_id in delete_bin:
        try:
            delete_recipe_item_preparation(recipe_item_preparation_id=recipe_item_preparation_id)
        except Exception as e:
            logger.error(f"Failure to delete recipe item preparation {recipe_item_preparation_id}: {e}")

    for template, recipe_item_ids in sorted(recipe_items_by_template.items()):
        for i in range(0, len(recipe_item_ids), BULK_UPDATE_BATCH_SIZE):
            bulk_update_recipe_item_data({
                'ids': recipe_item_ids[i:i + BULK_UPDATE_BATCH_SIZE],
                'attrs': {'preparationIds': [preparation_ids[template]]},
            })
        logger.warning(f"Added {template} to {len(recipe_item_ids)} label recipe items.")
