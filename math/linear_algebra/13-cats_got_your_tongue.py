#!/usr/bin/env python3
"""concatenates 2 matrices along an axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return a concatenates matrice along the specified axis"""
    return np.concatenate([mat1, mat2], axis=axis)
