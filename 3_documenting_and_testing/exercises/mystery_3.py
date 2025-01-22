#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for mystery_3 function that compares two numbers and returns result based on how they compare.

Module contents:
Compares and returns a if a<b
Compares and returns b if a>b
Compares and returns sum(a+b) if a = b

Created on 12_16_2024
Author: Gai Samuel
"""

def mystery_3(a:int, b:int )->int :
    """Compares two numbers and then returns result based on how they compare.
    
    Parameters:
    a(is the first number and is an integer)
    b(is the second number and is an integer)
    
    Returns:
    a (if a is less than b)
    b (if a is greater than b)
    a + b (if a is equal to b)
    
    Examples:
        >>> mystery_3(3, 6)
        3
        
        >>> mystery_3(9,2)
        2
        
        >>> mystery_3(20, 20)
        40
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
