#!/usr/bin/env python3
"""function to determine shape of a matrix"""


def matrix_shape(matrix):
    """Return the shape of a matrix"""
    shape = []
    current = matrix
    while isinstance(current, list):
        shape.append(len(current))
        current = current[0]
    return shape
