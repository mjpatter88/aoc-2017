from collections import defaultdict
import operator

def parse_instr(instr):
    tokens = instr.split(" ")
    if len(tokens) < 3:
        return (*tokens, None)
    else:
        return tokens

class VirtualMachine:
    def __init__(self, instrs):
        self.instrs = instrs
        self.regs = defaultdict(int)
        self.last_freq = None
        self.pc = 0

    def print_registers(self):
        print("***Registers***")
        for reg, val in self.regs.items():
            print(f"{reg}: {val}")

    def run(self):
        while self.pc < len(self.instrs):
            inst = self.instrs[self.pc]
            getattr(vm, inst[0])(inst[1], inst[2])

    def get_r(self, r2):
        try:
            r2 = int(r2)
        except:
            r2 = self.regs[r2]
        return r2

    def compute(self, r1, r2, operation):
        r2 = self.get_r(r2)
        self.regs[r1] = operation(self.regs[r1], r2)

    def set(self, r1, r2):
        r2 = self.get_r(r2)
        self.regs[r1] = r2
        self.pc += 1

    def add(self, r1, r2):
        self.compute(r1, r2, operator.add)
        self.pc += 1

    def snd(self, r1, r2):
        self.last_freq = self.regs[r1]
        self.pc += 1

    def mul(self, r1, r2):
        self.compute(r1, r2, operator.mul)
        self.pc += 1

    def mod(self, r1, r2):
        self.compute(r1, r2, operator.mod)
        self.pc += 1

    def rcv(self, r1, r2):
        r1 = self.get_r(r1)
        if r1 != 0:
            print("*** RCV ***")
            print(self.last_freq)
            self.stop_running()
        self.pc += 1

    def jgz(self, r1, r2):
        r1 = self.get_r(r1)
        r2 = self.get_r(r2)
        if r1 > 0:
            self.pc += int(r2)
        else:
            self.pc += 1

    def stop_running(self):
        self.pc = len(self.instrs)


with open("input.txt") as inp:
    instrs = list(map(str.strip, inp.readlines()))

instrs = [parse_instr(inst) for inst in instrs]
vm = VirtualMachine(instrs)
vm.run()
vm.print_registers()
print(f'Part 1 answer: {vm.last_freq}')

