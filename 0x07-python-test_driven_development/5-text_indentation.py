#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """def of text_indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    result = ""

    for char in text:
        result += char
        if char in punctuations:
            result += '\n\n'

    print(result.strip())
