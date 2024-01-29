#!/usr/bin/python3

''' Regular Rectangle class '''


class Rectangle:
    ''' Representation of Rectangle class '''

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        ''' height getter attribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter attribute '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        ''' width getter attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter attribute '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        ''' instance method that return the area of a rectangle '''
        return self.__height * self.__width

    def perimeter(self):
        ''' instance method that return the perimeter of a rectangle '''
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        perimeter = 2 * (self.__height + self.__width)
        return perimeter
