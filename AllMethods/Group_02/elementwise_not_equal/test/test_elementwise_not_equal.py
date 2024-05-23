import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.elementwise_not_equal import elementwise_not_equal


class TestElementwiseNotEqual(unittest.TestCase):
    
    def test_equal_lists(self):
        self.assertEqual(elementwise_not_equal([1, 2, 3], [1, 2, 3]), [False, False, False])

    def test_different_lists(self):
        self.assertEqual(elementwise_not_equal([1, 2, 3], [4, 5, 6]), [True, True, True])

    def test_partially_different_lists(self):
        self.assertEqual(elementwise_not_equal([1, 2, 3], [1, 2, 4]), [False, False, True])

    def test_mismatched_length_lists(self):
        with self.assertRaises(ValueError):
            elementwise_not_equal([1, 2, 3], [1, 2])

    def test_empty_lists(self):
        self.assertEqual(elementwise_not_equal([], []), [])

if __name__ == '__main__':
    unittest.main()
