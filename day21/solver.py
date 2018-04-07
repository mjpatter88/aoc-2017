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
    length = len(grid)
    assert length % 2 == 0 or length % 3 ==0
    if length == 2 or length == 3:
        return grid



    if length % 2 == 0:
        return divide_grid_by(grid, 2)
    else:
        return divide_grid_by(grid, 3)

def divide_grid_by(grid, jump):
    # 4x4 grid -> 4 divs
    # 6x6 grid -> 9 divs
    # (half one dimension) ^ 2 -> # grids
    dim = len(grid)
    grids = []

    row_index = 0
    while row_index < dim:
        col_index = 0
        grids_in_row = []
        while col_index < dim:
            new_grid = [row[col_index:col_index + jump] for row in grid[row_index:row_index + jump]]
            grids_in_row.append(new_grid)
            col_index += jump
        grids.append(grids_in_row)
        row_index += jump
    return grids


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

class Solver:
    def __init__(self):
        self.master_grid = [
            ['.', '#', '.'],
            ['.', '.', '#'],
            ['#', '#', '#']
        ]

        self.rules = []
        with open("test_input.txt") as inp:
            for line in inp:
                self.rules.append(Rule(line))


    def step(self):
        if len(self.master_grid) % 2 == 0:
            print("\tDivisable by 2, dividing...")
            grids = divide_grid(self.master_grid)
            print("\t", end="")
            print(grids)
        else:
            grids = [self.master_grid]
        new_grids = []
        for grid in grids:
            for rule in self.rules:
                if rule.match(grid):
                    new_grids.append(rule.output)
                    break
        self.master_grid = create_grid_from_pieces(new_grids)


if __name__ == '__main__':
    solver = Solver()

    for i in range(NUM_ROUNDS):
        print(f"Round {i}: Starting")
        print(solver.master_grid)
        solver.step()
        print(f"Round {i}: Complete")
        print(solver.master_grid)
        print()

# print(f'Part 1 answer: {min_index}')
# print(f'Part 2 answer: {len(particles)}')

# 1) Parse input into rules
# 2) Generate all permutations of input for each rule
# 3) Match grid state to rule
# 4) Transform grid state

# 5) Handle splitting of grid 
#    (Always have one "master" grid but split off others that are references to part of it?)
