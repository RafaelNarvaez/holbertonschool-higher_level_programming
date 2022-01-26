#!/usr/bin/python3
"""
    Test-driven development
    print_square - Arg:
        size: int
"""


def print_square(size):
    """
    Print a square by size side long
    """
    if type(size) in [int, float]:
        if type(size) is float and size < 0:
            raise ValueError("size must be an integer")
        else:
            if size >= 0:
                size = int(size)
                for i in range(size):
                    print("#" * size)
            else:
                raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
