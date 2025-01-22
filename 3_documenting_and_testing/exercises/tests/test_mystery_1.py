#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Module for mystery_1 function.

Created on 12_16_2024
Author: Gai Samuel
"""

import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """Test the mystery_1 function"""

    def test_minimal_input(self):
        """Test for zero input"""
        self.assertEqual(mystery_1(0, 0), 0)
        
    def test_integer_input(self):
        """Test for integer input"""
        self.assertEqual(mystery_1(4,2), 6)
        
    def test_float_input(self):
        """Test for a float input"""
        self.assertEqual(mystery_1(2.9,3.0), 5.9)
        
    def test_negative_integer_input(self):
        """Test for a negative integer input"""
        self.assertEqual(mystery_1(-4,-6), -10)
        
    def test_negative_float_input(self):
        """Test for a negative float input"""
        self.assertEqual(mystery_1(-6.1,-4.2), -10.3)

    def test_float_and_integer_input(self):
        """test for float and integer input"""
        self.assertEqual(mystery_1(8.1,4), 12.1)

    def test_large_numbers(self):
        """Test for very large numbers"""
        self.assertEqual(mystery_1(1e10, 1e10), 2e10)
        
    def test_small_numbers(self):
        """Test for very small numbers"""
        self.assertAlmostEqual(mystery_1(1e-10, 1e-10), 2e-10)
    
    def test_invalid_types(self):
        """Test for invalid non-numeric inputs"""
        with self.assertRaises(TypeError):
            mystery_1(None, 5) # type: ignore
        with self.assertRaises(TypeError):
            mystery_1("string", 5) # type: ignore
        with self.assertRaises(TypeError):
            mystery_1(5, [1, 2, 3]) # type: ignore
        with self.assertRaises(TypeError):
            mystery_1({}, 5) # type: ignore
