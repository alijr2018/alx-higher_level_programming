#!/usr/bin/python3

"""
Write a script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except Exception:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, "add_item.json")
