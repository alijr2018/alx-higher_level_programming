#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry.
"""


class BaseGeometry:
    """calss of base geometry"""

    def area(self):
        """def of area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """def integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """the class of rectangle"""

    def __init__(self, width, height):
        """def init"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
