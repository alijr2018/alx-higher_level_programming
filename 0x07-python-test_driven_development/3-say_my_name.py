#!/usr/bin/python3
"""Write a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """def of say_my_name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = f"{first_name} {last_name}" if last_name else first_name
    if full_name.strip():
        print("My name is", full_name)
