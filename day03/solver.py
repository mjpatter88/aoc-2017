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
spiral_2 = {}
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

def get_sum_adj_squares(pos, spiral):
    left = (pos[0] - 1, pos[1])
    bot_left = (pos[0] - 1, pos[1] - 1)
    bot = (pos[0], pos[1] - 1)
    bot_right = (pos[0] + 1, pos[1] - 1)
    right = (pos[0] + 1, pos[1])
    top_right = (pos[0] + 1, pos[1] + 1)
    top = (pos[0], pos[1] + 1)
    top_left = (pos[0] - 1, pos[1] + 1)
    locs = (left, bot_left, bot, bot_right, right, top_right, top, top_left)

    total = sum(spiral.get(position, 0) for position in locs)
    return total


value = 0
spiral_2[(0,0)] = 1
position = (0, 0)

direction_getter = get_direction()
move = next(direction_getter)
position = (position[0] + move[0], position[1] + move[1])

while True:
    value = get_sum_adj_squares(position, spiral_2)
    spiral_2[position] = value
    indexes[i] = position
    move = next(direction_getter)
    position = (position[0] + move[0], position[1] + move[1])
    if value > number:
        break

print(f'Part 2 answer: {value}')
