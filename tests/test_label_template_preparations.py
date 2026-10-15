import logging
from galley.enums import IngredientCategoryValueEnum, LabelIngredientEnum, RecipeCategoryTagTypeEnum
from galley.mutations import build_upsert_preparation_mutation, upsert_preparation
from galley.queries import get_raw_sellable_recipes_recipe_items_data
from galley.scripts.label_template_preparations import (
    AUTOLABEL_BOTTOM_TEMPLATE,
    AUTOLABEL_TOP_TEMPLATE,
    BULK_UPDATE_BATCH_SIZE,
    HUMMUS_ONE_COLOR_TEMPLATE,
    HUMMUS_TWO_COLOR_TEMPLATE,
    JAR_SALAD_TEMPLATE,
    MUFFIN_SMOOTHIE_TEMPLATE,
    SOUP_TEMPLATE,
    apply_label_template_preparations,
    create_label_template_preparations,
    get_label_template_assignments,
)
from unittest import TestCase, mock


logger = logging.getLogger(__name__)


TOP = LabelIngredientEnum.AUTOLABELER_TOP.value
BOTTOM = LabelIngredientEnum.AUTOLABELER_BOTTOM.value
CIRCLE = LabelIngredientEnum.MUFFIN_AND_SMOOTHIE_CIRCLE.value
HUMMUS = LabelIngredientEnum.HUMMUS_RECTANGLE.value
JAR_SALAD = 'jar-salad-label'

PREPARATION_IDS = {
    AUTOLABEL_TOP_TEMPLATE: 'prep-top',
    AUTOLABEL_BOTTOM_TEMPLATE: 'prep-bottom',
    HUMMUS_ONE_COLOR_TEMPLATE: 'prep-hummus-one',
    HUMMUS_TWO_COLOR_TEMPLATE: 'prep-hummus-two',
    MUFFIN_SMOOTHIE_TEMPLATE: 'prep-muffin',
    SOUP_TEMPLATE: 'prep-soup',
    'standalone': 'prep-standalone',
}


def mock_container(name):
    return {
        'id': f'cv-{name}',
        'name': name,
        'category': {'id': RecipeCategoryTagTypeEnum.MEAL_CONTAINER_TAG.value, 'name': 'meal container'},
    }


def mock_recipe_item_preparation(id, preparation_name):
    return {'id': id, 'preparation': {'id': PREPARATION_IDS[preparation_name], 'name': preparation_name}}


def mock_label_item(id, ingredient_id, preparations=()):
    return {
        'id': id,
        'ingredient': {
            'id': ingredient_id,
            'name': f'label {ingredient_id}',
            'externalName': None,
            'categoryValues': [{'id': IngredientCategoryValueEnum.LABEL.value, 'name': 'label'}],
        },
        'recipeItemPreparations': list(preparations),
    }


def mock_sellable(id, containers, recipe_items):
    return {
        'id': id,
        'name': f'recipe {id}',
        'categoryValues': [mock_container(c) for c in containers],
        'recipeItems': recipe_items,
    }


NON_LABEL_ITEM = {
    'id': 'ri-food',
    'ingredient': {'id': 'food', 'name': 'kale', 'externalName': None, 'categoryValues': []},
    'recipeItemPreparations': [],
}


