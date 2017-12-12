right = (1, 0)
up = (0, 1)
left = (-1, 0)
down = (0, -1)
move_order = (right, up, left, down)

def get_direction():
    next_move_index = 0
    counter = 0
    counter_limit = 1
    increment_limit = 0
    while True:
        counter += 1
        if increment_limit == 2:
            increment_limit = 0
            counter_limit += 1
        if counter > counter_limit:
            counter = 1
            increment_limit += 1
            next_move_index += 1
        move = move_order[next_move_index % 4]
        yield move

direction_getter = get_direction()

number = 0
answer = 0
position = (0, 0)
spiral = {}
indexes = {}

with open("input.txt") as input_file:
    line = input_file.readline()
    number = int(line.strip())

for i in range(1, number+1):
    spiral[position] = i
    indexes[i] = position
    move = next(direction_getter)
    position = (position[0] + move[0], position[1] + move[1])

location = indexes[number]
print(location)

print(f'Part 1 answer: {location[0] + location[1]}')
