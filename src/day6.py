from collections import Counter

from aocd import get_data


def part1(data, days):
    fish_pool = data
    for _ in range(1, days + 1):
        fish_pool = breed_fish(fish_pool)
    return len(fish_pool)


def breed_fish(fish_pool):
    curr_fish = []
    new_fish = 0
    for _, timer in enumerate(fish_pool):
        if timer == 0:
            new_fish += 1
            curr_fish.append(6)
        else:
            timer -= 1
            curr_fish.append(timer)
    for _ in range(new_fish):
        curr_fish.append(8)
    return curr_fish


def part_2(data, days):
    fish_pool = Counter({key: 0 for key in range(9)})
    fish_pool.update(data)
    for _ in range(1, days + 1):
        new_fish = fish_pool[0]

        for timer in range(8):
            fish_pool[timer] = fish_pool[timer + 1]
        fish_pool[8] = new_fish
        fish_pool[6] += new_fish

    return sum(fish_pool.values())


def flatten_fish(counter):
    output = []
    for fish, count in counter.items():
        if count == 0:
            continue
        for _ in range(count):
            output.append(fish)
    return output


if __name__ == "__main__":
    input_data = [int(x) for x in get_data(day=6).split(",")]
    print(f"part 1: {part_2(input_data,days=80)}")
    print(f"part 2: {part_2(input_data,days=256)}")
