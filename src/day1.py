from aocd import numbers


def count_depth_increment(data):
    increments = 0
    for prev, curr in zip(data, data[1:]):
        if curr > prev:
            increments += 1
    return increments


def count_depth_increment_sum_of_three(data):
    increments = 0
    prev_sum = data[0] + data[1] + data[2]
    for day1, day2, day3 in zip(data, data[1:], data[2:]):
        curr_sum = day1 + day2 + day3
        if curr_sum > prev_sum:
            increments += 1
        prev_sum = curr_sum
    return increments


if __name__ == "__main__":
    print(f"part 1 answer {count_depth_increment(numbers)}")
    print(f"part 2 answer {count_depth_increment_sum_of_three(numbers)}")
