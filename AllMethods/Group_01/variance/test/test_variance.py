import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.variance import variance

class TestVarianceCalc(unittest.TestCase):

    def test_variance_normal(self):
        self.assertAlmostEqual(variance([1, 2, 3, 4, 5]), 2.5)

    def test_variance_empty(self):
        with self.assertRaises(ValueError):
            variance([])

    def test_variance_invalid_input(self):
        with self.assertRaises(TypeError):
            variance("string")

    def test_variance_strings_in_list(self):
        with self.assertRaises(ValueError):
            variance(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()

