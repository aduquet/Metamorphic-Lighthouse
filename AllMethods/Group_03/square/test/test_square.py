import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.square import square

class TestSquareElements(unittest.TestCase):

    def test_square_of_numbers(self):
        self.assertEqual(square([1, 2, 3, 4]), [1, 4, 9, 16])

    def test_square_of_negative_numbers(self):
        self.assertEqual(square([-1, -2, -3]), [1, 4, 9])

    def test_square_of_empty_list(self):
        self.assertEqual(square([]), [])

    def test_invalid_input_string_list(self):
        with self.assertRaises(ValueError):
            square(["a", "b", "c"])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            square("string")

if __name__ == '__main__':
    unittest.main()
