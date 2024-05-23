import unittest
from src.min import min

class TestFindMin(unittest.TestCase):

    def test_min_of_integers(self):
        self.assertEqual(min([1, 2, 3, 4, 5]), 1)

    def test_min_with_negative_numbers(self):
        self.assertEqual(min([-5, -4, -3, -2, -1]), -5)

    def test_min_of_single_element(self):
        self.assertEqual(min([42]), 42)

    def test_min_of_floats(self):
        self.assertEqual(min([1.2, 2.3, 3.4, 0.5]), 0.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            min([])

    def test_invalid_data_string(self):
        with self.assertRaises(TypeError):
            min(['a', 'b', 'c'])

    def test_invalid_data_mixed(self):
        with self.assertRaises(TypeError):
            min([1, 2, 'a', 3])

if __name__ == '__main__':
    unittest.main()
