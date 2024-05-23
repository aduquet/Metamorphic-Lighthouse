import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.add_values import add_values

class TestAddValues(unittest.TestCase):

    def test_sum_of_integers(self):
        self.assertEqual(add_values([1, 2, 3, 4, 5]), 15)

    def test_sum_of_floats(self):
        self.assertAlmostEqual(add_values([1.1, 2.2, 3.3]), 6.6)

    def test_sum_of_mixed_numbers(self):
        self.assertAlmostEqual(add_values([1, 2.2, 3]), 6.2)

    def test_sum_of_empty_list(self):
        self.assertEqual(add_values([]), 0)

    def test_sum_of_negative_numbers(self):
        self.assertEqual(add_values([-1, -2, -3]), -6)

    def test_invalid_data_string(self):
        with self.assertRaises(TypeError):
            add_values(['a', 'b', 'c'])

    def test_invalid_data_mixed(self):
        with self.assertRaises(TypeError):
            add_values([1, 2, 'a'])

if __name__ == '__main__':
    unittest.main()
