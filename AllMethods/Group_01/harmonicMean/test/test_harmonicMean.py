import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.harmonicMean import harmonicMean


class TestHarmonicMean(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(harmonicMean([1, 2, 3]), 1.6363636363636365)

    def test_single_number(self):
        self.assertEqual(harmonicMean([5]), 5.0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            harmonicMean([])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            harmonicMean([1, -2, 3])

    def test_zero_in_list(self):
        with self.assertRaises(ValueError):
            harmonicMean([0, 2, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            harmonicMean(123)

if __name__ == "__main__":
    unittest.main()

