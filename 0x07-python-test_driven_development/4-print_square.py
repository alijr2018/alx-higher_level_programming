#!/usr/bin/python3
"""Write a function that prints a square with the character #."""


def print_square(size):
    """def of print_square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("x" * size)
