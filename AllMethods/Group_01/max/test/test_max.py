import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.max import max

class TestFindMax(unittest.TestCase):

    def test_max_of_integers(self):
        self.assertEqual(max([1, 2, 3, 4, 5]), 5)

    def test_max_with_negative_numbers(self):
        self.assertEqual(max([-5, -4, -3, -2, -1]), -1)

    def test_max_of_single_element(self):
        self.assertEqual(max([42]), 42)

    def test_max_of_floats(self):
        self.assertEqual(max([1.2, 2.3, 3.4, 4.5]), 4.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max([])

    def test_invalid_data_string(self):
        with self.assertRaises(TypeError):
            max(['a', 'b', 'c'])

    def test_invalid_data_mixed(self):
        with self.assertRaises(TypeError):
            max([1, 2, 'a', 3])

if __name__ == '__main__':
    unittest.main()