class TestGetLabelTemplateAssignments(TestCase):
    def assign(self, recipe):
        return {a['recipe_item_id']: a for a in get_label_template_assignments([recipe])}

    def test_adds_template_for_container_and_label(self):
        assignments = self.assign(mock_sellable('r1', ['ts48'], [
            NON_LABEL_ITEM,
            mock_label_item('ri-top', TOP),
            mock_label_item('ri-bottom', BOTTOM),
        ]))
        self.assertEqual(set(assignments), {'ri-top', 'ri-bottom'})
        self.assertEqual(assignments['ri-top']['action'], 'add')
        self.assertEqual(assignments['ri-top']['templates'], AUTOLABEL_TOP_TEMPLATE)
        self.assertEqual(assignments['ri-top']['templates_to_add'], AUTOLABEL_TOP_TEMPLATE)
        self.assertEqual(assignments['ri-bottom']['templates_to_add'], AUTOLABEL_BOTTOM_TEMPLATE)

    def test_adds_both_hummus_templates(self):
        for container in ('tssb1r', 'tssb3r'):
            assignments = self.assign(mock_sellable('r1', [container], [mock_label_item('ri-hummus', HUMMUS)]))
            self.assertEqual(assignments['ri-hummus']['action'], 'add')
            self.assertEqual(
                assignments['ri-hummus']['templates_to_add'],
                f'{HUMMUS_ONE_COLOR_TEMPLATE}|{HUMMUS_TWO_COLOR_TEMPLATE}'
            )

    def test_adds_missing_hummus_template(self):
        assignments = self.assign(mock_sellable('r1', ['tssb3r'], [
            mock_label_item('ri-hummus', HUMMUS, [mock_recipe_item_preparation('rip-1', HUMMUS_TWO_COLOR_TEMPLATE)]),
        ]))
        self.assertEqual(assignments['ri-hummus']['action'], 'add')
        self.assertEqual(assignments['ri-hummus']['templates_to_add'], HUMMUS_ONE_COLOR_TEMPLATE)
        self.assertEqual(assignments['ri-hummus']['recipe_item_preparation_ids_to_delete'], '')

    def test_ok_when_templates_already_applied(self):
        assignments = self.assign(mock_sellable('r1', ['tssb3r'], [
            mock_label_item('ri-hummus', HUMMUS, [
                mock_recipe_item_preparation('rip-1', HUMMUS_TWO_COLOR_TEMPLATE),
                mock_recipe_item_preparation('rip-2', HUMMUS_ONE_COLOR_TEMPLATE),
            ]),
        ]))
        self.assertEqual(assignments['ri-hummus']['action'], 'ok')
        self.assertEqual(assignments['ri-hummus']['templates_to_add'], '')
        self.assertEqual(assignments['ri-hummus']['recipe_item_preparation_ids_to_delete'], '')

    def test_replaces_other_template(self):
        assignments = self.assign(mock_sellable('r1', ['ts48'], [
            mock_label_item('ri-top', TOP, [
                mock_recipe_item_preparation('rip-standalone', 'standalone'),
                mock_recipe_item_preparation('rip-stale', AUTOLABEL_BOTTOM_TEMPLATE),
            ]),
        ]))
        self.assertEqual(assignments['ri-top']['action'], 'replace')
        self.assertEqual(assignments['ri-top']['current_templates'], AUTOLABEL_BOTTOM_TEMPLATE)
        self.assertEqual(assignments['ri-top']['templates_to_add'], AUTOLABEL_TOP_TEMPLATE)
        self.assertEqual(assignments['ri-top']['recipe_item_preparation_ids_to_delete'], 'rip-stale')

    def test_replace_keeps_one_of_each_expected_template(self):
        assignments = self.assign(mock_sellable('r1', ['ts48'], [
            mock_label_item('ri-top', TOP, [
                mock_recipe_item_preparation('rip-keep', AUTOLABEL_TOP_TEMPLATE),
                mock_recipe_item_preparation('rip-duplicate', AUTOLABEL_TOP_TEMPLATE),
                mock_recipe_item_preparation('rip-stale', SOUP_TEMPLATE),
            ]),
        ]))
        self.assertEqual(assignments['ri-top']['action'], 'replace')
        self.assertEqual(assignments['ri-top']['templates_to_add'], '')
        self.assertEqual(assignments['ri-top']['recipe_item_preparation_ids_to_delete'], 'rip-duplicate,rip-stale')

    def test_skips_without_meal_container(self):
        for containers in ([], ['not set']):
            assignments = self.assign(mock_sellable('r1', containers, [
                mock_label_item('ri-top', TOP, [mock_recipe_item_preparation('rip-stale', SOUP_TEMPLATE)]),
            ]))
            self.assertEqual(assignments['ri-top']['action'], 'skip: no meal container')
            self.assertEqual(assignments['ri-top']['templates_to_add'], '')
            self.assertEqual(assignments['ri-top']['recipe_item_preparation_ids_to_delete'], '')

    def test_skips_multiple_meal_containers(self):
        assignments = self.assign(mock_sellable('r1', ['ts48', 'ts32'], [mock_label_item('ri-top', TOP)]))
        self.assertEqual(assignments['ri-top']['action'], 'skip: multiple meal containers')
        self.assertEqual(assignments['ri-top']['meal_container'], 'ts48|ts32')

    def test_skips_unmapped_container_and_label(self):
        for container, label in (('ts24', CIRCLE), ('jar27', JAR_SALAD), ('tssb3r', TOP), ('tssb3r', BOTTOM)):
            assignments = self.assign(mock_sellable('r1', [container], [mock_label_item('ri-label', label)]))
            self.assertEqual(assignments['ri-label']['action'], 'skip: no template mapped')
            self.assertEqual(assignments['ri-label']['templates'], '')


