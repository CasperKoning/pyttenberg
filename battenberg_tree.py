import matplotlib.patches as patches


class BattenbergTree:
    def __init__(self, entities):
        num_entities = len(entities)
        if num_entities == 2:
            self.left = BattenbergLeaf(entities[0])
            self.right = BattenbergLeaf(entities[1])
        else:
            left_entities = entities[:int(num_entities / 2)]
            right_entities = entities[int(num_entities / 2):]
            self.left = BattenbergTree(left_entities)
            self.right = BattenbergTree(right_entities)

    def plot(self, ax, x, y, width, height):
        half_width = width / 2
        half_height = height / 2
        self.left.plot(ax, x, y, half_width, half_height)
        self.left.plot(ax, x + half_width, y + half_height, half_width, half_height)
        self.right.plot(ax, x + half_width, y, half_width, half_height)
        self.right.plot(ax, x, y + half_height, half_width, half_height)


class BattenbergLeaf:
    def __init__(self, value):
        self.value = value

    def plot(self, ax, x, y, width, height):
        ax.add_patch(
            patches.Rectangle(
                (x, y), width, height,
                facecolor=self.value.to_hex(),
                edgecolor="none"     # No border
            )
        )
