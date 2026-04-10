#!/usr/bin/env python3
"""derive function"""


def poly_derivative(poly):
    new_list = []
    for i in range(1, len(poly)):
        new_list.append(poly[i] * i)
    return new_list
