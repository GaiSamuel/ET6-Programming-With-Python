#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for mystery_1 function that adds two numbers together.

Module contents:
    Returns integer or float result of the sum of the two numbers.
    
Created 12_16_2024
Author: Gai Samuel 
    """
def mystery_1 (a: int|float, b: int|float)-> int|float:
    """adds two numbers together
    
    parameters:
        a(is an integer or float and is the first number)
        b(is an integer or float and is the second number)
        
    Returns:
        integer or float: The sum of the two numbers
        
    Raises: Type error for an invalid input
        
    example:
        >>> mystery_1 (2,9)
        11
        >>> mystery_1(3.0,4.5)
        7.5
        
    returns a + b
        """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be an integer or a float")

    return a + b
