from aocd import get_data


def part_1(input_data):
    input_data = [int(x) for x in input_data.split(",")]
    return find_min_global_cost(input_data)


def find_min_global_cost(input_data, costs=None):
    start, end = min(input_data), max(input_data) + 1

    global_total_distance = float("inf")

    for i in range(start, end):
        curr_total_distance = 0
        for pos in input_data:
            curr_distace = abs(i - pos)
            if costs:
                curr_total_distance += costs[curr_distace]
            else:
                curr_total_distance += curr_distace
        global_total_distance = min(global_total_distance, curr_total_distance)
    return global_total_distance


def part_2(input_data):
    input_data = [int(x) for x in input_data.split(",")]
    cost_memo = create_cost_memo(input_data)
    return find_min_global_cost(input_data, costs=cost_memo)


def create_cost_memo(input_data):
    end = max(input_data) + 1
    lookup = {}
    lookup[0] = 0
    for i in range(1, end):
        lookup[i] = i + lookup[i - 1]

    return lookup


if __name__ == "__main__":
    data = get_data(day=7)
    print(f"part 1: {part_1(data)}")
    print(f"part 1: {part_2(data)}")
