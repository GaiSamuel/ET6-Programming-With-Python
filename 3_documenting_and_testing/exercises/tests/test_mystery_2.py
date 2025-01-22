#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""A test module for mystery_2 function

Created on: 18/01/2025
@author: Gai Samuel
"""
import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """Test the mystery_2 function """

    def test_empty_list_input(self):
        """test for a minimal list input"""
        self.assertEqual(mystery_2([]), None)

    def test_empty_string_input(self):
        """test for a empty string inout"""
        self.assertEqual(mystery_2(''), None)
        
    def test_list_input(self):
        """Test for list input"""
        self.assertEqual(mystery_2([1,2,3,4,5]), 5)
        
    def test_string_input(self):
        """Test for string input"""
        self.assertEqual(mystery_2('Perfect'), 7)
        
    def test_tuple_input(self):
        """Test for tuple input"""
        self.assertEqual(mystery_2((6,5,9)),3)

    def test_set_input(self):
        """Test for set input"""
        self.assertEqual(mystery_2({'gai','a',6}), 3)
        
    def test_dictionary_input(self):
        """Test for dictionary input"""
        self.assertEqual(mystery_2({'name': 'Gai'}), 1)
        
    def test_boolean_input(self):
        """Test for boolean input"""
        with self.assertRaises(TypeError):
            mystery_2(True)
            mystery_2(False)

    def test_integer_input(self):
        """Test for an integer input"""
        with self.assertRaises(TypeError):
            mystery_2(44)
