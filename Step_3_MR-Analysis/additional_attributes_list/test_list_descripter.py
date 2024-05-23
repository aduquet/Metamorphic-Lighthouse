import unittest
from list_descripter import *

class TestListDescripter(unittest.TestCase):

    def test_get_length(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.get_length(), 4)

    def test_has_zero(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertTrue(descripter.has_zero())

    def test_cnt_positive_numbers(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.cnt_positive_numbers(), 2)

    def test_cnt_negative_numbers(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.cnt_negative_numbers(), 1)

    def test_get_minimum(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.get_minimum(), -4)

    def test_get_maximum(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.get_maximum(), 2)

    def test_get_sum(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.get_sum(), -1)

    def test_get_mean(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertAlmostEqual(descripter.get_mean(), -0.25, places=2)

    def test_get_median(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.get_median(), 0.5)

    def test_get_range(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.get_range(), 6)

    def test_has_duplicates(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertFalse(descripter.has_duplicates())

    def test_is_sorted(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertFalse(descripter.is_sorted())

    def test_count_distinct_values(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertEqual(descripter.count_distinct_values(), 4)

    def test_contains_even_numbers(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertTrue(descripter.contains_even_numbers())

    def test_contains_odd_numbers(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertTrue(descripter.contains_odd_numbers())

    def test_contains_integers(self):
        data_list = [1, 2, -4, 0]
        descripter = ListDescripter(data_list)
        self.assertTrue(descripter.contains_integers())

if __name__ == '__main__':
    unittest.main()
