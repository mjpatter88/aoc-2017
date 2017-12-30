from itertools import cycle

class Layer():
    def __init__(self, r):
        self.range = r
        self.scanner_position = 0
        positions = list(range(0, r)) + list(range(r-2, 0, -1))
        self.cycler = cycle(positions)
        self.step()

    def step(self):
        self.scanner_position = next(self.cycler)

    def does_catch(self):
        return self.scanner_position == 0

layers = {}
max_depth = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        left, right = map(int, line.split(": "))
        layers[left] = Layer(right)
        max_depth = max(max_depth, left)

total_severity = 0
position = -1 # Start prior to depth 0
while position < max_depth:
    position += 1
    layer = layers.get(position)
    if layer and layer.does_catch():
        total_severity += (layer.range * position)
        print(f'caught: {position}')
    for layer in layers.values():
        layer.step()


print(f'Part 1 answer: {total_severity}')

# print(f'Part 2 answer:')

