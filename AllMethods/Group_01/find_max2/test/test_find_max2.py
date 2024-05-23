import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.find_max2 import find_max2

class TestMaxConsecutiveSum(unittest.TestCase):
    
    def test_list_too_small(self):
        with self.assertRaises(ValueError):
            find_max2([5])

    def test_all_positive(self):
        self.assertEqual(find_max2([1, 3, 5, 7, 9]), 16)  # 7 + 9 = 16

    def test_all_negative(self):
        self.assertEqual(find_max2([-1, -3, -5, -7, -9]), -4)  # -1 + -3 = -4

    def test_mixed_positive_negative(self):
        self.assertEqual(find_max2([-3, 1, 5, -7, 9, 2]), 11)  # 9 + 2 = 11

    def test_with_zero(self):
        self.assertEqual(find_max2([-3, 0, 5, 7, 9, 2]), 16)  # 7 + 9 = 16

if __name__ == '__main__':
    unittest.main()
