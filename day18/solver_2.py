from collections import defaultdict, deque
import operator

def parse_instr(instr):
    tokens = instr.split(" ")
    if len(tokens) < 3:
        return (*tokens, None)
    else:
        return tokens

class VirtualMachine:
    def __init__(self, instrs, pid, input_queue, output_queue):
        self.pid = pid
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.instrs = instrs
        self.regs = defaultdict(int)
        self.pc = 0
        self.regs['p'] = pid
        self.times_sent = 0
        self.blocked = False

    def print_registers(self):
        print("***Registers***")
        for reg, val in self.regs.items():
            print(f"{reg}: {val}")

    def run(self):
        self.blocked = False
        while self.pc < len(self.instrs) and not self.blocked:
            inst = self.instrs[self.pc]
            getattr(self, inst[0])(inst[1], inst[2])

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
        r1 = self.get_r(r1)
        print(f"SEND: {self.pid}: {r1}")
        self.output_queue.appendleft(r1)
        self.pc += 1
        self.times_sent += 1

    def mul(self, r1, r2):
        self.compute(r1, r2, operator.mul)
        self.pc += 1

    def mod(self, r1, r2):
        self.compute(r1, r2, operator.mod)
        self.pc += 1

    def rcv(self, r1, r2):
        print(f"RCV: {self.pid}: {len(self.input_queue)}")
        try:
            self.regs[r1] = self.input_queue.pop()
            self.blocked = False
            self.pc += 1
        except IndexError:
            self.blocked = True

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
vm0_input = deque()
vm1_input = deque()
vm0 = VirtualMachine(instrs, 0, vm0_input, vm1_input)
vm1 = VirtualMachine(instrs, 1, vm1_input, vm0_input)
while True:
    vm0.run()
    vm1.run()
    # If neither vm is blocked then they are both done running
    if not vm0.blocked and not vm1.blocked:
        break
    # If both vms are blocked and neither has input to process, then they are both done running
    if (vm0.blocked and vm1.blocked) and (not vm0_input and not vm1_input):
        break
print(f'Part 2 answer: {vm1.times_sent}')

