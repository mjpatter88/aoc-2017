
steps = 0
loop_len = 0
banks = []
cache = {}

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
    cache[",".join(map(str, banks))] = steps

    blocks = max(banks)
    max_index = banks.index(blocks)
    banks[max_index] = 0
    distribute_blocks(max_index+1, blocks)

    steps += 1
    cache_entry = ",".join(map(str, banks))
    if cache_entry in cache:
        repeat = True

loop_len = steps - cache[cache_entry]

print(f'Part 1 answer: {steps}')
print(f'Part 2 answer: {loop_len}')
