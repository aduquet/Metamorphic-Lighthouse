import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.ebeDivide import ebeDivide

class TestEbeDivide(unittest.TestCase):
    def test_ebe_divide(self):
        self.assertEqual(ebeDivide([10, 20, 30], [2, 4, 5]), [5, 5, 6])

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            ebeDivide([1, 2, 3], [1, 0, 1])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            ebeDivide("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            ebeDivide([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
