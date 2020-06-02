#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """init"""
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """area"""
        return self.__size ** 2

    def __str__(self):
        """__str__"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
