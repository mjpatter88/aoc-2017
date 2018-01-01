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

binary_map = []
num_ones = 0
for h in hashes:
    row = []
    for c in h:
        binary = bin(int(c, 16))[2:] # We just want the 1s and 0s
        binary = binary.zfill(4)
        row.extend(binary)
        num_ones += binary.count('1')
    binary_map.append(row)

print(f'Part 1 answer: {num_ones}')

used_marker = 'x'
region_map = []
for row in binary_map:
    new_row = ['x' if r =='1' else 'o' for r in row]
    region_map.append(new_row)

def map_region(row_index, col_index, region_map, region_num):
    region_map[row_index][col_index] = str(region_num)

    # left
    if col_index > 0 and region_map[row_index][col_index-1] == used_marker:
        map_region(row_index, col_index-1, region_map, region_num)

    # right
    if col_index < 127 and region_map[row_index][col_index+1] == used_marker:
        map_region(row_index, col_index+1, region_map, region_num)

    # top
    if row_index > 0 and region_map[row_index-1][col_index] == used_marker:
        map_region(row_index-1, col_index, region_map, region_num)

    # bottom
    if row_index < 127 and region_map[row_index+1][col_index] == used_marker:
        map_region(row_index+1, col_index, region_map, region_num)

# Walk through row by row. If an x is encountered, replace it with the currrent region number and trace all adjacent xs
# Then increment region number and restart
current_region_num = 1
start_over = False
while True:
    for row_i, row in enumerate(region_map):
        for col_i, c in enumerate(row):
            if c == used_marker:
                map_region(row_i, col_i, region_map, current_region_num)
                current_region_num += 1
                start_over = True
                break
        if start_over:
            break
    if not start_over:
        break
    if start_over:
        start_over = False
# TODO: fix this terrible start_over logic

# for row in region_map:
#    print("".join(r for r in row))

print(f'Part 2 answer: {current_region_num-1}')
