skip_size = 0
current_position = 0

class CircularList:
    def __init__(self, vals):
        self.data = vals

    def __getitem__(self, given):
        if isinstance(given, slice):
            return [self[x] for x in range(given.start, given.stop)]
        else:
            return self.data[given % len(self.data)]

    def __setitem__(self, given, value):
        if isinstance(given, slice):
            for i in range(given.start, given.stop):
                v = next(value)
                self[i] = v
        else:
            self.data[given % len(self.data)] = value

    def __repr__(self):
        return str(self.data)

    def reverse_portion(self, start, length):
        end = start + length
        self[start:end] = reversed(self[start:end])

lines = []
total_score = 0
total_in_garbage = 0

test_list = [0, 1, 2, 3, 4]
real_list = [x for x in range(256)]
cl = CircularList(real_list)
with open("input.txt") as input_file:
    line = input_file.readline()
    lengths = [int(l) for l in line.split(',')]
    for length in lengths:
        cl.reverse_portion(current_position, length)
        current_position += length
        current_position += skip_size
        skip_size += 1

print(cl)
print(f'Part 1 answer: {cl[0] * cl[1]}')
print(f'Part 2 answer: ')


