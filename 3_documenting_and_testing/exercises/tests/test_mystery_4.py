#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test module for mystery_4 function

Created on 12_16_2024
@author: Gai Samuel"""
import unittest

from ..mystery_4 import mystery_4

class TestMystery4(unittest.TestCase):
    """Tests for mystery_4 function """

    def test_minimal_input(self):
        """Test with minimal input"""
        self.assertEqual(mystery_4(0), [])

    def test_positive_input(self):
        """Test with a positive integer"""
        self.assertEqual(mystery_4(5), [0, 1, 2, 3, 4])
        
    def test_negative_input(self):
        """Test with a negative integer"""
        self.assertEqual(mystery_4(-1), [])
        
    def test_large_input(self):
        """Test with a large integer"""
        self.assertEqual(mystery_4(1000), list(range(1000)))

        
    def test_non_integer_input(self):
        """Test with non-integer inputs"""
        with self.assertRaises(TypeError):
            mystery_4(3.5) # type: ignore
        with self.assertRaises(TypeError):
            mystery_4("string") # type: ignore
