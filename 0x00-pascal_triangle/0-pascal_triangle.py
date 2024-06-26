#!/usr/bin/python3
"""
    Module implementing Pascals triangle.
"""


def pascal_triangle(n):
    """Function implementing the pascal triangle"""
    if n <= 0:
        return []

    result = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)
    return result
