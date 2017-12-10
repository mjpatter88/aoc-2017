
steps = 0
jumps = []

with open("input.txt") as input_file:
    for line in input_file.readlines():
        jumps.append(int(line.strip()))

end = len(jumps)
index = 0

while index < end and index >= 0:
    steps += 1
    next_index = index + jumps[index]
    jumps[index] += 1
    index = next_index

print(f'Part 1 answer: {steps}')
