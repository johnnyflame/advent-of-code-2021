from src.day5 import part_1, part_2
import textwrap

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


# def test_part_2():
#     assert part_2(test_data) == 12
