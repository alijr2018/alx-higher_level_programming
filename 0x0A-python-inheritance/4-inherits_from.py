#!/usr/bin/python3
"""
Write a function that returns True otherwise False.
"""


def inherits_from(obj, a_class):
    """def of the function"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
