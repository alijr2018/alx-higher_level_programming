#!/usr/bin/python3

"""
Write a function that returns an object
(Python data structure) represented by a JSON string:
"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """def of to_json"""
        if attrs is None:
            attrs = self.__dict__.keys()
        description = {}
        for attr in attrs:
            if hasattr(self, attr):
                description[attr] = getattr(self, attr)
        return (description)

    def reload_from_json(self, json):
        """def of reload_from_json"""
        for attr, value in json.items():
            setattr(self, attr, value)
