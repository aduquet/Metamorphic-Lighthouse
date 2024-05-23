import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.ebeSubtract import ebeSubtract



class TestEbeSubtract(unittest.TestCase):

    def test_valid_subtraction(self):
        self.assertEqual(ebeSubtract([10, 20, 30], [1, 2, 3]), [9, 18, 27])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            ebeSubtract([1, 2, 3], [1, 2])

    def test_empty_lists(self):
        self.assertEqual(ebeSubtract([], []), [])

if __name__ == '__main__':
    unittest.main()
