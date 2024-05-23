import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
import math
from src.entropy import entropy

import unittest

class TestEntropyFunction(unittest.TestCase):

    def test_basic_entropy(self):
        self.assertAlmostEqual(entropy([1, 1]), 0.6931471805599453)  # Assuming base e

    def test_zero_elements(self):
        self.assertEqual(entropy([0, 0]), 0)

    def test_single_nonzero_element(self):
        self.assertEqual(entropy([3, 0]), 0)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):  # assuming entropy of negative values isn't valid
            entropy([-1, 2])

    def test_empty_list(self):
        self.assertEqual(entropy([]), 0)

