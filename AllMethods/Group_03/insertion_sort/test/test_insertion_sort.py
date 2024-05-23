import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_sort_integer_list(self):
        self.assertEqual(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

    def test_sort_float_list(self):
        self.assertEqual(insertion_sort([3.5, 1.1, 2.2, 4.0]), sorted([3.5, 1.1, 2.2, 4.0]))

    def test_sort_mixed_numbers(self):
        self.assertEqual(insertion_sort([3, 1.5, 4, 2.5]), sorted([3, 1.5, 4, 2.5]))

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            insertion_sort(["a", "b", "c"])

    def test_invalid_input_mixed(self):
        with self.assertRaises(TypeError):
            insertion_sort([1, 2, "a"])

if __name__ == "__main__":
    unittest.main()
