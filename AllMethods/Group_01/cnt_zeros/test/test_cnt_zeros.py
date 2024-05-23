import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.cnt_zeros import cnt_zeros


class TestCountZerosFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(cnt_zeros([]), 0)
        
    def test_integer_list(self):
        self.assertEqual(cnt_zeros([5, 0, 1, 4, 0, 0]), 3)

    def test_none_values_in_list(self):
        self.assertEqual(cnt_zeros([0, None, 0, None]), 2)
        
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            cnt_zeros("100200")

if __name__ == '__main__':
    unittest.main()
