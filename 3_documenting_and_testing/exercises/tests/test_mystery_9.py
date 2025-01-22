#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A test module for the mystery_9 function.

Created on 22/01/2025
Authors: Gai Samuel"""
import unittest

from ..mystery_9 import mystery_9

class TestMystery9(unittest.TestCase):
    """Tests for the mystery_9 function"""

    def test_minimal_input(self):
        """Test with an empty list."""
        self.assertEqual(mystery_9([]), [])
        
    def test_single_element(self):
        """Test with a single-element list."""
        self.assertEqual(mystery_9([5]), [5])

    def test_already_sorted(self):
        """Test with an already sorted list."""
        self.assertEqual(mystery_9([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_sorted(self):
        """Test with a reverse-sorted list."""
        self.assertEqual(mystery_9([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted(self):
        """Test with an unsorted list."""
        self.assertEqual(mystery_9([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        """Test with a list containing duplicate elements."""
        self.assertEqual(mystery_9([4, 2, 4, 1, 2]), [1, 2, 2, 4, 4])
