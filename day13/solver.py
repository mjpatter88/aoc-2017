from itertools import cycle

class Layer():
    def __init__(self, r):
        self.range = r
        self.scanner_position = 0

    def step(self, amount=1):
        self.scanner_position += amount

    def does_catch(self):
        cycle = (self.range - 1) * 2
        return self.scanner_position % cycle == 0

    def set_delay(self, amount):
        self.scanner_position = amount

def reset_layers():
    for layer in layers.values():
        layer.scanner_position = 0

def get_total_severity():
    total_severity = 0
    position = -1 # Start prior to depth 0
    while position < max_depth:
        position += 1
        layer = layers.get(position)
        if layer and layer.does_catch():
            total_severity += (layer.range * position)
        for layer in layers.values():
            layer.step()
    return total_severity

def is_clean_run():
    position = 0 # Start prior to depth 0
    while position <= max_depth:
        layer = layers.get(position)
        if layer:
            layer.step(position)
            if layer.does_catch():
                return False
        position += 1
    return True


layers = {}
max_depth = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        left, right = map(int, line.split(": "))
        layers[left] = Layer(right)
        max_depth = max(max_depth, left)

print(f'Part 1 answer: {get_total_severity()}')
reset_layers()

# TODO: make this better. Use math to calculate rather than brute force.
delay = 0
while True:
    for layer in layers.values():
        layer.set_delay(delay)
    if is_clean_run():
        break
    delay += 1
    if delay % 100000 == 0:
        print(delay)

print(f'Part 2 answer: {delay}')

