#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2 or type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) != int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter"""
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        for i in range(self.size):
            for c in range(self.position[0]):
                print(end=' ')
            for j in range(self.size):
                print("#", end='')
            print()
