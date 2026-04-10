#!/usr/bin/env python3
"""calculate sum"""


def summation_i_squared(n):
    if type(n) is not int:
        return None
    return sum(i**2 for i in range(1, n + 1))
