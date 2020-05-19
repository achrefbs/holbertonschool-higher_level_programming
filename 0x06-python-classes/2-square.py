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
