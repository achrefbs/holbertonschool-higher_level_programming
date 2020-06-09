#!/usr/bin/python3
"""the class Rectangle that inherits from Base"""
from .base import Base


class Rectangle(Base):
    """the class Rectangle that inherits from Base"""
    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """return the area value of the Rectangle"""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(end=' ')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """str"""
        return ('[{}] ({}) {}/{} - {}/{}'
                .format(type(self).__name__, self.id, self.x, self.y,
                        self.width, self.height))

    def update(self, *args):
        """update"""
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            if i == 1:
                self.width = arg
            if i == 2:
                self.height = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg
            i += 1
