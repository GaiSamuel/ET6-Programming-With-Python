#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test module for mystery_5 function

Created on: 18/01/2025
@author: Gai Samuel"""
import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """Tests for mystery_5 function"""

    def test_minimal_input(self):
        """Test with minimal input"""
        self.assertEqual(mystery_5([], []), [])
        
    def test_single_element(self):
        """Test when a has one element"""
        self.assertEqual(mystery_5([5], []), [5])
        
    def test_existing_elements_in_b(self):
        """Test when b already has elements"""
        self.assertEqual(mystery_5([3, 1], [2]), [2, 1, 3])
        
    def test_duplicates_in_a(self):
        """Test when a contains duplicate elements"""
        self.assertEqual(mystery_5([4, 4, 2], []), [2, 4, 4])
        
    def test_elements_in_b_and_a(self):
        """Test when both a and b have elements"""
        self.assertEqual(mystery_5([3, 1], [5, 4]), [5, 4, 1, 3])
        
    def test_empty_a_non_empty_b(self):
        """Test when a is empty and b is not"""
        self.assertEqual(mystery_5([], [6, 7]), [6, 7])
        
    def test_reverse_sorted_a(self):
        """Test when a is reverse sorted"""
        self.assertEqual(mystery_5([3, 2, 1], []), [1, 2, 3])
        
    def test_mixed_types(self):
        """Test when a contains mixed types"""
        with self.assertRaises(TypeError):  # Adjust if mixed types are allowed
            mystery_5([1, "a", 2], [])
