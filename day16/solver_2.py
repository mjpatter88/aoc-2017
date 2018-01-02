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

NUM_RUNS = 1000000000
for x in range(NUM_RUNS):
    for instr in instructions:
        programs = evaluate(instr, programs)
    print(x)

order = "".join(programs)
print(f'Part 2 answer: {order}')
