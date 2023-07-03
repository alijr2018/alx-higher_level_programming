#!/usr/bin/python3
"""
This is a Rectangle module
"""


class Rectangle:
    """The Rectangle class and def for length and width"""
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        if not isinstance(value, int):
            raise TypeError("lenght must be an integer")
        if value < 0:
            raise ValueError("lenght must be >= 0")
        self.__lenght = value
