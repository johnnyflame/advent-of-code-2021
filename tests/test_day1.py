from src.day1 import count_depth_increment, count_depth_increment_sum_of_three

RAW_DATA = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
"""
test_input = [int(line) for line in RAW_DATA.splitlines() if line]


def test_count_increment():
    assert count_depth_increment(test_input) == 7


def test_count_increment_sum_of_three():
    assert count_depth_increment_sum_of_three(test_input) == 5
