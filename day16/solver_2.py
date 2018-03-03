orig_programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

def evaluate(instr, programs):
    new_programs = []
    i = instr[0]
    if i == 's':
        size = int(instr[1:])
        e = len(programs)
        s = e - size
        new_programs = programs[s:e] + programs[:s]
    if i == 'x':
        instr = instr[1:]
        a, b = instr.split("/")
        a = int(a)
        b = int(b)
        new_programs = programs
        new_programs[a], new_programs[b] = programs[b], programs[a]
    if i == 'p':
        a = instr[1]
        b = instr[3]
        a_index = programs.index(a)
        b_index = programs.index(b)
        new_programs = programs
        new_programs[a_index], new_programs[b_index] = programs[b_index], programs[a_index]

    return new_programs


with open("input.txt", "r") as input_file:
    line = input_file.readline()
    line = line.strip()
    instructions = line.split(',')

# The key insight is to look for loops. The same instructions are run each time,
# so if the programs are in the same order, you know the output will be the same.
# Find the period of repetition and use that with the total number of runs to determine
# the offset. Then just find the result of running that offset to get the answer.
NUM_RUNS = 1000000000
for x in range(NUM_RUNS):
    run = x+1
    for instr in instructions:
        programs = evaluate(instr, programs)
    if programs == orig_programs:
        print(f"Loop detected after {run} runs.")
        break

offset = NUM_RUNS % run
print(f"Offset: {offset}")
for x in range(offset):
    run = x+1
    for instr in instructions:
        programs = evaluate(instr, programs)

order = "".join(programs)
print(f'Part 2 answer: {order}')
