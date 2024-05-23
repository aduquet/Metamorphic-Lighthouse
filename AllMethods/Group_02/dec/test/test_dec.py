import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.dec import dec


class TestDecFunction(unittest.TestCase):

    def test_elementwise_subtraction(self):
        self.assertEqual(dec([10, 20, 30], [1, 2, 3]), [9, 18, 27])

    def test_mismatched_array_length(self):
        with self.assertRaises(ValueError):
            dec([1, 2, 3], [1, 2])

    def test_empty_arrays(self):
        self.assertEqual(dec([], []), [])

if __name__ == '__main__':
    unittest.main()
