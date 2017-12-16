class Node():
    def __init__(self, name, weight, children_names):
        self.name = name
        self.weight = weight
        self.children = []
        self.children_names = children_names

    def get_weight(self):
        return self.weight + sum(c.get_weight() for c in self.children)

    def __repr__(self):
        return f'{self.name}:{self.weight} -> {self.children_names}'

def parse_line(line):
    line = line.strip()
    right = []
    c_right = None
    c_left = line
    if "->" in line:
        c_left, c_right = line.split("->")
        c_right = c_right.strip()

    if c_right:
        right = [r.strip() for r in c_right.split(",")]
    left, weight = c_left.split()
    weight = int(weight.strip("(").strip(")"))

    return left, weight, right

def find_node(name, nodes):
    return [n for n in nodes if n.name == name][0]

def attach_children(node, nodes):
    for child_name in node.children_names:
        c = find_node(child_name, nodes)
        node.children.append(c)

def traverse_node(node, q, level):
    spacing = '\t' * level
    print(spacing, end='')
    weight = node.get_weight()
    for child in node.children:
        q.append((child, level+1))
    print(node)
    print(spacing, end='')
    print(weight)

def traverse_graph(root, q):
    level = 0
    weight = root.get_weight()
    for child in root.children:
        q.append((child, level+1))
    print(root)
    print(weight)
    while q:
        n = q.popleft()
        traverse_node(n[0], q, n[1])
    print("here")
    print(q)


left = []
right = []
graph = []

with open("input.txt") as input_file:
    for line in input_file.readlines():
        l, w, r = parse_line(line)
        left.append(l)
        right.extend(r)
        node = Node(l, w, r)
        graph.append(node)

for node in graph:
    attach_children(node, graph)

root_name = (set(left) - set(right)).pop()
print(f'Part 1 answer: {root_name}')

from collections import deque
q = deque()
traverse_graph(find_node(root_name, graph), q)

