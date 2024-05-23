# filename: test_array_copy.py
import sys
import os
import unittest
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.array_copy import array_copy  # Make sure to adjust the import based on where your function is defined.

class TestArrayCopyFunction(unittest.TestCase):
    
    def test_copy_empty_list(self):
        self.assertEqual(array_copy([]), [])

    def test_copy_integer_list(self):
        data = [1, 2, 3, 4, 5]
        result = array_copy(data)
        self.assertEqual(result, data)
        self.assertIsNot(result, data)  # Ensure a new list is created
    
    def test_copy_string_list(self):
        data = ['a', 'b', 'c']
        result = array_copy(data)
        self.assertEqual(result, data)
        self.assertIsNot(result, data)
    
    def test_copy_mixed_list(self):
        data = [1, 'a', 2.5, 'b']
        result = array_copy(data)
        self.assertEqual(result, data)
        self.assertIsNot(result, data)

if __name__ == '__main__':
    unittest.main()
