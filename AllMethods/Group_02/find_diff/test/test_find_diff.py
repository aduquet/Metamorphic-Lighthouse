import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.find_diff import find_diff

class TestFindDiff(unittest.TestCase):
    def test_find_diff(self):
        self.assertEqual(find_diff([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            find_diff([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
