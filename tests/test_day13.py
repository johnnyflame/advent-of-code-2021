from textwrap import dedent

from src.day13 import part_1, part_2

test_input = dedent(
    """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
).lstrip()


def test_part_1():
    assert part_1(test_input, num_fold=1) == 17


def test_part_2():
    assert (
        part_2(test_input)
        == dedent(
            """
    #####
#...#
#...#
#...#
#####
.....
.....
    """
        ).lstrip()
    )
