#!/usr/bin/python3

"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class with public instance methods area and integer_validator"""
    def __init__(self, size):
        """instantion of class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
