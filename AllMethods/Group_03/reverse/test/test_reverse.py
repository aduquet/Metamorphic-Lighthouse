import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.reverse import reverse

class TestReverse(unittest.TestCase):

    def test_reverse_list_of_integers(self):
        self.assertEqual(reverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_reverse_single_element(self):
        self.assertEqual(reverse([42]), [42])

    def test_reverse_list_of_strings(self):
        self.assertEqual(reverse(["a", "b", "c"]), ["c", "b", "a"])

    def test_empty_list(self):
        self.assertEqual(reverse([]), [])

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            reverse("string")

if __name__ == '__main__':
    unittest.main()
