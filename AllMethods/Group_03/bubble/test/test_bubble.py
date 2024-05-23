import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.bubble import bubble

class TestBubbleFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bubble([]), [])
        
    def test_integer_list(self):
        self.assertEqual(bubble([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_string_list(self):
        self.assertEqual(bubble(["d", "c", "b", "a"]), ["a", "b", "c", "d"])
        
    def test_invalid_mixed_list(self):
        with self.assertRaises(ValueError):
            bubble([1, 2.5, "3"])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            bubble("123")

if __name__ == '__main__':
    unittest.main()
