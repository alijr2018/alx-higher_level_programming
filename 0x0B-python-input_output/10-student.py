#!/usr/bin/python3

"""
Write a class Student that defines a student
"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """def to_json"""
        if attrs is None:
            attrs = self.__dict__.keys()
        description = {}
        for attr in attrs:
            if hasattr(self, attr):
                description[attr] = getattr(self, attr)
        return (description)
