from collections import Counter
from typing import DefaultDict

from aocd import get_data


def build_adjacency_list(input_data):
    adjacency_list = DefaultDict(list)
    for line in input_data.splitlines():
        src, dest = line.split("-")
        adjacency_list[src].append(dest)
        adjacency_list[dest].append(src)

    return adjacency_list


def part_1(input_data):
    adjancency_list = build_adjacency_list(input_data)

    def terminating_predicate(curr_path):
        return curr_path[-1].islower() and curr_path[-1] in curr_path[:-2]

    return len(search(adjancency_list, "start", "end", terminating_predicate))


def part_2(input_data):
    adjancency_list = build_adjacency_list(input_data)

    def terminating_predicate(curr_path):
        if Counter(curr_path)["start"] > 1:
            return True
        if curr_path[-1].islower() and curr_path[-1] in curr_path[:-2]:
            counter = Counter(curr_path[:-1])
            for key, count in counter.items():
                if key[0].islower() and count > 1:
                    return True
        return False

    results = search(adjancency_list, "start", "end", terminating_predicate)
    return len(results)


def search(graph, start, end, terminating_condition):
    def backtrack(curr_path, goal):
        if terminating_condition(curr_path):
            return
        if curr_path[-1] == goal:
            solutions.append(curr_path)
            return
        else:
            for neighbour in graph[curr_path[-1]]:
                backtrack(curr_path + [neighbour], goal)

    solutions = []
    backtrack(
        [
            start,
        ],
        end,
    )
    return solutions


if __name__ == "__main__":
    print(f"part 1 : {part_1(get_data(day=12))}")
    print(f"part 2 : {part_2(get_data(day=12))}")
