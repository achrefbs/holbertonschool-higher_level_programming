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
        with open(cls.__name__ + ".json", "w") as f:
            for obj in list_objs:
                l.append(obj.to_dictionary())
            f.write(cls.to_json_string(l))
