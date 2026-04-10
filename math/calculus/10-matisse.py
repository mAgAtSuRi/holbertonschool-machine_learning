#!/usr/bin/env python3
"""derive function"""


def poly_derivative(poly):
    """derive a poly"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    return [i * poly[i] for i in range(1, len(poly))]
