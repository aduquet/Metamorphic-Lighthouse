import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from scipy.stats import kurtosis as kt

from src.kurtosis import kurtosis

import unittest

class TestKurtosisFunction(unittest.TestCase):

    def test_kurtosis_of_integer_list(self):
        self.assertAlmostEqual(kurtosis([2, 7, 7, 4, 5, 9, 8]), kt([2, 7, 7, 4, 5, 9, 8]), places=4)

    def test_kurtosis_of_float_list(self):
        self.assertAlmostEqual(kurtosis([2.5, 7.2, 7.1, 4.3, 5.0, 9.8, 8.4]), kt([2.5, 7.2, 7.1, 4.3, 5.0, 9.8, 8.4]), places=4)

    def test_kurtosis_of_empty_list(self):
        with self.assertRaises(ValueError):
            kurtosis([])

    def test_kurtosis_of_non_numerical_list(self):
        with self.assertRaises(TypeError):
            kurtosis(["apple", "banana", "cherry"])

    def test_kurtosis_of_mixed_list(self):
        with self.assertRaises(TypeError):
            kurtosis([1, 2.5, "apple"])

if __name__ == "__main__":
    unittest.main()
