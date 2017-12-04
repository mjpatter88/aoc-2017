from itertools import combinations

checksum1 = 0
checksum2 = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        nums = [int(n) for n in line.split()]
        checksum1 += (max(nums) - min(nums))
        for a, b in combinations(nums, 2):
            div = max(a, b) / min(a, b)
            if int(div) == div:
                checksum2 += int(div)


print(f'Part 1 answer: {checksum1}')
print(f'Part 2 answer: {checksum2}')
