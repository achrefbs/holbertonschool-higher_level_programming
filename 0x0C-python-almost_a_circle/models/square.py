#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        return ('[{}] ({}) {}/{} - {}'
                .format(type(self).__name__, self.id, self.x, self.y,
                        self.height))
