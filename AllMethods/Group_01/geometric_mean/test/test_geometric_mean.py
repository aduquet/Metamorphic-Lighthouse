import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.geometric_mean import geometric_mean

class TestGeometricMean(unittest.TestCase):

    def test_geometric_mean_positive_numbers(self):
        self.assertAlmostEqual(geometric_mean([1, 2, 3, 4]), 2.213364, places=6)

    def test_geometric_mean_single_number(self):
        self.assertAlmostEqual(geometric_mean([5]), 5, places=6)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            geometric_mean([])

    def test_non_numeric_list(self):
        with self.assertRaises(ValueError):
            geometric_mean(["a", "b"])

    def test_non_positive_numeric_list(self):
        with self.assertRaises(ValueError):
            geometric_mean([-1, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            geometric_mean("string")

if __name__ == '__main__':
    unittest.main()

