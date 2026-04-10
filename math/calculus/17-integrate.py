#!/usr/bin/env python3
"""calculate integral of polynomial"""


def poly_integral(poly, C=0):
    """calculate integral of a poly"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, (int, float)):
        return None

    new_list = [C]
    for i in range(1, len(poly) + 1):
        coef = poly[i - 1] / i
        new_list.append(int(coef) if coef == int(coef) else coef)
    return new_list
