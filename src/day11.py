from typing import Deque

from aocd import get_data


def part_1(input_data, days):
    octopus_data = proprocess(input_data)
    return flash(octopus_data, days)


def part_2(input_data):
    octopus_data = proprocess(input_data)
    return simultanelous_flash(octopus_data)


def proprocess(input):
    return [[int(x) for x in line] for line in input.splitlines()]


def flash(grid, steps):
    total_flash_count = 0
    for _ in range(steps):
        flashed = set()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if (i, j) not in flashed:
                    grid[i][j] += 1
                    grid, flashed = update_neighbours(grid, i, j, flashed)

        for line in grid:
            for val in line:
                if val == 0:
                    total_flash_count += 1

    return total_flash_count


def all_zero(grid):
    return all(v == 0 for line in grid for v in line)


def simultanelous_flash(grid):
    iteration = 0
    while True:
        iteration += 1
        flashed = set()
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) not in flashed:
                    grid[i][j] += 1
                    grid, flashed = update_neighbours(grid, i, j, flashed)

        if all_zero(grid):
            return iteration


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
        )
    ]


def update_neighbours(grid, x, y, flashed):

    start = (x, y)
    queue = Deque()
    queue.append(start)

    while queue:
        curr_x, curr_y = queue.popleft()
        if grid[curr_x][curr_y] <= 9:
            return grid, flashed

        grid[curr_x][curr_y] = 0
        flashed.add((curr_x, curr_y))
        for next_x, next_y in get_neighbours(grid, curr_x, curr_y):
            if (next_x, next_y) in flashed:
                continue
            grid[next_x][next_y] += 1
            if grid[next_x][next_y] > 9 and (next_x, next_y) not in queue:
                queue.append((next_x, next_y))

    return grid, flashed


if __name__ == "__main__":
    data = get_data(day=11)
    print(f"part 1: {part_1(data, days=100)}")
    print(f"part 2: {part_2(data)}")
