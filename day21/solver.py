import math
NUM_ROUNDS = 2


class Rule:
    def __init__(self, row):
        inp, outp = row.split(" => ")
        first = self.parse_input(inp)
        self.inputs = self.generate_all_input_matches(first)
        self.output = self.parse_output(outp)

    def parse_output(self, string):
        return [list(s.strip()) for s in string.split("/")]

    def parse_input(self, string):
        return [list(s.strip()) for s in string.split("/")]

    def generate_all_input_matches(self, first):
        horiz = self.flip_horiz(first)
        vert = self.flip_vert(first)
        r90 = self.rotate_90(first)
        r180 = self.rotate_90(r90)
        r270 = self.rotate_90(r180)
        return [first, horiz, vert, r90, r180, r270]

    def flip_horiz(self, matrix):
        return [list(reversed(row)) for row in matrix]

    def flip_vert(self, matrix):
        return list(reversed(matrix))

    def rotate_90(self, matrix):
        rot = list(zip(*matrix[::-1]))
        return [list(l) for l in rot]

    def match(self, grid):
        return grid in self.inputs



def divide_grid(grid):
        assert len(grid) % 2 == 0
        div = int(len(grid)/2)
        grid1 = [row[:div] for row in grid[:div]]
        grid2 = [row[div:] for row in grid[:div]]
        grid3 = [row[:div] for row in grid[div:]]
        grid4 = [row[div:] for row in grid[div:]]
        return [grid1, grid2, grid3, grid4]

def create_grid_from_pieces(pieces):
    if len(pieces) == 1:
        return pieces[0]
    return [
        pieces[0][0] + pieces[1][0],
        pieces[0][1] + pieces[1][1],
        pieces[0][2] + pieces[1][2],
        pieces[2][0] + pieces[3][0],
        pieces[2][1] + pieces[3][1],
        pieces[2][2] + pieces[3][2]
    ]


if __name__ == '__main__':
    master_grid = [
        ['.', '#', '.'],
        ['.', '.', '#'],
        ['#', '#', '#']
    ]

    rules = []
    with open("test_input.txt") as inp:
        for line in inp:
            rules.append(Rule(line))

    print("************** Starting ****************")
    print(master_grid)
    for i in range(NUM_ROUNDS):
        if len(master_grid) % 2 == 0:
            print("Divisable by 2, dividing...")
            grids = divide_grid(master_grid)
            print(grids)
        else:
            grids = [master_grid]
        new_grids = []
        for grid in grids:
            for rule in rules:
                if rule.match(grid):
                    new_grids.append(rule.output)
                    break
        master_grid = create_grid_from_pieces(new_grids)
        print("MASTER")
        print(master_grid)
# print(f'Part 1 answer: {min_index}')
# print(f'Part 2 answer: {len(particles)}')

# 1) Parse input into rules
# 2) Generate all permutations of input for each rule

# 3) Match grid state to rule
# 4) Transform grid state
# 5) Handle splitting of grid 
#    (Always have one "master" grid but split off others that are references to part of it?)
