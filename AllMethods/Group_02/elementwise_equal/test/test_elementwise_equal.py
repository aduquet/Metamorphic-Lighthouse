import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.elementwise_equal import elementwise_equal



class TestElementwiseEqual(unittest.TestCase):
    def test_elementwise_equal(self):
        self.assertEqual(elementwise_equal([1, 2, 3], [1, 2, 4]), [True, True, False])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            elementwise_equal([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
