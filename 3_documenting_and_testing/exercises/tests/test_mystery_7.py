#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A test module for the mystery_7 function.

Created on 21/01/2025
@author: Gai Samuel
"""
import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """Tests for the mystery_7 function """

    def test_minimal_input_list(self):
        """Handles empty input lists"""
        self.assertEqual(mystery_7([], []), [])

    def test_minimal_input_string(self):
        """Handles empty input strings"""
        self.assertEqual(mystery_7('', ''), [])
        
    def test_uncommon_string_inputs(self):
        """Handles string inputs"""
        self.assertEqual(mystery_7('abc', 'bcd'), [])
        
    def test_common_string_input(self):
        """Handles common string input"""
        self.assertEqual(mystery_7('abc', 'abc'), [])
        
    def test_integer_input(self):
        """Raises typeError for an integer input"""
        with self.assertRaises(TypeError):
            mystery_7((1, 2), (2, 4))
