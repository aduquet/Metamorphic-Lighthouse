import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.find_magnitude import find_magnitude

class TestFindMagnitude(unittest.TestCase):

    def test_valid_input(self):
        self.assertAlmostEqual(find_magnitude([3, 4]), 5, places=4)

    def test_zero_vector(self):
        self.assertEqual(find_magnitude([0, 0]), 0)

    def test_negative_elements(self):
        self.assertAlmostEqual(find_magnitude([-3, 4]), 5, places=4)

    def test_single_element(self):
        self.assertAlmostEqual(find_magnitude([5]), 5, places=4)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_magnitude([])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_magnitude("abc")

if __name__ == "__main__":
    unittest.main()

