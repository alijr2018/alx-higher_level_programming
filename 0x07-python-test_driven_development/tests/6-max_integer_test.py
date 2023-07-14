#!/usr/bin/python3

""""""


import unittest
from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Class of TestMaxInteger"""
    def test_regular_list(self):
        """def of test_regular_list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """def of test_empty_list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """def of test_single_element_list"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-10]), -10)

    def test_duplicate_max(self):
        """def of test_duplicate_max"""
        self.assertEqual(max_integer([1, 2, 3, 3, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_negative_values(self):
        """def of test_negative_values"""
        self.assertEqual(max_integer([-5, -2, -9, -1]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -20, -30]), -5)


if __name__ == '__main__':
    unittest.main()
