from solver import Rule

test_2x2_row = "../.# => ##./#../..."
test_3x3_row = ".#./..#/### => #..#/..../..../#..#"

def test_rule_init_2x2_creates_output():
    r = Rule(test_2x2_row)
    assert r.output == [
        ['#', '#', '.'],
        ['#', '.', '.'],
        ['.', '.', '.']
    ]

def test_rule_init_3x3_creates_output():
    r = Rule(test_3x3_row)
    assert r.output == [
        ['#', '.', '.', '#'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['#', '.', '.', '#']
    ]

def test_rule_init_2x2_creates_first_input():
    r = Rule(test_2x2_row)
    expected_input = [
        ['.', '.'],
        ['.', '#']
    ]
    assert expected_input in r.inputs

def test_rule_init_2x2_creates_input_flipped_horizontally():
    r = Rule(test_2x2_row)
    expected_input = [
        ['.', '.'],
        ['#', '.']
    ]
    assert expected_input in r.inputs

def test_rule_init_2x2_creates_input_flipped_vertically():
    r = Rule(test_2x2_row)
    expected_input = [
        ['.', '#'],
        ['.', '.']
    ]
    assert expected_input in r.inputs

def test_rule_init_2x2_creates_input_rotated_90():
    r = Rule(test_2x2_row)
    expected_input = [
        ['.', '.'],
        ['#', '.']
    ]
    assert expected_input in r.inputs

def test_rule_init_2x2_creates_input_rotated_180():
    r = Rule(test_2x2_row)
    expected_input = [
        ['#', '.'],
        ['.', '.']
    ]
    assert expected_input in r.inputs

def test_rule_init_2x2_creates_input_rotated_270():
    r = Rule(test_2x2_row)
    expected_input = [
        ['.', '#'],
        ['.', '.']
    ]
    assert expected_input in r.inputs

################################ 3x3 ########################

def test_rule_init_3x3_creates_first_input():
    r = Rule(test_3x3_row)
    expected_input = [
        ['.', '#', '.'],
        ['.', '.', '#'],
        ['#', '#', '#']
    ]
    assert expected_input in r.inputs

def test_rule_init_3x3_creates_input_flipped_horizontally():
    r = Rule(test_3x3_row)
    expected_input = [
        ['.', '#', '.'],
        ['#', '.', '.'],
        ['#', '#', '#']
    ]
    assert expected_input in r.inputs

def test_rule_init_3x3_creates_input_flipped_vertically():
    r = Rule(test_3x3_row)
    expected_input = [
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['.', '#', '.']
    ]
    assert expected_input in r.inputs

def test_rule_init_3x3_creates_input_rotated_90():
    r = Rule(test_3x3_row)
    expected_input = [
        ['#', '.', '.'],
        ['#', '.', '#'],
        ['#', '#', '.']
    ]
    assert expected_input in r.inputs

def test_rule_init_3x3_creates_input_rotated_180():
    r = Rule(test_3x3_row)
    expected_input = [
        ['#', '#', '#'],
        ['#', '.', '.'],
        ['.', '#', '.']
    ]
    assert expected_input in r.inputs

def test_rule_init_3x3_creates_input_rotated_270():
    r = Rule(test_3x3_row)
    expected_input = [
        ['.', '#', '#'],
        ['#', '.', '#'],
        ['.', '.', '#']
    ]
    assert expected_input in r.inputs

