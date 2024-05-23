import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.skew import skew

class TestSkewness(unittest.TestCase):

    def test_skewness_of_numbers(self):
        self.assertAlmostEqual(skew([1, 2, 3, 4, 5]), 0.0)

    def test_two_elements(self):
        with self.assertRaises(ValueError):
            skew([1, 2])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            skew([])

    def test_invalid_input_string_list(self):
        with self.assertRaises(ValueError):
            skew(["a", "b", "c"])

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            skew("string")

if __name__ == '__main__':
    unittest.main()
