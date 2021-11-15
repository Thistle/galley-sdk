from unittest import mock, TestCase

from galley.pagination import paginate_results


class TestPaginateResults(TestCase):
    def setUp(self):
        self.mock = mock.MagicMock()

    def test_called_4_for_100_by_default(self):
        paginate_results()(self.mock)(list(range(100)))
        self.assertEqual(4, self.mock.call_count)

    def test_called_5_for_105_by_default(self):
        paginate_results()(self.mock)(list(range(105)))
        self.assertEqual(5, self.mock.call_count)

    def test_called_10_for_100_when_page_size_10(self):
        paginate_results(page_size=10)(self.mock)(list(range(100)))
        self.assertEqual(10, self.mock.call_count)

    def test_called_11_for_105_when_page_size_10(self):
        paginate_results(page_size=10)(self.mock)(list(range(105)))
        self.assertEqual(11, self.mock.call_count)

    def test_called_0_for_empty_list(self):
        paginate_results()(self.mock)([])
        self.assertEqual(0, self.mock.call_count)

    def test_nocall_noexception_for_bad_arg(self):
        paginate_results()((self.mock))(5)
        self.assertEqual(0, self.mock.call_count)

    def test_nocall_noexception_for_no_arg(self):
        paginate_results()((self.mock))()
        self.assertEqual(0, self.mock.call_count)
