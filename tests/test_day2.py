from textwrap import dedent

from src.day2 import move_submarine


def test_move_submarine():
    data = dedent(
        """
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    """
    ).lstrip("\n")

    assert move_submarine(data)
