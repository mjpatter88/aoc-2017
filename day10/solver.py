skip_size = 0
current_position = 0

class CircularList:
    def __init__(self, vals):
        self.data = vals

    def __getitem__(self, given):
        if isinstance(given, slice):
            #TODO: handle slice here
            pass
        else:
            return self.data[index % len(self.data)]

    def __repr__(self):
        return str(self.data)

    def reverse_portion(self, start, length):
        self[start:length] = reversed(self[start:length])

lines = []
total_score = 0
total_in_garbage = 0

test_list = [0, 1, 2, 3, 4]
cl = CircularList(test_list)
with open("test_input.txt") as input_file:
    line = input_file.readline()
    lengths = [int(l) for l in line.split(',')]
    for length in lengths:
        cl.reverse_portion(current_position, length)
        current_position += length
        current_position += skip_size
        skip_size += 1

print(cl)
print(f'Part 1 answer: ')
print(f'Part 2 answer: ')


