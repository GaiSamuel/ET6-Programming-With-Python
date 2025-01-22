#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A test module for the mystery_8 function

Created on 21/01/2025
@author: Gai Samuel
"""
import unittest

from ..mystery_8 import mystery_8

class TestMystery8(unittest.TestCase):
    """Tests for mystery_8 function"""

    def test_minimal_input(self):
        """Test with minimal input values"""
        self.assertEqual(mystery_8([], ''), [])
        
    def test_no_match(self):
        """Test when no elements in the list match the condition."""
        self.assertEqual(mystery_8(['apple', 'banana'], 'z'), [])
        
    def test_partial_match(self):
        """Test when some elements in the list match the condition."""
        self.assertEqual(mystery_8(['apple', 'banana', 'cherry'], 'a'), ['apple', 'banana'])

    def test_all_match(self):
        """Test when all elements in the list match the condition."""
        self.assertEqual(mystery_8(['aa', 'ab', 'ac'], 'a'), ['aa', 'ab', 'ac'])

    def test_empty_string_condition(self):
        """Test when the condition string is empty."""
        self.assertEqual(mystery_8(['apple', 'banana'], ''), ['apple', 'banana'])
        
