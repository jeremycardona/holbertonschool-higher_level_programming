#!/usr/bin/python3
"""Module for unittesting max integer"""


import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_values(self):
        self.assertEqual(max_integer([-10, 50, 20, 30, 40]), 50)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_identical_elements(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_values(self):
        self.assertEqual(max_integer([1.5, 2.8, 3.1, 0.4]), 3.1)

    def test_string_values(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([None, 1, 2])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == '__main__':
    unittest.main()
