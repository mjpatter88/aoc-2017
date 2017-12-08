
valid = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        words = line.split()
        if len(words) == len(set(words)):
            valid += 1

print(f'Part 1 answer: {valid}')
