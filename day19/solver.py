rows = []
movement = {
    "DOWN": (1, 0),
    "RIGHT": (0, 1),
    "LEFT": (0, -1),
    "UP": (-1, 0),
}
# if going down, it can't change to up or down, so check left and then right
# if going right, it won't be left or right, so check up and down
possible_changes = {
    "DOWN": ["LEFT", "RIGHT"],
    "UP": ["LEFT", "RIGHT"],
    "RIGHT": ["UP", "DOWN"],
    "LEFT": ["UP", "DOWN"],
}

path_char_for_dir = {
    "DOWN": '|',
    "UP": '|',
    "RIGHT": '-',
    "LEFT": '-',
}

class GameOverException(Exception):
    pass

class Network:
    def __init__(self, rows):
        self.rows = rows
        self.direction = "DOWN"
        self.visited = []
        self.location = self.find_starting_location()

    def step(self):
        self.move()
        self.update_direction()

    def find_starting_location(self):
        col = self.rows[0].index('|')
        return (0, col)

    def move(self):
        self.location = self.location[0] + movement[self.direction][0], self.location[1] + movement[self.direction][1]

        cur_char = self.current_character()
        if cur_char == ' ':
            raise GameOverException
        elif cur_char.isalpha():
            self.visited.append(cur_char)

    def update_direction(self):
        if self.current_character() != '+':
            return
        possible_directions = possible_changes[self.direction]
        for direction in possible_directions:
            next_pos = self.location[0] + movement[direction][0], self.location[1] + movement[direction][1]
            if self.rows[next_pos[0]][next_pos[1]] == path_char_for_dir[direction] or self.rows[next_pos[0]][next_pos[1]].isalpha():
                self.direction = direction
                break

    def current_character(self):
        return self.rows[self.location[0]][self.location[1]]

with open("input.txt") as inp:
    for line in inp:
        rows.append(line)
# Append a final row
# row_len = len(rows[0])
# rows.append([' '] * row_len)

network = Network(rows)
while True:
    try:
        network.step()
    except GameOverException:
        break

print(f'Part 1 answer: {"".join(network.visited)}')

