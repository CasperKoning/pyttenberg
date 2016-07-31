import random


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def to_array(self):
        return [self.r, self.g, self.b]


def random_color():
    return Color(r=random.randint(0, 255),
                 g=random.randint(0, 255),
                 b=random.randint(0, 255))


def unique_colors(number_of_colors):
    num_completed = 0
    color_set = set()
    while num_completed != number_of_colors:
        color = random_color()
        if color not in color_set:
            color_set.add(color)
            num_completed += 1
    return list(color_set)