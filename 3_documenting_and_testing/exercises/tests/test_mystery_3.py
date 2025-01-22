#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test module for mystery_3 function

Created on: 18/01/2025
@author: Gai Samuel"""
import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """tests for the mystery_3 function """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_3(0, 0), 0)

    def test_a_greater_than_b(self):
        """Test for when a is greater than b"""
        self.assertEqual(mystery_3(8,3), 3)
        
    def test_a_less_than_b(self):
        """Test for when a is less than b"""
        self.assertEqual(mystery_3(4,7), 4)
        
    def test_a_equal_to_b(self):
        """Test for when a and b are equal"""
        self.assertEqual(mystery_3(1,1), 2)
        
    def test_boundary_values(self):
        """Test boundary values"""
        self.assertEqual(mystery_3(-2147483648, 2147483647), -2147483648)
        self.assertEqual(mystery_3(2147483647, 2147483647), 4294967294)
        
    def test_both_negative(self):
        """Test when both a and b are negative"""
        self.assertEqual(mystery_3(-4, -7), -7)
        self.assertEqual(mystery_3(-7, -4), -7)
        self.assertEqual(mystery_3(-5, -5), -10)
        
    def test_negative_a(self):
        """Test when a is negative"""
        self.assertEqual(mystery_3(-3, 2), -3)
    
    def test_negative_b(self):
        """Test when b is negative"""
        self.assertEqual(mystery_3(3, -2), -2)
        
    def test_a_zero(self):
        """Test when a is zero"""
        self.assertEqual(mystery_3(0, 5), 0)
    
    def test_b_zero(self):
        """Test when b is zero"""
        self.assertEqual(mystery_3(5, 0), 0)
