from collections import defaultdict
registers = defaultdict(int)
instructions = []

class Instruction():
    def __init__(self, reg_a, instr, val_a, reg_b, comp, val_b):
        self.reg_a = reg_a
        self.instr = instr
        self.val_a = val_a
        self.reg_b = reg_b
        self.comp = comp
        self.val_b = val_b

    def __repr__(self):
        return f'"{self.reg_a} {self.instr} {self.val_a} {self.reg_b} {self.comp} {self.val_b}"'

    def evaluate(self, registers):
        reg = registers[self.reg_b]
        if eval(f'{reg} {self.comp} {self.val_b}'):
            if self.instr == "inc":
                registers[self.reg_a] += self.val_a
            else:
                registers[self.reg_a] -= self.val_a

def parse(line):
    reg_a, instr, val_a, _, reg_b, comp, val_b = line.split()

    instruction = Instruction(reg_a, instr, int(val_a), reg_b, comp, int(val_b))
    return instruction

with open("input.txt") as input_file:
    for line in input_file.readlines():
        instructions.append(parse(line))

for instr in instructions:
    instr.evaluate(registers)

largest = max(registers.values())
print(f'Part 1 answer: {largest}')


