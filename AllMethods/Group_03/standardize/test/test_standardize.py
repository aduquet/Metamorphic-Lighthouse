import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.standardize import standardize

class TestStandardize(unittest.TestCase):

    def test_standardize_normal(self):
        input_data = [1, 2, 3, 4, 5]
        standardized = standardize(input_data)
        self.assertTrue(all(-2 <= x <= 2 for x in standardized))

    def test_standardize_empty(self):
        with self.assertRaises(ValueError):
            standardize([])

    def test_standardize_invalid_input(self):
        with self.assertRaises(TypeError):
            standardize("string")

    def test_standardize_strings_in_list(self):
        with self.assertRaises(ValueError):
            standardize(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
