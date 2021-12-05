import textwrap

from src.day5 import Coordinate, expand_source_dest, part_1, part_2

test_data = textwrap.dedent(
    """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
).lstrip("\n")


def test_part_1():
    assert part_1(test_data) == 5


def test_part_2():
    assert part_2(test_data) == 12


def test_expand_source_dest():
    source = Coordinate(1, 1)
    dest = Coordinate(3, 3)

    assert expand_source_dest(source, dest) == [
        Coordinate(1, 1),
        Coordinate(2, 2),
        Coordinate(3, 3),
    ]


def test_expand_source_dest_2():
    source = Coordinate(9, 7)
    dest = Coordinate(7, 9)

    assert expand_source_dest(source, dest) == [
        Coordinate(9, 7),
        Coordinate(8, 8),
        Coordinate(7, 9),
    ]


def test_bottom_right_to_top_left():
    source = Coordinate(3, 3)
    dest = Coordinate(1, 1)

    assert expand_source_dest(source, dest) == [
        Coordinate(3, 3),
        Coordinate(2, 2),
        Coordinate(1, 1),
    ]
