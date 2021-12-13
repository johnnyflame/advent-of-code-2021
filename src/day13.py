from dataclasses import dataclass

from aocd import get_data


def part_1(input_data, num_fold):
    coords, fold_instructions = parse_input(input_data)

    for line in fold_instructions[:num_fold]:
        axis, val = line
        coords = fold(coords=coords, axis=axis, centre=int(val))
    return len(set(coords))


def part_2(input_data):
    coords, fold_instructions = parse_input(input_data)

    last_x, last_y = -1, -1
    for line in fold_instructions:
        axis, val = line
        if axis == "y":
            last_y = int(val)
        if axis == "x":
            last_x = int(val)

        coords = fold(coords=coords, axis=axis, centre=int(val))

    coords = set(coords)
    print(last_x, last_y)
    for y in range(0, last_y):
        for x in range(0, last_x):
            if Coordinate(x, y) in coords:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def fold(*, coords, axis, centre):
    post_fold = []

    if axis == "y":
        for coord in coords:
            if coord.y < centre:
                post_fold.append(coord)
            else:
                new_y_coord = centre - (coord.y - centre)
                post_fold.append(Coordinate(coord.x, new_y_coord))
    else:
        for coord in coords:
            if coord.x < centre:
                post_fold.append(coord)
            else:
                new_x_coord = centre - (coord.x - centre)
                post_fold.append(Coordinate(new_x_coord, coord.y))

    return post_fold


def parse_input(input_data):
    coords = []
    fold_instructions = []
    for line in input_data.splitlines():
        if line == "":
            continue
        if line.startswith("fold"):
            fold_instructions.append(line.split()[-1].split("="))
        else:
            line = line.split(",")
            coords.append(Coordinate(int(line[0]), int(line[1])))

    return coords, fold_instructions


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


if __name__ == "__main__":
    data = get_data(day=13)
    print(f"part 1: {part_1(data,num_fold=1)}")
    print(f"part 2: {part_2(data)}")
