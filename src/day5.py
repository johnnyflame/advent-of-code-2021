from dataclasses import dataclass
from pprint import pprint
from collections import Counter
from aocd import get_data


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def forms_straight_line(self, other):
        return self.x == other.x or self.y == other.y


def part_2(input_data):
    pass


def part_1(input_data):
    pairs = get_source_destination_pairs(input_data)

    all_traversed_cells = []
    for pair in pairs:
        print(f"pair: {pair}")
        all_traversed_cells.extend(expand_source_dest(pair))

    counter = Counter(all_traversed_cells)
    total = 0
    for count in counter.values():
        if count > 1:
            total += 1
    return total


def expand_source_dest(pair):
    source, dest = pair
    assert source.forms_straight_line(dest)

    if source.x == dest.x:
        if dest.y > source.y:
            return [Coordinate(source.x, y) for y in range(source.y, dest.y + 1)]
        else:
            return [Coordinate(source.x, y) for y in range(dest.y, source.y + 1)]
    else:
        if dest.x > source.x:
            return [Coordinate(x, source.y) for x in range(source.x, dest.x + 1)]
        else:
            return [Coordinate(x, source.y) for x in range(dest.x, source.x + 1)]


def get_source_destination_pairs(input_data, horizontal_only=True):
    pairs = []
    for line in input_data.splitlines():
        line = line.split("->")
        source = line[0].split(",")
        dest = line[1].split(",")

        source_coord = Coordinate(int(source[0]), int(source[1]))
        dest_coord = Coordinate(int(dest[0]), int(dest[1]))

        # print(source_coord, dest_coord)
        if horizontal_only and source_coord.forms_straight_line(dest_coord):
            pairs.append((source_coord, dest_coord))

    return pairs


if __name__ == "__main__":
    data = get_data(day=5)
    print(f"part 1: {part_1(data)}")
