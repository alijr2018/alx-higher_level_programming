#!/usr/bin/python3
"""Define a class as a Square."""


class Square:
    """The square"""
    def __init__(self, size=0):
        """The def of square."""
        self.__size = size

    @property
    def size(self):
        """The def of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """The def of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The def of area"""
        return self.__size ** 2
