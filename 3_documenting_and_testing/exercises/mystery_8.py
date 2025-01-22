#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A module for the mystery_8 function that processes two inputs, a and b,
and returns a modified list based on specific conditions.
"""
def mystery_8(a: list, b:str)-> list:
    """Processes the input list a and modifies it based on the value of b.

    Parameters:
        a (list): A list of elements to process.
        b (str): A condition for processing.

    Returns:
        list: A modified version of a where elements are added or filtered based on b.
        
    Examples:
        >>> mystery_8(['Trent', 'dog', 'man'], ('a'))
        ['man']
        >>> mystery_8(['bag', 'Gai'], ('z'))
        []
        >>> mystery_8(['Gai', 'bad'], ('a'))
        ['Gai', 'bad']
    """
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
