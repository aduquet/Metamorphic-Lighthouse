import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.find_max import find_max

class TestFindMaxFunction(unittest.TestCase):
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_max([])

    def test_single_element(self):
        self.assertEqual(find_max([5]), 5)

    def test_all_positive(self):
        self.assertEqual(find_max([1, 3, 5, 7, 9]), 9)

    def test_all_negative(self):
        self.assertEqual(find_max([-1, -3, -5, -7, -9]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(find_max([-3, 1, 5, -7, 9]), 9)

    def test_with_zero(self):
        self.assertEqual(find_max([-3, 0, 5, 7, 9]), 9)

if __name__ == '__main__':
    unittest.main()
