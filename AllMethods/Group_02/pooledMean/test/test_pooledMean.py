import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.pooledMean import pooledMean

class TestPooledMean(unittest.TestCase):
    def test_pooled_mean(self):
        self.assertAlmostEqual(pooledMean([1, 2, 3], [4, 5, 6, 7]), 4)

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            pooledMean([], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
