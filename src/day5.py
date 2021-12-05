from collections import Counter
from dataclasses import dataclass

from aocd import get_data


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def forms_straight_line(self, other):
        return self.x == other.x or self.y == other.y


def part_2(input_data):
    pairs = get_source_destination_pairs(input_data)

    all_traversed_cells = []
    for source, dest in pairs:
        all_traversed_cells.extend(expand_source_dest(source, dest))
    return count_repeated_occurance(all_traversed_cells)


def part_1(input_data):
    pairs = get_source_destination_pairs(input_data)

    all_traversed_cells = []
    for source, dest in pairs:
        if not source.forms_straight_line(dest):
            continue
        all_traversed_cells.extend(expand_source_dest(source, dest))
    return count_repeated_occurance(all_traversed_cells)


def count_repeated_occurance(cells):
    counter = Counter(cells)
    total = 0
    for count in counter.values():
        if count > 1:
            total += 1
    return total


def expand_source_dest(source, dest):
    if source.x == dest.x:
        if dest.y > source.y:
            return [Coordinate(source.x, y) for y in range(source.y, dest.y + 1)]
        else:
            return [Coordinate(source.x, y) for y in range(dest.y, source.y + 1)]
    elif source.y == dest.y:
        if dest.x > source.x:
            return [Coordinate(x, source.y) for x in range(source.x, dest.x + 1)]
        else:
            return [Coordinate(x, source.y) for x in range(dest.x, source.x + 1)]
    else:
        if source.x < dest.x:
            x_coords = list(range(source.x, dest.x + 1))
            if source.y < dest.y:
                y_coords = list(range(source.y, dest.y + 1))
            else:
                y_coords = list(range(source.y, dest.y - 1, -1))
        else:
            x_coords = list(range(source.x, dest.x - 1, -1))
            if source.y < dest.y:
                y_coords = list(range(source.y, dest.y + 1))
            else:
                y_coords = list(range(source.y, dest.y - 1, -1))
        return [Coordinate(x, y) for x, y in zip(x_coords, y_coords)]


def get_source_destination_pairs(input_data):
    pairs = []
    for line in input_data.splitlines():
        line = line.split("->")
        source = line[0].split(",")
        dest = line[1].split(",")

        source_coord = Coordinate(int(source[0]), int(source[1]))
        dest_coord = Coordinate(int(dest[0]), int(dest[1]))

        pairs.append((source_coord, dest_coord))

    return pairs


if __name__ == "__main__":
    data = get_data(day=5)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")
