import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.ebeMultiply import ebeMultiply

class TestEbeMultiply(unittest.TestCase):
    def test_ebe_multiply(self):
        self.assertEqual(ebeMultiply([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            ebeMultiply("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            ebeMultiply([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
