#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A module for the mystery_9 function that modifies the input list a
using the Bubble Sort algorithm.

Created on 22/01/2025
@author: Gai Samuel
"""
def mystery_9(a: list)-> list:
    """  Sorts a list "a" in ascending order. 

    Parameters:
        a (list): A list of comparable elements to sort.

    Returns:
        list: The sorted list in ascending order.
        
    Examples:
        >>> mystery_9([3, 4, 2])
        [2, 3, 4]
        >>> mystery_9(['b', 'c', 'a'])
        ['a', 'b', 'c']
        >>> mystery_9([1, 2, 1, 2])
        [1, 1, 2, 2]
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