@mock.patch('galley.scripts.label_template_preparations.get_preparations')
@mock.patch('galley.scripts.label_template_preparations.upsert_preparation')
class TestCreateLabelTemplatePreparations(TestCase):
    def test_dry_run_creates_nothing(self, mock_upsert, mock_get_preparations):
        mock_get_preparations.return_value = [{'id': 'prep-top', 'name': AUTOLABEL_TOP_TEMPLATE}]
        result = create_label_template_preparations()
        mock_upsert.assert_not_called()
        self.assertEqual(result, {AUTOLABEL_TOP_TEMPLATE: 'prep-top'})

    def test_creates_only_missing_templates(self, mock_upsert, mock_get_preparations):
        mock_get_preparations.return_value = [{'id': 'prep-top', 'name': AUTOLABEL_TOP_TEMPLATE}]
        mock_upsert.side_effect = lambda name: {'id': f'new-{name}', 'name': name}
        result = create_label_template_preparations(dry_run=False)
        self.assertEqual(sorted(c.args[0] for c in mock_upsert.call_args_list), sorted([
            AUTOLABEL_BOTTOM_TEMPLATE,
            HUMMUS_ONE_COLOR_TEMPLATE,
            HUMMUS_TWO_COLOR_TEMPLATE,
            JAR_SALAD_TEMPLATE,
            MUFFIN_SMOOTHIE_TEMPLATE,
            SOUP_TEMPLATE,
        ]))
        self.assertEqual(result[AUTOLABEL_TOP_TEMPLATE], 'prep-top')
        self.assertEqual(result[SOUP_TEMPLATE], f'new-{SOUP_TEMPLATE}')
        self.assertEqual(result[JAR_SALAD_TEMPLATE], f'new-{JAR_SALAD_TEMPLATE}')


