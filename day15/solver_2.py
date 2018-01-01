FILTER = int("0xFFFF", 0)
A_FACTOR = 16807
B_FACTOR = 48271
DIVISOR = 2147483647
NUM_PAIRS = 5000000

a_starting = 0
b_starting = 0

with open("input.txt", "r") as input_file:
    a_starting = input_file.readline().split()[-1]
    b_starting = input_file.readline().split()[-1]

a = int(a_starting)
b = int(b_starting)

num_matching = 0
for x in range(NUM_PAIRS):
    while True:
        a = (a * A_FACTOR) % DIVISOR
        if (a % 4) == 0:
            break
    while True:
        b = (b * B_FACTOR) % DIVISOR
        if (b % 8) == 0:
            break
    if (a & FILTER) == (b & FILTER):
        num_matching += 1
    if x % 100000 == 0:
        print(x)


print(f'Part 2 answer: {num_matching}')
