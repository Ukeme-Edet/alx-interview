#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D Matrix

    Args:
        matrix: 2D matrix
    """
    res = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            res[j][-i - 1] = matrix[i][j]
    matrix[:] = res
