from collections import Counter
from textwrap import dedent

from src.day14 import parse_data, part_1, update_pairs

test_data = dedent(
    """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
).lstrip()


def test_part_1():
    assert part_1(test_data, 10) == 1588


def test_char_count():
    pairs, ch_count, rules = parse_data(test_data)
    pairs, ch_count = update_pairs(pairs, ch_count, rules, steps=4)

    assert ch_count == Counter("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")
