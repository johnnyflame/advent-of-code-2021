from src.day1 import count_depth_increment, count_depth_increment_sum_of_three


def test_count_increment():
    raw_data = """
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
    test_input = [int(line) for line in raw_data.splitlines() if line]
    assert count_depth_increment(test_input) == 7


def test_count_increment_sum_of_three():
    raw_data = """
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
    test_input = [int(line) for line in raw_data.splitlines() if line]
    assert count_depth_increment_sum_of_three(test_input) == 5
