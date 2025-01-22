#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mystery_6(a:int, b:int)-> list:
    """Generates a list if length a, starting from b and increasing by 1 for each following element.

    Parameters:
        a (int): The desired length of the resulting list
        b (int): The starting number for the list

    Returns:
        List: A list containing a numbers starting from b
        
    Examples:
        >>> mystery_6(5, 4)
        [4, 5, 6, 7, 8]
        
        >>> mystery_6(2, 1)
        [1, 2]
        
        >>> mystery_6(0,8)
        []
        
        >>> mystery_6(0, 0)
        []
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
