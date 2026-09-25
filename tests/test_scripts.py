import logging
from galley.scripts.bulk_add_preparation_to_ingredient_usages import (
    bulk_add_plating_preparation_to_send_to_plate_ingredient_usages
)
from unittest import TestCase, mock


logger = logging.getLogger(__name__)


MODULE = 'galley.scripts.bulk_add_preparation_to_ingredient_usages'


class TestBulkAddPlatingPreparation(TestCase):
    def setUp(self) -> None:
        search = mock.patch(f'{MODULE}.get_ingredient_ids_by_search_term')
        by_name = mock.patch(f'{MODULE}.get_ingredient_ids_by_name')
        bulk_add = mock.patch(f'{MODULE}.bulk_add_preparation_to_ingredient_recipe_items')

        self.mock_search = search.start()
        self.mock_by_name = by_name.start()
        self.mock_bulk_add = bulk_add.start()

        self.addCleanup(search.stop)
        self.addCleanup(by_name.stop)
        self.addCleanup(bulk_add.stop)

        self.mock_search.return_value = ['ingredient-1', 'ingredient-2']
        self.mock_by_name.return_value = ['ingredient-1']

    def ingredient_ids_of_last_call(self):
        return sorted(self.mock_bulk_add.call_args.kwargs['ingredient_ids'])

    def test_exclusions_do_not_carry_over_between_runs(self):
        bulk_add_plating_preparation_to_send_to_plate_ingredient_usages(
            exclude_ingredient_names=['Diced Onion']
        )
        self.assertEqual(self.ingredient_ids_of_last_call(), ['ingredient-2'])

        self.mock_by_name.return_value = []
        bulk_add_plating_preparation_to_send_to_plate_ingredient_usages()
        self.assertEqual(
            self.ingredient_ids_of_last_call(),
            ['ingredient-1', 'ingredient-2']
        )

    def test_caller_supplied_exclusion_list_is_not_mutated(self):
        exclude_ingredient_ids = ['ingredient-2']

        bulk_add_plating_preparation_to_send_to_plate_ingredient_usages(
            exclude_ingredient_ids=exclude_ingredient_ids,
            exclude_ingredient_names=['Diced Onion'],
        )

        self.assertEqual(self.ingredient_ids_of_last_call(), [])
        self.assertEqual(exclude_ingredient_ids, ['ingredient-2'])
