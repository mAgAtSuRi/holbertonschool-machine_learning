#!/usr/bin/env python3
"""slice a matrix along specific axes"""


def np_slice(matrix, axes={}):
	if axes == None:
		return None
	return matrix[axes[0]]