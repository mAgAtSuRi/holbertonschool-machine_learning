#!/usr/bin/env python3
"""add 2d matrices"""


def add_matrices2D(mat1, mat2):
    """return the sum of 2d matrices"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    new_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        new_mat.append(row)
    return new_mat
