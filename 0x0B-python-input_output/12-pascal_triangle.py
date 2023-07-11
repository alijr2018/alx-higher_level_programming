#!/usr/bin/python3

"""
Write a function that returns an object
(Python data structure) represented by a JSON string:
"""


def pascal_triangle(n):
    """def of pascal_tringle"""
    if n <= 0:
        return ([])
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)
    return (triangle)
