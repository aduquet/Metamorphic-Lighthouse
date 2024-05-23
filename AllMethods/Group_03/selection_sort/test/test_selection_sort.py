import unittest
import os
import sys

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element(self):
        self.assertEqual(selection_sort([1]), [1])

if __name__ == "__main__":
    unittest.main()
