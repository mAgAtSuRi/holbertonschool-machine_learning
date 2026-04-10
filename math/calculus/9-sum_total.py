#!/usr/bin/env python3
"""calculate sum"""


def summation_i_squared(n):
    """calculate the sum of i ** 2"""
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
