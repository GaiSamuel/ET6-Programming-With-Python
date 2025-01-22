#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
A module of mystery_2 function that determines length of a sequence.

Module contents:
Returns integer if sequence isn't empty
Returns 'None' if sequence is empty.

Created on 12_16_2024
Author: Gai Samuel
"""
def mystery_2(a):
    """"
    A function for determining the length of a sequence in mystery_2.
    
    A sequence refers to(string, list, tuple etc)
    
    Parameters:
        a is a sequence whose length is to be determined.
        
    Returns:
        integer of sequence a: if a isn't empty
        None: if sequence a was empty
    
    Raises:
        TypeError for a boolean input
        
    Examples:
        >>> len([])
        0
        >>> len('Gai')
        3
        >>> len([1,2,3,4,5])
        5
        >>> len({1,2,3})
        3
    
        """
    #checks if input is boolean.
    if isinstance(a, bool):
        raise TypeError('Input must not be a boolean')
    
    if isinstance(a, int):
        raise TypeError('Input must not be an integer')

    if len(a) == 0:
        return None

    return len(a)
