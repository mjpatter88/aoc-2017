from collections import defaultdict
from collections import deque

group = defaultdict(set)

def get_program(prog_id):
    conns = set()
    q = deque()
    connections = group[prog_id]
    q.extendleft(connections)

    while len(q) > 0:
        connection = q.popleft()
        if connection not in conns:
            conns.add(connection)
            q.extendleft(group[connection])
    return conns

with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        left, right = line.split(" <-> ")
        right = right.split(", ")
        group[left] = right

first_id = "0"
conns = get_program(first_id)
print(f'Part 1 answer: {len(conns)}')
num_groups = 1

while len(conns) != len(group.keys()):
    new_progs = group.keys() - conns
    new_prog = new_progs.pop()
    conns |= get_program(new_prog)
    num_groups += 1

print(f'Part 2 answer: {num_groups}')

