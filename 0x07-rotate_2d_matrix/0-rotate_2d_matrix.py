#!/usr/bin/python3
"""
    Module with function implementing 2D matrix rotation about
    an axis at 90 degrees.

"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D n x n matrix 90 degrees clockwise"""
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
