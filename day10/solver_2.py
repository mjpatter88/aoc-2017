from circular_list import CircularList
NUM_ROUNDS = 64

LENGTHS_SUFFIX = [17, 31, 73, 47, 23]

skip_size = 0
current_position = 0

total_score = 0
total_in_garbage = 0

real_list = [x for x in range(256)]
cl = CircularList(real_list)

with open("input.txt", "rb") as input_file:
    line = input_file.read()[:-1]
    lengths = [c for c in line]
    lengths.extend(LENGTHS_SUFFIX)

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

print(sparse_hashes)
answer = "".join([format(sh, '02x') for sh in sparse_hashes])
print(f'Part 2 answer: {answer}')

