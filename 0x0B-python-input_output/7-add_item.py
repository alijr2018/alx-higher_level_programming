#!/usr/bin/python3

"""
Write a script that adds all arguments to a Python list,
and then save them to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """def of save_to_json_file"""
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """def of load_from_json_file"""
    with open(filename) as file:
        return (json.load(file))


try:
    items = load_from_json_file("add_item.json")
except Exception:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, "add_item.json")
