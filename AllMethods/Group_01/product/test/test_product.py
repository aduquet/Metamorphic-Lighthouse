import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.product import product

class TestProduct(unittest.TestCase):

    def test_product_of_integers(self):
        self.assertEqual(product([1, 2, 3, 4, 5]), 120)

    def test_product_with_zero(self):
        self.assertEqual(product([1, 2, 0, 4, 5]), 0)

    def test_product_of_single_element(self):
        self.assertEqual(product([42]), 42)

    def test_product_of_floats(self):
        self.assertEqual(product([1.2, 2.3, 3.4, 0.5]), 4.656)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            product([])

    def test_invalid_data_string(self):
        with self.assertRaises(TypeError):
            product(['a', 'b', 'c'])

    def test_invalid_data_mixed(self):
        with self.assertRaises(TypeError):
            product([1, 2, 'a', 3])

if __name__ == '__main__':
    unittest.main()
