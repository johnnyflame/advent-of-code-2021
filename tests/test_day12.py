from textwrap import dedent

from src.day12 import part_1, part_2

small_example = dedent(
    """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
).lstrip()

medium_example = dedent(
    """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""
).lstrip()


def test_part_1():
    assert part_1(small_example) == 10


def test_part_1_medium():
    assert part_1(medium_example) == 19


def test_part_2_small():
    assert part_2(small_example) == 36


def test_part_2_medium():
    assert part_2(medium_example) == 103
