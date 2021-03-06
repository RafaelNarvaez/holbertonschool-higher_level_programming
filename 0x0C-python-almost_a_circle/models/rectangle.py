#!/usr/bin/python3
""" Module Rectangle """
from models.base import Base


class Rectangle(Base):
    ''' a class Rectangle that inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initialize an object '''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' get width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Set width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Get Height '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set Height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' Get X '''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set X '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' Get Y '''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set Y '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''return the area of a rectangle '''
        return self.width * self.height

    def display(self):
        ''' Print a Rectangle '''
        for newLine in range(self.y):
            print()

        for idx in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for idy in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''Overrides a rectangle '''
        s = '[Rectangle] ({}) {}/{} - {}/{}'
        return s.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **keywords):
        ''' Update square with args '''
        idx = 0
        if args:
            while idx < len(args):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.size = args[idx]
                if idx == 2:
                    self.x = args[idx]
                if idx == 3:
                    self.y = args[idx]
                idx += 1
        else:
            for arg in keywords:
                setattr(self, arg, keywords.get(arg))

    def to_dictionary(self):
        ''' Returns dictionary representation of Rectangle '''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
