from queue import PriorityQueue

from aocd import get_data


def part_1(input):
    grid = parse_input(input)
    target = (len(grid) - 1, len(grid[0]) - 1)
    return find_min_cost_to_target(grid, (0, 0), target)


def find_min_costs_matrix(grid):
    # work out horizontal costs
    for idx, _ in enumerate(grid[0][2:], 2):
        grid[0][idx] += grid[0][idx - 1]
    # work out vertical starting costs
    for row, _ in enumerate(grid[2:], 2):
        grid[row][0] += grid[row - 1][0]

    for row_id, row in enumerate(grid[1:], 1):
        for col_id, col in enumerate(grid[0][1:], 1):
            grid[row_id][col_id] += min(
                grid[row_id - 1][col_id], grid[row_id][col_id - 1]
            )

    return grid


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


def part_2(input):
    original_grid = parse_input(input)
    large_grid = expand_grid(original_grid)

    target = (len(large_grid) - 1, len(large_grid[0]) - 1)
    return find_min_cost_to_target(large_grid, (0, 0), target)


def find_min_cost_to_target(grid, start, dest):
    costs = {}
    costs[start] = 0

    queue = PriorityQueue()

    for row, curr_row in enumerate(grid):
        for col, _ in enumerate(curr_row):
            costs[(row, col)] = float("inf")

    queue.put((0, (start)))
    while queue:
        cost, (curr_x, curr_y) = queue.get()

        if cost > costs[(curr_x, curr_y)]:
            continue

        if (curr_x, curr_y) == dest:
            return cost

        for next_x, next_y in get_neighbours(grid, curr_x, curr_y):
            if (curr_x, curr_y) == start:
                delta_cost = grid[next_x][next_y]
            else:
                delta_cost = costs[(curr_x, curr_y)] + grid[next_x][next_y]

            if costs[(next_x, next_y)] > delta_cost:
                costs[(next_x, next_y)] = delta_cost
                queue.put((delta_cost, (next_x, next_y)))


def expand_grid(grid):
    output = []
    increments = []
    increments.append(grid)
    for i in range(1, 5):
        post_increment_grid = []
        for row in grid:
            post_increment_grid.append(
                [(val + i) % 9 if (val + i) > 9 else (val + i) for val in row]
            )
        increments.append(post_increment_grid)

    for tile in increments:
        output += expand_tile_row(tile)

    return output


def expand_tile_row(grid):
    increments = []
    increments.append(grid)

    for i in range(1, 5):
        post_increment_grid = []
        for row in grid:
            post_increment_grid.append(
                [(val + i) % 9 if (val + i) > 9 else (val + i) for val in row]
            )
        increments.append(post_increment_grid)

    return [a + b + c + d + e for a, b, c, d, e in zip(*increments)]


def parse_input(data):
    output = []
    for line in data.splitlines():
        output.append([int(val) for val in line])
    return output


if __name__ == "__main__":
    data = get_data(day=15)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")
