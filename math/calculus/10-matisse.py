#!/usr/bin/env python3
"""derive function"""


def poly_derivative(poly):
    if len(poly) == 0 or not isinstance(poly, list):
        return None
    if len(poly) == 1:
        return 0
    return [i * poly[i] for i in range(1, len(poly))]
