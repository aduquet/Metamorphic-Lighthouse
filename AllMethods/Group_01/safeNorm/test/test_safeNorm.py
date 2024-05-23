import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.safeNorm import safeNorm

class TestSafeNorm(unittest.TestCase):

    def test_norm_of_numbers(self):
        self.assertAlmostEqual(safeNorm([1, 2, 3, 4, 5]), 7.416198487095663)

    def test_norm_single_element(self):
        self.assertAlmostEqual(safeNorm([42]), 42)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            safeNorm([])

    def test_invalid_input_string_list(self):
        with self.assertRaises(ValueError):
            safeNorm(["a", "b"])

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            safeNorm("string")

if __name__ == '__main__':
    unittest.main()
