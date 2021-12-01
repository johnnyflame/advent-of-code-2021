from aocd import numbers


def count_depth_increment(data):
    increments = 0
    for prev, curr in zip(data, data[1:]):
        if curr > prev:
            increments += 1
    return increments


if __name__ == "__main__":
    print(f"part 1 answer {count_depth_increment(numbers)}")
