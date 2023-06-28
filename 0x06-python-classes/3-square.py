#!/usr/bin/python3
"""Define a class as a Square."""


class Square:
    """The square."""
    def __init__(self, size=0):
        """The def of square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """The def of area"""
        return self.__size ** 2
