#!/usr/bin/python3
"""This is a class named as Rectangle"""


class Rectangle:
    """
    Defines a Rectangle
    Args:
            width = Rectangle width (int)
            height = Rectangle height (int)
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retreive the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retreive the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value