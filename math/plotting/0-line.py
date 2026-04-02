#!/usr/bin/env python3
"""Draw a linear graph in red"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Draw a red line"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    x = np.arange(0, 11)
    plt.plot(x, y, "r-")
    plt.xlim(0, 10)
    plt.show()
