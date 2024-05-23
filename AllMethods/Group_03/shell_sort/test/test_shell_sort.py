import unittest
import os
import sys

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.shell_sort import shell_sort

import unittest

class TestShellSort(unittest.TestCase):

    def test_shell_sort(self):
        self.assertEqual(shell_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])

    def test_empty_array(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(shell_sort([1]), [1])

if __name__ == '__main__':
    unittest.main()
