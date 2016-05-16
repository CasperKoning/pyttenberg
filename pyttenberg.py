from color import random_color
from battenberg_tree import BattenbergTree
import matplotlib.pyplot as plt
import argparams


def make_list_of_unique_colors(number_of_colors):
    num_completed = 0
    color_set = set()
    while num_completed != number_of_colors:
        color = random_color()
        if color not in color_set:
            color_set.add(color)
            num_completed += 1
    return list(color_set)


def plot_battenberg_tree(tree, output_path):
    fig = plt.figure(figsize=(10,10), dpi=200)
    ax = plt.Axes(fig, [0., 0., 1., 1.], autoscale_on=False, frameon=False)
    ax.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off')
    fig.add_axes(ax)
    plt.axis('off')
    tree.plot(ax, 0, 0, 1., 1.)
    fig.savefig(output_path)


def main():
    colors = make_list_of_unique_colors(argparams.number_of_colors)
    color_tree = BattenbergTree(colors)
    plot_battenberg_tree(color_tree, argparams.output_path)


if __name__ == '__main__':
    main()
