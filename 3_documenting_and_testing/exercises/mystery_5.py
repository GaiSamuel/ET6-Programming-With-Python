#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the `mystery_5` function, which sorts the elements 
of one list (`a`) and appends them to another list (`b`).

functions:
    mystery_5(a, b): Validates input, sorts the elements of `a`, and appends them to `b`.
"""
def mystery_5(a: list, b: list)-> list:
    """
    Sorts the elements of list `a` in ascending order and appends them to list `b`.

    Parameters:
        a (list): A list of comparable elements to be sorted and removed.
        b (list): A list to which sorted elements of `a` will be appended.

    Returns:
        list: List `b` containing the sorted elements of `a`.

    Examples:
        >>> mystery_5([3, 1, 4], [])
        [1, 3, 4]

        >>> mystery_5([5, 2, 2], [1])
        [1, 2, 2, 5]

        >>> mystery_5([], [10])
        [10]
        """
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("input must be a list")
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
