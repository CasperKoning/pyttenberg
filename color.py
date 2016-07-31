import random


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def to_hex(self):
        return '#%02x%02x%02x' % (self.r, self.g, self.b)


def random_color():
    return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
