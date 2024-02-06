#!/usr/bin/python3

"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class with public instance methods area and integer_validator"""
    def __init__(self, width, height):
        """ instantion of class"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """raises an exception when called"""
        return self.__width * self.__height

    def __str__(self):
        """prints string representation of object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
