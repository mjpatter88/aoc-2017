
num_lines = 0
invalid = 0
invalid_2 = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        words = line.split()
        num_lines += 1
        sorted_words = ["".join(sorted(word)) for word in words]

        if len(words) != len(set(words)):
            invalid += 1
            invalid_2 += 1

        elif len(sorted_words) != len(set(sorted_words)):
            invalid_2 += 1


valid = num_lines - invalid
valid_2 = num_lines - invalid_2
print(f'Part 1 answer: {valid}')
print(f'Part 2 answer: {valid_2}')
