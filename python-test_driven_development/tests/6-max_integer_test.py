#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines a class for testing max_integer function"""

    def test_max_end(self):
        """Test with the max at the end"""
        test_list = [1, 2, 3, 4]
        result = max_integer(test_list)
        self.assertEqual(result, 4)

    def test_max_begin(self):
        """Test with the max at the beginning"""
        test_list = [4, 3, 2, 1]
        result = max_integer(test_list)
        self.assertEqual(result, 4)

    def test_max_middle(self):
        """Test with the max in the middle"""
        test_list = [1, 4, 2, 3]
        result = max_integer(test_list)
        self.assertEqual(result, 4)

    def test_one_element(self):
        """Test with a list of one element"""
        test_list = [5]
        result = max_integer(test_list)
        self.assertEqual(result, 5)

    def test_empty_list(self):
        """Test with an empty list"""
        test_list = []
        result = max_integer(test_list)
        self.assertEqual(result, None)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        test_list = [-1, -2, -3, -4]
        result = max_integer(test_list)
        self.assertEqual(result, -1)

    def test_mix_neg_pos(self):
        """Test with a list of negative and positive numbers"""
        test_list = [-1, -2, 3, 4]
        result = max_integer(test_list)
        self.assertEqual(result, 4)

    def test_non_integers(self):
        """Test with non-integer elements"""
        test_list = [1, "two", 3, 4]
        self.assertRaises(TypeError, max_integer, test_list)

    def test_no_argument(self):
        """Test with no argument"""
        result = max_integer()
        self.assertEqual(result, None)
