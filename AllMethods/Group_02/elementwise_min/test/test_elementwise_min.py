import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.elementwise_min import elementwise_min


class TestElementwiseMin(unittest.TestCase):
    def test_elementwise_min(self):
        self.assertEqual(elementwise_min([1, 4, 3], [2, 2, 2]), [1, 2, 2])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            elementwise_min([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
