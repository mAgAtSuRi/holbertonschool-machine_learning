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
    colors = ["red", "yellow", "#ff8000", "#ffe5b4"]
    for i, row in enumerate(fruit):
        plt.bar(names, row, bottom=bottom, color=colors[i], label=labels[i], width=0.5)
        bottom += row
    plt.ylabel("Quantity of Fruit")
    plt.ylim(0, 80)
    plt.yticks(range(0, 81, 10))
    plt.legend()
    plt.title('Number of Fruit per Person')
    plt.show()

bars()