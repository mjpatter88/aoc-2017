from solver import create_grid_from_pieces, divide_grid


def test_grid_divides():
    art = [
        ['#', '.', '.', '#'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['#', '.', '.', '#']
    ]
    grid1 = [
        ['#', '.'],
        ['.', '.']
    ]
    grid2 = [
        ['.', '#'],
        ['.', '.']
    ]
    grid3 = [
        ['.', '.'],
        ['#', '.']
    ]
    grid4 = [
        ['.', '.'],
        ['.', '#']
    ]
    assert divide_grid(art) == [grid1, grid2, grid3, grid4]

def test_create_grid_from__3x3_pieces():
#    ##.|##.
#    #..|#..
#    ...|...
#    ---+---
#    ##.|##.
#    #..|#..
#    ...|...
    pieces = [
        [['#', '#', '.'], ['#', '.', '.'], ['.', '.', '.']],
        [['#', '#', '.'], ['#', '.', '.'], ['.', '.', '.']],
        [['#', '#', '.'], ['#', '.', '.'], ['.', '.', '.']],
        [['#', '#', '.'], ['#', '.', '.'], ['.', '.', '.']]
    ]
    expected = [
        ['#', '#', '.', '#', '#', '.'],
        ['#', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['#', '#', '.', '#', '#', '.'],
        ['#', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
    assert create_grid_from_pieces(pieces) == expected

def test_create_grid_from__4x4_pieces():
#    ##.#|##..
#    #...|#...
#    ....|....
#    ----+----
#    ##..|##..
#    #...|#...
#    ....|....
    pieces = [
        [['#', '#', '.', '#'], ['#', '.', '.', '.'], ['.', '.', '.', '.']],
        [['#', '#', '.', '.'], ['#', '.', '.', '.'], ['.', '.', '.', '.']],
        [['#', '#', '.', '.'], ['#', '.', '.', '.'], ['.', '.', '.', '.']],
        [['#', '#', '.', '.'], ['#', '.', '.', '.'], ['.', '.', '.', '.']]
    ]
    expected = [
        ['#', '#', '.', '#', '#', '#', '.', '.'],
        ['#', '.', '.', '.', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['#', '#', '.', '.', '#', '#', '.', '.'],
        ['#', '.', '.', '.', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]
    assert create_grid_from_pieces(pieces) == expected
