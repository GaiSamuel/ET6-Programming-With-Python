#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A module for the mystery_7 function that performs filtering based on conditions.

Created on 21/01/2025
@author: Gai Samuel
"""
def mystery_7(a, b):
    """Filters the elements of a based on the presence of b.

    Parameters:
        a (iterable): An iterable of elements to filter.
        b (iterable): An iterable of elements to compare against.

    Returns:
        A list: A list containing elements from a that are also in b.
        
    Examples:
        >>> mystery_7('abc', 'bcd')
        []
        
        >>> mystery_7([], [1, 2, 3])
        []
        
        >>> mystery_7('abc', '')
        ['a', 'b', 'c']
    """
    if isinstance(a,int) or isinstance(b, int):
        raise TypeError('Input must not be an integer')
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
