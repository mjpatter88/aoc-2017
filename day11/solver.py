def evaluate(step):
    if step == "n":
        return 1, 0
    if step =="s":
        return -1, 0

    n, e = 0, 0
    if "n" in step:
        n = 0.5
    if "s" in step:
        n = -0.5
    if "e" in step:
        e = 0.5
    if "w" in step:
        e = -0.5

    return n, e

def how_far_away(steps):
    n, e = 0, 0
    for step in steps:
        n_inc, e_inc = evaluate(step)
        n += n_inc
        e += e_inc
    return abs(n) + abs(e)

with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        steps = line.split(",")
        print(steps)
        dist = how_far_away(steps)
        print(dist)

print(f'Part 1 answer: {dist}')

