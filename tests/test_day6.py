from src.day6 import part1, part_2

test_data = [int(x) for x in "3,4,3,1,2".split(",")]


def test_part1():
    assert part1(test_data, days=80) == 5934


def test_part2():
    assert part_2(test_data, days=18) == 26
