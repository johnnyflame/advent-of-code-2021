from collections import Counter, defaultdict
from typing import DefaultDict

from aocd import get_data


def part_1(data, steps):
    pairs, ch_count, rules = parse_data(data)
    pairs, ch_count = update_pairs(pairs, ch_count, rules, steps=steps)

    return max(ch_count.values()) - min(ch_count.values())


def update_pairs(initial_pairs, ch_count, rules, steps):
    pairs = initial_pairs
    for _ in range(steps):
        pairs_updated = pairs.copy()
        for pair, count in pairs.items():
            if count < 1:
                continue
            if pair in rules:
                insert_ch = rules[pair]

                ch_count[insert_ch] += count
                pairs_updated[pair[0] + insert_ch] += count
                pairs_updated[insert_ch + pair[1]] += count
                pairs_updated[pair] -= count

        pairs = pairs_updated

    return {pair: count for pair, count in pairs_updated.items() if count > 0}, ch_count


def count_pairs(line):
    pairs = DefaultDict(int)
    for p1, p2 in zip(line, line[1:]):
        pairs[p1 + p2] += 1
    return pairs


def parse_data(data):
    data = data.splitlines()
    rules = {}

    for line in data[2:]:
        pair, insert = line.strip().split("->")
        rules[pair.strip()] = insert.strip()

    return count_pairs(data[0]), defaultdict(int, Counter(data[0])), rules


if __name__ == "__main__":
    data = get_data(day=14)
    print(f"part 1: {part_1(data,steps=10)}")
    print(f"part 2: {part_1(data,steps=40)}")
