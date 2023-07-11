#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the class of rectangle"""

    def __init__(self, width, height):
        """def init"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

     def area(self):
        """def of area"""
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

