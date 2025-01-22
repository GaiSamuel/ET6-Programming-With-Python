#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for _count_vowels_function
Some tests are buggy!

Created on 12_16_2024
Author: Gai Samuel
"""

import unittest

from ..count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    """Test the count_vowels function - some tests are buggy!"""

    # TODO: as an exercise, write more tests!
    
    def test_empty_string(self):
        """It should return 0 for an empty string"""
        self.assertEqual(count_vowels(""), 0)
        
    def test_no_vowels(self):
        """It should return 0 for strings without vowels"""
        self.assertEqual(count_vowels("cry"), 0)
        
    def test_all_vowels(self):
        """It should count all vowels in a string"""
        self.assertEqual(count_vowels("AUIO"), 4)
        
    def test_mixed_case(self):
        """It should handle mixed case strings"""
        self.assertEqual(count_vowels("Hello World"), 3)
        
    def test_not_string(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            count_vowels(123) # type: ignore
            
    def test_set_input(self):
        """test with set input"""
        with self.assertRaises(AssertionError):
            count_vowels({1, 2, 3, 4, 5}) # type: ignore
            
    def test_whitespace_only(self):
        """It should return 0 for strings with only whitespace."""
        self.assertEqual(count_vowels("     "), 0)

    def test_whitespace_with_vowels(self):
        """It should count vowels in strings with leading/trailing whitespace."""
        self.assertEqual(count_vowels("  aeiou  "), 5)
        
    def test_special_characters(self):
        """It should ignore special characters and count only vowels."""
        self.assertEqual(count_vowels("@!#a$%^e&*()i123"), 3)
        
    def test_none_input(self):
        """It should raise AssertionError for None input."""
        with self.assertRaises(AssertionError):
            count_vowels(None)  # type: ignore
            
    def test_uppercase_string(self):
        """It should count vowels in uppercase strings."""
        self.assertEqual(count_vowels("AEIOU"), 5)
        
    def test_long_string(self):
        """It should count vowels in a long string."""
        long_string = "a" * 1000 + "b" * 1000 + "e" * 1000
        self.assertEqual(count_vowels(long_string), 2000)
        
    def test_numeric_string(self):
        """It should return 0 for numeric strings."""
        self.assertEqual(count_vowels("1234567890"), 0)
