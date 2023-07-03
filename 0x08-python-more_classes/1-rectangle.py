#!/usr/bin/python3
"""
This is a Rectangle module
"""


class Rectangle:
    """The Rectangle class and def for height and width"""
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
