
left = []
right = []

with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        c_right = None
        c_left = line
        if "->" in line:
            c_left, c_right = line.split("->")
            c_right = c_right.strip()

        if c_right:
            right.extend([r.strip() for r in c_right.split(",")])
        left.append(c_left.split()[0])

answer = set(left) - set(right)

print(f'Part 1 answer: {answer}')
