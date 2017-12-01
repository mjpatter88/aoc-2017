
answer = 0
num = ""

with open("input.txt") as input_file:
    for line in input_file:
        num = line
        num = num + num[0]

for index, digit in enumerate(num[:-1]):
    if digit == num[index+1]:
        answer += int(digit)

print(answer)
