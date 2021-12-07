from src.day7 import part_1, part_2

test_input = "16,1,2,0,4,2,7,1,2,14"


def test_part_1():
    assert part_1(test_input) == 37


def test_part_2():
    assert part_2(test_input) == 168
