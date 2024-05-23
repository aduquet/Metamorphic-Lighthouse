import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.find_min import find_min

class TestFindMinFunction(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_min([])

    def test_min_integer_list(self):
        self.assertEqual(find_min([4, 7, 2, 8, 5]), 2)

    def test_min_float_list(self):
        self.assertEqual(find_min([4.5, 7.1, 2.2, 8.9, 5.4]), 2.2)

    def test_min_mixed_list(self):
        self.assertEqual(find_min([4, 7.1, 2, 8.9, 5]), 2)

    def test_min_single_element_list(self):
        self.assertEqual(find_min([4]), 4)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            find_min(["a", "b", "c"])

    def test_invalid_input_mixed_list(self):
        with self.assertRaises(TypeError):
            find_min([4, "b", 2])

if __name__ == "__main__":
    unittest.main()
