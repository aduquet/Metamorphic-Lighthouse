import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.sampleVariance import sampleVariance

class TestSampleVariance(unittest.TestCase):

    def test_variance_of_numbers(self):
        self.assertAlmostEqual(sampleVariance([1, 2, 3, 4, 5]), 2.5)

    def test_single_element(self):
        with self.assertRaises(ValueError):
            sampleVariance([42])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            sampleVariance([])

    def test_invalid_input_string_list(self):
        with self.assertRaises(ValueError):
            sampleVariance(["a", "b"])

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            sampleVariance("string")

if __name__ == '__main__':
    unittest.main()

