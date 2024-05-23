import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.durbinWatson import durbinWatson

class TestDurbinWatsonFunction(unittest.TestCase):

    def test_empty_data(self):
        with self.assertRaises(IndexError):
            durbinWatson([])

    def test_single_element_data(self):
        self.assertEqual(durbinWatson([5]), 0)

    def test_positive_autocorrelation(self):
        self.assertTrue(durbinWatson([1, 2, 3, 4, 5]) < 2)

    def test_no_autocorrelation(self):
        self.assertAlmostEqual(durbinWatson([5, 1, 3, 7, 2]), 2, delta=0.1)

    def test_negative_autocorrelation(self):
        self.assertTrue(durbinWatson([5, 3, 1, -1, -3]) > 2)

if __name__ == '__main__':
    unittest.main()
