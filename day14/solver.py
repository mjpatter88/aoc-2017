# Much of this code is from from day 10

from circular_list import CircularList
NUM_ROUNDS = 64

LENGTHS_SUFFIX = [17, 31, 73, 47, 23]

def get_knot_hash(lengths):
    lengths.extend(LENGTHS_SUFFIX)
    skip_size = 0
    current_position = 0

    total_score = 0
    total_in_garbage = 0

    real_list = [x for x in range(256)]
    cl = CircularList(real_list)


    for length in lengths * NUM_ROUNDS:
        cl.reverse_portion(current_position, length)
        current_position += length
        current_position += skip_size
        skip_size += 1

    sparse_hashes = []

    for x in range(16):
        offset = 16 * x
        sh = 0
        for i in range(16):
            sh ^= cl[offset + i]

        sparse_hashes.append(sh)

    return "".join([format(sh, '02x') for sh in sparse_hashes])

hashes = []
with open("input.txt", "r") as input_file:
    key = input_file.read()[:-1]
    for x in range(128):
        new_key = key + "-" + str(x)
        lengths = [ord(c) for c in new_key]
        knot_hash = get_knot_hash(lengths)
        hashes.append(knot_hash)
        print(str(x) + '\r', end='')

num_ones = 0
for h in hashes:
    for c in h:
        binary = bin(int(c, 16))[2:] # We just want the 1s and 0s
        num_ones += binary.count('1')

print(f'Part 1 answer: {num_ones}')

