import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.calculateDifferences import calculateDifferences


# Test suite for the calculateDifferences function
class TestCalculateDifferences(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(calculateDifferences([1, 2, 3], [4, 5, 6]), [3, 3, 3])

    def test_empty_lists(self):
        self.assertEqual(calculateDifferences([], []), [])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            calculateDifferences("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            calculateDifferences([1, 2], [1, 2, 3])

# Running the test suite
if __name__ == "__main__":
    unittest.main()