@mock.patch('galley.scripts.label_template_preparations.bulk_update_recipe_item_data')
@mock.patch('galley.scripts.label_template_preparations.delete_recipe_item_preparation')
@mock.patch('galley.scripts.label_template_preparations.get_raw_sellable_recipes_recipe_items_data')
@mock.patch('galley.scripts.label_template_preparations.get_preparations')
class TestApplyLabelTemplatePreparations(TestCase):
    def setUp(self) -> None:
        self.preparations = [{'id': id, 'name': name} for name, id in PREPARATION_IDS.items()]
        self.recipes = [
            mock_sellable('r1', ['ts48'], [
                mock_label_item('ri-1-top', TOP, [mock_recipe_item_preparation('rip-stale', AUTOLABEL_BOTTOM_TEMPLATE)]),
                mock_label_item('ri-1-bottom', BOTTOM),
            ]),
            mock_sellable('r2', ['ts48'], [
                mock_label_item('ri-2-top', TOP, [mock_recipe_item_preparation('rip-ok', AUTOLABEL_TOP_TEMPLATE)]),
            ]),
            mock_sellable('r3', ['tssb3r'], [mock_label_item('ri-3-hummus', HUMMUS)]),
        ]

    def test_dry_run_makes_no_changes(self, mock_get_preparations, mock_get_recipes, mock_delete, mock_bulk_update):
        mock_get_preparations.return_value = self.preparations
        mock_get_recipes.return_value = self.recipes
        apply_label_template_preparations()
        mock_delete.assert_not_called()
        mock_bulk_update.assert_not_called()

    def test_replaces_and_adds_templates(self, mock_get_preparations, mock_get_recipes, mock_delete, mock_bulk_update):
        mock_get_preparations.return_value = self.preparations
        mock_get_recipes.return_value = self.recipes
        apply_label_template_preparations(dry_run=False)
        mock_delete.assert_called_once_with(recipe_item_preparation_id='rip-stale')
        self.assertEqual(
            sorted((c.args[0]['attrs']['preparationIds'][0], c.args[0]['ids']) for c in mock_bulk_update.call_args_list),
            [
                ('prep-bottom', ['ri-1-bottom']),
                ('prep-hummus-one', ['ri-3-hummus']),
                ('prep-hummus-two', ['ri-3-hummus']),
                ('prep-top', ['ri-1-top']),
            ]
        )

    def test_batches_bulk_updates(self, mock_get_preparations, mock_get_recipes, mock_delete, mock_bulk_update):
        mock_get_preparations.return_value = self.preparations
        mock_get_recipes.return_value = [
            mock_sellable(f'r{i}', ['ts48'], [mock_label_item(f'ri-{i}', TOP)])
            for i in range(BULK_UPDATE_BATCH_SIZE + 1)
        ]
        apply_label_template_preparations(dry_run=False)
        self.assertEqual([len(c.args[0]['ids']) for c in mock_bulk_update.call_args_list], [BULK_UPDATE_BATCH_SIZE, 1])

    def test_raises_when_template_missing(self, mock_get_preparations, mock_get_recipes, mock_delete, mock_bulk_update):
        mock_get_preparations.return_value = []
        mock_get_recipes.return_value = self.recipes
        apply_label_template_preparations()
        with self.assertRaises(ValueError):
            apply_label_template_preparations(dry_run=False)
        mock_delete.assert_not_called()
        mock_bulk_update.assert_not_called()


class TestUpsertPreparation(TestCase):
    def test_upsert_preparation_mutation(self):
        expected_str = '''mutation {
            upsertPreparation(input: {name: "275x4625-autolabel-top-label"}) {
            error {
            message
            }
            preparation {
            id
            name
            }
            }
            }'''.replace(' '*12, '')
        mutation_str = bytes(build_upsert_preparation_mutation('275x4625-autolabel-top-label')).decode('utf-8')
        self.assertEqual(mutation_str, expected_str)

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_returns_preparation(self, mock_mr):
        mock_mr.return_value = {'data': {'upsertPreparation': {'error': None, 'preparation': {'id': 'p1', 'name': '275x4625-autolabel-top-label'}}}}
        self.assertEqual(upsert_preparation('275x4625-autolabel-top-label'), {'id': 'p1', 'name': '275x4625-autolabel-top-label'})

    @mock.patch('galley.mutations.make_request_to_galley')
    def test_raises_on_payload_error(self, mock_mr):
        mock_mr.return_value = {'data': {'upsertPreparation': {'error': {'message': 'nope'}, 'preparation': None}}}
        with self.assertRaises(ValueError):
            upsert_preparation('275x4625-autolabel-top-label')


class TestGetRawSellableRecipesRecipeItemsData(TestCase):
    @mock.patch('galley.queries.make_request_to_galley')
    def test_pages_from_after_inclusive_end_index_and_dedupes(self, mock_mr):
        def page(ids, start_index, end_index, has_next_page):
            return {'data': {'viewer': {'recipeConnection': {
                'totalCount': 3,
                'pageInfo': {'startIndex': start_index, 'endIndex': end_index, 'hasNextPage': has_next_page},
                'edges': [{'node': {'id': id}} for id in ids],
            }}}}

        mock_mr.side_effect = [page(['1', '2'], 0, 1, True), page(['2', '3'], 2, 3, False)]
        result = get_raw_sellable_recipes_recipe_items_data()
        self.assertEqual([r['id'] for r in result], ['1', '2', '3'])
        second_query = bytes(mock_mr.call_args_list[1].kwargs['op']).decode('utf-8')
        self.assertIn('startIndex: 2', second_query)
        self.assertIn('isDish: true', second_query)
