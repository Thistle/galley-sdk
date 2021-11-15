from unittest import mock, TestCase

from galley.pagination import paginate_results


class TestPaginateResults(TestCase):
    def setUp(self):
        self.mock = mock.MagicMock()

    def test_called_5_for_100(self):
        paginate_results(self.mock)(list(range(100)))
        self.assertEqual(5, self.mock.call_count)

    def test_called_11_for_100_when_page_size_10(self):
        paginate_results(self.mock, page_size=10)(list(range(100)))
        self.assertEqual(11, self.mock.call_count)

    def test_called_1_for_empty_list(self):
        paginate_results(self.mock, page_size=10)([])
        self.assertEqual(1, self.mock.call_count)

    def test_nocall_noexception_for_bad_arg(self):
        paginate_results(self.mock, page_size=10)(5)
        self.assertEqual(0, self.mock.call_count)
