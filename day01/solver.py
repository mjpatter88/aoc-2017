part1_answer = 0
part2_answer = 0
num = ""

with open("input.txt") as input_file:
    num = input_file.readline()

class CircularQueue:
    def __init__(self, vals):
        self.data = vals

    def __getitem__(self, index):
        return self.data[index % len(self.data)]

cq = CircularQueue(num)
length = len(num)

for index, digit in enumerate(num):
    if digit == cq[index+1]:
        part1_answer += int(digit)

    if digit == cq[index + int(length/2)]:
        part2_answer += int(digit)

print(f'Part 1 part1_answer: {part1_answer}')
print(f'Part 2 part2_answer: {part2_answer}')

