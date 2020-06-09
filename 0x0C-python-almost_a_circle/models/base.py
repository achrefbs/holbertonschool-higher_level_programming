#!/usr/bin/python3
"""the first class Base"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv"""
        l = []
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        l.append([obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == 'Square':
                        l.append([obj.id, obj.size, obj.x, obj.y])
            writer = csv.writer(f)
            for row in l:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                l = []
                reader = csv.DictReader(f)
                for dic in reader:
                    for key, val in dic.items():
                        dic[key] = int(val)
                    l.append(cls.create(**dic))
                return l
        except FileNotFoundError:
            return []
