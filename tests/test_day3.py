from textwrap import dedent

from src.day3 import (
    co2_scrubber_rating,
    life_support_rating,
    oxygen_generator_rating,
    power_consumption,
)

test_data = dedent(
    """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
).lstrip("\n")


def test_power_consumption():
    assert power_consumption(test_data) == 198


def test_oxygen_generator_rating():
    assert oxygen_generator_rating(test_data) == 23


def test_co2_scrubber_rating():
    assert co2_scrubber_rating(test_data) == 10


def test_life_support_rating():
    assert life_support_rating(test_data) == 230
