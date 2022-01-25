#!/usr/bin/python3
"""This is a class named as Rectangle"""


class Rectangle:
    """
        A Rectangle class that counts the instances
    """
    instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).instances += 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return(("#"*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        type(self).instances -= 1
        print("Bye rectangle...")
