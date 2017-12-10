
steps = 0
banks = []
cache = []

def distribute_blocks(starting_index, num_blocks):
    index = starting_index
    end = len(banks)
    while num_blocks > 0:
        if index >= end:
            index = 0
        banks[index] += 1
        num_blocks -= 1

        index += 1

with open("input.txt") as input_file:
    line = input_file.readline()
    banks = line.split()
    banks = [int(bank) for bank in banks]

repeat = False
while not repeat:
    cache.append(",".join(map(str, banks)))

    blocks = max(banks)
    max_index = banks.index(blocks)
    banks[max_index] = 0
    distribute_blocks(max_index+1, blocks)

    steps += 1
    if ",".join(map(str, banks)) in cache:
        repeat = True

print(f'Part 1 answer: {steps}')
