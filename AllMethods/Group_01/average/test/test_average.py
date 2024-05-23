# filename: test_average.py
import sys
import os
import unittest
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.average import average

class TestAverageFunction(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertIsNone(average([]))
        
    def test_integer_list(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)
    
    def test_float_list(self):
        self.assertEqual(average([1.5, 2.5, 3.5]), 2.5)

    def test_mixed_list(self):
        self.assertEqual(average([1, 2.5, 3]), 2.1666666666666665)
        
    def test_invalid_input_string(self):
        with self.assertRaises(ValueError):
            average(["1", "2", "3"])
            
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            average("123")

if __name__ == '__main__':
    unittest.main()
