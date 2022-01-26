#!/usr/bin/python3
"""This is a class named as Rectangle"""


class Rectangle:
    """
        A Rectangle class that counts the instances
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialized and/or creates an object"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get the area of a rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """gets the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
            returns __str__ method of an object
            when is called
        """

        if self.__height == 0 or self.__width == 0:
            return ""
        return((str(self.print_symbol)*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """ returns __repr__ method for object when repr()
            is called, or eval().
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
            deletes an instancewhen called
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise ValueError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle"""

        return cls(size, size)
