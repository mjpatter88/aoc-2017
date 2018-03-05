num_steps_per_turn = 377
# num_steps_per_turn = 3
num_turns = 2018
# num_turns = 10

class CircularBuffer:
    def __init__(self, num_steps_per_turn):
        self.num_steps_per_turn = num_steps_per_turn
        self.buff = [0]
        self.cursor = 0

    def insert(self, value):
        self.cursor = (self.cursor + num_steps_per_turn) % len(self.buff) + 1
        self.buff.insert(self.cursor, value)

cb = CircularBuffer(num_steps_per_turn)

for x in range(1, num_turns):
    cb.insert(x)

print(f'Part 1 answer: {cb.buff[cb.cursor+1]}')
