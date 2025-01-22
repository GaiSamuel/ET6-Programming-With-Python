#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A module for mystery_4 function that creates a list containing integers

Module contents:
Returns list of integers from 0 until when given length is reached. 

Created on 12_16_2024
Author: Gai Samuel
"""
def mystery_4(a: int)-> list:
    """Creates a list of integers in ascending order starting from zero excluding the given length in this case (a).
    
    Parameters:
        a is the integer length on which the function stops. 
        
    Returns:
        A list of integers excluding the given length
        
    Examples:
        >>> mystery_4(9)
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
        >>> mystery_4(0)
        []
        >>> mystery_4(2)
        [0, 1]
        """
    if not isinstance(a, int):
        raise TypeError('Input must be an integer')
    
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
