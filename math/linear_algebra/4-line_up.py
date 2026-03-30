#!/usr/bin/env python3
"""add 2 matrix"""


def add_arrays(arr1, arr2):
    """return sum of 2 matrix"""
    if len(arr1) != len(arr2):
        return None
    sum_arr = []
    for i in range(len(arr1)):
        sum_arr.append(arr1[i] + arr2[i])
    return sum_arr
