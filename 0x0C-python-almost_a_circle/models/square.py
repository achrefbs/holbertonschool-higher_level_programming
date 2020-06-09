#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    @property
    def size(self):
        """getter"""
        return self.height

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.width = value
        self.height = value

    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        return ('[{}] ({}) {}/{} - {}'
                .format(type(self).__name__, self.id, self.x, self.y,
                        self.height))

    def update(self, *args, **kwargs):
        """update"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
