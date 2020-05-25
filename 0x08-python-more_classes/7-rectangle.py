#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print"""
        str = ""
        if self.__width is 0 or self.__height is 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str += Rectangle.print_symbol
            if i < self.__height - 1:
                    str += '\n'
        return str

    def __repr__(self):
        """repr"""
        str = "Rectangle({}, {})".format(self.__width, self.__height)
        return str

    def __del__(self):
        """deletion"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
