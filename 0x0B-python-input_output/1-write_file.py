#!/usr/bin/python3

"""
Write a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """def of write_file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
    return (len(text))
