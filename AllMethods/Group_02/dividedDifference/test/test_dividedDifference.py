import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.dividedDifference import dividedDifference


class TestdividedDifference(unittest.TestCase):
    # def test_divided_difference(self):
    #     x = [1, 2, 3, 4]
    #     y = [1, 2, 4, 8]
    #     self.assertEqual(dividedDifference(x, y), some_expected_output)  # Replace with expected output

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            dividedDifference("not a list", [1, 2, 3, 4])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            dividedDifference([1, 2, 3], [1, 2])

if __name__ == "__main__":
    unittest.main()
