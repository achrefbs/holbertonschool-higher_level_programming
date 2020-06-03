#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """a class BaseGeometry"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
