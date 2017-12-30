from collections import defaultdict
from collections import deque

group = defaultdict(set)

with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.strip()
        left, right = line.split(" <-> ")
        right = right.split(", ")
        group[left] = right

conns = set()
q = deque()
connections = group["0"]
q.extendleft(connections)

while len(q) > 0:
    connection = q.popleft()
    if connection not in conns:
        conns.add(connection)
        q.extendleft(group[connection])

ans2 = 0
print(f'Part 1 answer: {len(conns)}')
print(f'Part 2 answer: {ans2}')

