from circular_list import CircularList

skip_size = 0
current_position = 0

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

