import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.sum import sum


class TestSum(unittest.TestCase):

    def test_sum_normal(self):
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)

    def test_sum_empty(self):
        self.assertEqual(sum([]), 0)

    def test_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            sum("string")

    def test_sum_strings_in_list(self):
        with self.assertRaises(ValueError):
            sum(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
