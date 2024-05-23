import unittest
import os
import sys

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.absoluteDifferences import absoluteDifferences

class TestCalculateAbsoluteDifferences(unittest.TestCase):
    def test_mixed_values(self):
        self.assertEqual(absoluteDifferences([-3, 4, -1, 0]), [3, 4, 1, 0])

    def test_empty_list(self):
        self.assertIsNone(absoluteDifferences([]))

    def test_none_input(self):
        self.assertIsNone(absoluteDifferences(None))

    def test_all_positive_values(self):
        self.assertEqual(absoluteDifferences([5, 7, 9]), [5, 7, 9])

if __name__ == "__main__":
    unittest.main()
