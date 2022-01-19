#!/usr/bin/python3
'''This module defines a class named as Square'''


class Square:
    '''Create a Square'''

    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
