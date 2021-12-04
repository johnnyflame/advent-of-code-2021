from collections import Counter

from aocd import get_data


def power_consumption(data):
    data = data.splitlines()
    gamma = []
    epsilon = []

    for col in range(len(data[0])):
        col_vals = [row[col] for row in data]
        counter = Counter(col_vals)
        if counter["1"] > counter["0"]:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")

    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)

    return gamma * epsilon


def oxygen_generator_rating(data):
    data = data.splitlines()
    for col in range(len(data[0])):
        col_vals = [row[col] for row in data]

        most_common = "1"
        counter = Counter(col_vals)
        if counter["1"] < counter["0"]:
            most_common = "0"

        to_remove = []
        for row in data:
            if (row[col]) != most_common:
                to_remove.append(row)

        for val in to_remove:
            data.remove(val)

        if len(data) == 1:
            break

    return int("".join(data), 2)


def co2_scrubber_rating(data):
    data = data.splitlines()
    for col in range(len(data[0])):
        col_vals = [row[col] for row in data]

        most_common = "1"
        counter = Counter(col_vals)
        if counter["1"] < counter["0"]:
            most_common = "0"

        to_remove = []
        for row in data:
            if (row[col]) == most_common:
                to_remove.append(row)

        for val in to_remove:
            data.remove(val)

        if len(data) == 1:
            break

    return int("".join(data), 2)


def life_support_rating(data):
    return oxygen_generator_rating(data) * co2_scrubber_rating(data)


if __name__ == "__main__":
    input_data = get_data(day=3)
    print(f"part 1: {power_consumption(input_data)}")
    print(f"part 2: {life_support_rating(input_data)}")
