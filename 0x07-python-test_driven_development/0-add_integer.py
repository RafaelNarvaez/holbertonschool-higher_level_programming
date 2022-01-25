#!/usr/bin/python3
"""
Module Add Integer
"""


def add_integer(a, b=98):
    """
    Add integer a, b
    Raises:
        TypeError: a or b are not int or float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError('a must be an integer')
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
