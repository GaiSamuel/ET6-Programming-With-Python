#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A test module for the mystery_6 function

Created on 21/01/2025
@author: Gai Samuel
"""
import unittest

from ..mystery_6 import mystery_6

class TestMystery6(unittest.TestCase):
    """Tests for the mystery_6 function"""

    def test_minimal_input(self):
        """Returns empty list"""
        self.assertEqual(mystery_6(0, 0), [])
    
    def test_value_of_b_greater_than_zero(self):
        """Returns empty list"""
        self.assertEqual(mystery_6(0, 4), [])
        
    def test_value_of_a_greater_than_0(self):
        """Returns a list of a greater than 0"""
        self.assertEqual(mystery_6(2,3), [3,4])
        
    def test_value_of_a_greater_than_b(self):
        """Returns a list of a greater than b"""
        self.assertEqual(mystery_6(4,0), [0,1,2,3])
            
    def test_standard_input_(self):
        """Handles standard inputs"""
        self.assertEqual(mystery_6(3,1), [1,2,3])
