import textwrap

from src.day10 import part_1, part_2

test_data = textwrap.dedent(
    """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
).lstrip()


def test_part_1():
    assert part_1(test_data) == 26397


def test_part_2():
    assert part_2(test_data) == 288957
