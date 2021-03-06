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
# value after zero....

# IDEA: rather than store an array at all for part two, lets just calc all the indexes and only store
# the entries that would happen at index 0. The last value that would be entered at that index is the answer...

# Enhancement: you can skip chunks at a time. One you calculate a cursor, you can figure out how many
# spots are between you and the end of the list. You know how many steps each turn takes, so any jumps until you
# would pass the end you can just skip. This saves lots of mods which are the expensive op.


num_steps_per_turn = 377
num_turns = 50000001
answer = -1
cursor = 0

x = 1
while x < num_turns:
    size = x
    if x % 500000 == 0:
        print(x)
    cursor = (cursor + num_steps_per_turn) % size + 1
    if cursor == 1:
        answer = x
        print(x)
    num_skips = int((size - cursor) / num_steps_per_turn)
    x += num_skips + 1
    cursor += num_skips * (num_steps_per_turn + 1)

print(f'Part 2 answer: {answer}')
