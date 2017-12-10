
steps = 0
part2_steps = 0
jumps = []

with open("input.txt") as input_file:
    for line in input_file.readlines():
        jumps.append(int(line.strip()))

part2_jumps = jumps.copy()

end = len(jumps)
index = 0

while index < end and index >= 0:
    steps += 1
    step = jumps[index]
    jumps[index] += 1
    index += step

print(f'Part 1 answer: {steps}')

index = 0
while index < end and index >= 0:
    part2_steps += 1
    step = part2_jumps[index]
    if step >= 3:
        part2_jumps[index] -= 1
    else:
        part2_jumps[index] += 1
    index += step

print(f'Part 2 answer: {part2_steps}')
