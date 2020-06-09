#!/usr/bin/python3
"""the first class Base"""
import json


class Base:
    """the first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        l = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    l.append(obj.to_dictionary())
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            r1 = cls(1, 1)
        if cls.__name__ == 'Square':
            r1 = cls(1)
        r1.update(**dictionary)
        return r1
