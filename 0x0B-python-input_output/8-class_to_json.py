#!/usr/bin/python3

"""
Write a function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """def of class_to_json"""
    description = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            description[attr] = value
    return (description)
