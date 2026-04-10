#!/usr/bin/env python3
"""calculate sum"""


def summation_i_squared(n):
    """calculate the sum of i ** 2"""
    if type(n) is not int:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
