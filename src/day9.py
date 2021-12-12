from collections import deque

from aocd import get_data


def part_1(input_data):
    height_map = preprocess(input_data)
    total = 0
    for row, curr_row in enumerate(height_map):
        for col, curr_val in enumerate(curr_row):
            neighbours = [
                height_map[x][y] for (x, y) in get_neighbours(height_map, row, col)
            ]
            if curr_val < min(neighbours):
                total += curr_val + 1
    return total


def preprocess(input_data):
    table = []
    for row in input_data.splitlines():
        curr_row = []
        for val in row:
            curr_row.append(int(val))
        table.append(curr_row)
    return table


def part_2(input_data):
    height_map = preprocess(input_data)

    basin_sizes = []
    for row, curr_row in enumerate(height_map):
        for col, curr_val in enumerate(curr_row):
            neighbours = [
                height_map[x][y] for (x, y) in get_neighbours(height_map, row, col)
            ]
            if curr_val < min(neighbours):
                basin_sizes.append(find_size_of_basin(height_map, row, col) + 1)
    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


def find_size_of_basin(grid, x, y):

    start = (x, y)
    queue = deque()
    visited = set()
    seen_neighbours = set()
    queue.append(start)

    while queue:
        curr_x, curr_y = queue.popleft()
        curr_val = grid[curr_x][curr_y]
        visited.add((curr_x, curr_y))

        for next_x, next_y in get_neighbours(grid, curr_x, curr_y):
            neighbour_val = grid[next_x][next_y]
            if neighbour_val == 9:
                continue
            if neighbour_val > curr_val and (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                seen_neighbours.add((next_x, next_y))

    return len(seen_neighbours)


def get_neighbours(grid, x, y):

    X = len(grid) - 1
    Y = len(grid[0]) - 1

    return [
        (x2, y2)
        for x2 in range(x - 1, x + 2)
        for y2 in range(y - 1, y + 2)
        if (
            -1 < x <= X
            and -1 < y <= Y
            and (x != x2 or y != y2)
            and (0 <= x2 <= X)
            and (0 <= y2 <= Y)
            and (y2 == y or x2 == x)  # make sure it's only horizontal and verticle
        )
    ]

    # return [grid[x][y] for (x, y) in neighbour_coords]


if __name__ == "__main__":
    data = get_data(day=9)

    # print(data)

    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")
