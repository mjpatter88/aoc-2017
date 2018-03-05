num_steps_per_turn = 377
num_turns = 2018

class CircularBuffer:
    def __init__(self, num_steps_per_turn, num_turns):
        self.num_steps_per_turn = num_steps_per_turn
        self.buff = [''] * num_turns
        self.buff[0] = 0
        self.cursor = 0
        self.size = 1

    def insert(self, value):
        self.cursor = (self.cursor + num_steps_per_turn) % self.size + 1
        self.buff[self.cursor] = value
        self.size += 1

cb = CircularBuffer(num_steps_per_turn, num_turns)

for x in range(1, num_turns):
    cb.insert(x)

print(f'Part 1 answer: {cb.buff[cb.cursor+1]}')

# Key insight: the insertion into the array used in part 1 is way too slow. As the array grows,
# more and more numbers need to be shifted on a single insert. A linked list might help, but as
# the array grows the search to get to the right index would be slow.
# Instead, let's create the whole array first, then the insert becomes fast.
# This provides the right answer, but as I think through it, it shouldn't work. It's actually
# replacing values rather than pushing them down. It only works since we are just looking for the
# value after zero.

num_steps_per_turn = 377
num_turns = 50000001

cb = CircularBuffer(num_steps_per_turn, num_turns)

for x in range(1, num_turns):
    cb.insert(x)
    if x % 500000 == 0:
        print(x)

answer = -1
for ind, x in enumerate(cb.buff):
    if x == 0:
        answer = cb.buff[ind+1]
        break

print(f'Part 2 answer: {answer}')
