
class ProcessingMachine():
    def __init__(self):
        self.inside_garbage = False
        self.ignore_next = False
        self.line = []
        self.garbage = []
        self.level = 0
        self.score = 0

    def step(self, char):
        if self.ignore_next:
            self.ignore_next = False
            return

        if self.inside_garbage:
            if char == '!':
                self.ignore_next = True
            elif char != '>': # Don't count closing of garbage as garbage
                self.garbage.append(char)

        if char == '<':
            self.inside_garbage = True
            return

        if self.inside_garbage and char == '>':
            self.inside_garbage = False
            return

        if not self.inside_garbage:
            if char == '{':
                self.level += 1
            if char == '}':
                self.score += self.level
                self.level -= 1
            self.line.append(char)

    def get_line(self):
        return ''.join(self.line)

lines = []
total_score = 0
total_in_garbage = 0
with open("input.txt") as input_file:
    for line in input_file.readlines():
        pm = ProcessingMachine()
        line = line.strip()
    #line = input_file.readline().strip()
        for c in line:
            pm.step(c)
        print(pm.score)
        total_score += pm.score
        total_in_garbage += len(pm.garbage)
        lines.append(pm.get_line())


print(f'Part 1 answer: {total_score}')
print(f'Part 2 answer: {total_in_garbage}')


