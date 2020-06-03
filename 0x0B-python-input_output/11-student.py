#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(obj):
        """returns the dictionary description with simple data structure"""
        return(obj.__dict__)
