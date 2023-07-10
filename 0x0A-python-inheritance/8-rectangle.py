#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry.
"""


class Rectangle:
    """the class"""
    def __init__(self, width, height):
        """def init"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """def area"""
        return (self.__width * self.__height)

    def __str__(self):
        """def str"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
