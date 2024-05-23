import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.find_median import find_median

class TestFindMedian(unittest.TestCase):
    
    def test_odd_number_of_elements(self):
        self.assertEqual(find_median([5, 3, 2, 4, 1]), 3)

    def test_even_number_of_elements(self):
        self.assertEqual(find_median([5, 3, 2, 4, 1, 6]), 3.5)

    def test_one_element(self):
        self.assertEqual(find_median([5]), 5)

    def test_two_elements(self):
        self.assertEqual(find_median([5, 2]), 3.5)

    def test_negative_numbers(self):
        self.assertEqual(find_median([-5, -3, -2, -4, -1]), -3)

if __name__ == '__main__':
    unittest.main()
