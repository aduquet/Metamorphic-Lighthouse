import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.add import add
import unittest

class TestAddFunction(unittest.TestCase):

    def test_add_same_length_arrays(self):
        self.assertEqual(add([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_add_empty_arrays(self):
        self.assertEqual(add([], []), [])

    def test_add_different_length_arrays(self):
        with self.assertRaises(ValueError):
            add([1, 2, 3], [4, 5])

    def test_add_arrays_with_negative_numbers(self):
        self.assertEqual(add([-1, -2, -3], [1, 2, 3]), [0, 0, 0])

# Running the tests
unittest.main(argv=[''], exit=False)

