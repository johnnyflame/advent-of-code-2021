import textwrap

from src.day9 import part_1, part_2

test_data = textwrap.dedent(
    """
2199943210
3987894921
9856789892
8767896789
9899965678"""
).lstrip()


def test_part_1():
    assert part_1(test_data) == 15


def test_part_2():
    assert part_2(test_data) == 1134
