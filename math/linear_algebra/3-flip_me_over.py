#!/usr/bin/env python3
"""Transpose matrix"""

def matrix_transpose(matrix):
    """function to transpose a matrix"""
    transposed = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed
