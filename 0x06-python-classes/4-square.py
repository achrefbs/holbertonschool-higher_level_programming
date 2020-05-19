#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
