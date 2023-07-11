#!/usr/bin/python3

"""
Write a function that writes an Object to a
text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """def of save_to_json_file"""
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
