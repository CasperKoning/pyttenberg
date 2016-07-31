import numpy


class BattenbergTree:
    def __init__(self, entities):
        self.num_entities = len(entities)
        if self.num_entities == 2:
            self.left = BattenbergLeaf(entities[0])
            self.right = BattenbergLeaf(entities[1])
        else:
            left_entities = entities[:int(self.num_entities / 2)]
            right_entities = entities[int(self.num_entities / 2):]
            self.left = BattenbergTree(left_entities)
            self.right = BattenbergTree(right_entities)

    def to_pixels(self):
        pixels = numpy.zeros((self.num_entities, self.num_entities, 3))
        self._fill_pixels(pixels, 0, 0)
        return pixels

    def _fill_pixels(self, pixels, x, y):
        half_width = self.num_entities / 2
        half_height = self.num_entities / 2
        self.left._fill_pixels(pixels, x, y)
        self.left._fill_pixels(pixels, x + half_width, y + half_height)
        self.right._fill_pixels(pixels, x + half_width, y)
        self.right._fill_pixels(pixels, x, y + half_height)


class BattenbergLeaf:
    def __init__(self, value):
        self.value = value

    def _fill_pixels(self, matrix, x, y):
        matrix[x, y, :] = self.value.to_array()
