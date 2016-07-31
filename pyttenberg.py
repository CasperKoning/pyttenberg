from color import unique_colors
from battenberg_tree import BattenbergTree
import matplotlib.pyplot as plt
import argparams


def main():
    colors = unique_colors(argparams.number_of_colors)
    color_tree = BattenbergTree(colors)
    pixels = color_tree.to_pixels()
    plt.imsave(fname=argparams.output_path, arr=pixels)


if __name__ == '__main__':
    main()
