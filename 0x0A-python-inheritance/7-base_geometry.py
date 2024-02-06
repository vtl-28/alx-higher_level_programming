#!/usr/bin/python3

"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def __init__(self):
        pass

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
