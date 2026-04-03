#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def bars():
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))

    plt.figure(figsize=(6.4, 4.8))

    bottom = np.zeros(3)
    names = ["Farrah", "Fred", "Felicia"]
    labels = ["apples", "bananas", "oranges", "peaches"]
    colors = ["red", "yellow", "orange", "peachpuff"]
    for i, row in enumerate(fruit):
        plt.bar(names, row, bottom=bottom, color=colors[i], label=labels[i])
        bottom += row
    plt.ylabel("Quantity of Fruit")
    plt.ylim(0, 80)
    plt.legend()
    plt.show()
