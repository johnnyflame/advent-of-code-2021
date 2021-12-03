from textwrap import dedent

from aocd import get_data


def move_submarine(instructions):
    horizontal = 0
    verticle = 0
    for line in instructions.splitlines():
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)
        if direction == "forward":
            horizontal += magnitude
        elif direction == "down":
            verticle += magnitude
        elif direction == "up":
            verticle -= magnitude
    return horizontal * verticle


def move_submarine_with_aim(instructions: str):
    horizontal = 0
    verticle = 0
    aim = 0
    for line in instructions.splitlines():
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)
        if direction == "forward":
            horizontal += magnitude
            verticle += aim * magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude
    return horizontal * verticle


if __name__ == "__main__":
    print(f"part 1 answer {move_submarine(get_data(day=2))}")
    print(f"part 1 answer {move_submarine_with_aim(get_data(day=2))}")
