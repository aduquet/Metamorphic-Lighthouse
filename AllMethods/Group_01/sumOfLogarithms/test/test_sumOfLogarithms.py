import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
import math
from src.sumOfLogarithms import sumOfLogarithms

class TestLogarithmSum(unittest.TestCase):

    def test_sum_log_normal(self):
        self.assertAlmostEqual(sumOfLogarithms([1, 2, 3]), math.log(1) + math.log(2) + math.log(3))

    def test_sum_log_empty(self):
        self.assertEqual(sumOfLogarithms([]), 0)

    def test_sum_log_invalid_input(self):
        with self.assertRaises(TypeError):
            sumOfLogarithms("string")

    def test_sum_log_strings_in_list(self):
        with self.assertRaises(ValueError):
            sumOfLogarithms(["a", "b", "c"])

    def test_sum_log_negative_numbers(self):
        with self.assertRaises(ValueError):
            sumOfLogarithms([-1, 1, 2])

if __name__ == '__main__':
    unittest.main()
