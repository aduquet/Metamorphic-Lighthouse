import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.ebeAdd import ebeAdd

class TestEbeAdd(unittest.TestCase):
    def test_ebe_add(self):
        self.assertEqual(ebeAdd([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            ebeAdd("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            ebeAdd([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
