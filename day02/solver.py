checksum = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        nums = [int(n) for n in line.split()]
        smallest = min(nums)
        largest = max(nums)
        checksum += (largest - smallest)

print(f'Part 1 answer: {checksum}')
