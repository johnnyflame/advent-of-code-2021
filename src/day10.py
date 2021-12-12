from aocd import get_data

MATCHING_BRACES = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def part_1(input_data):
    first_illegal_chars_in_line = []
    corrupt_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    for line in input_data.splitlines():
        illegal_ch = find_first_corrupt_ch(line)
        if illegal_ch:
            first_illegal_chars_in_line.append(illegal_ch)

    return sum(corrupt_scores[ch] for ch in first_illegal_chars_in_line)


def part_2(input_data):
    corrupt_scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    ch_to_complete_line = []
    for line in input_data.splitlines():
        if find_first_corrupt_ch(line):
            continue
        ch_to_complete_line.append(find_incomplete(line))

    all_scores = []
    for line in ch_to_complete_line:
        score = 0
        for ch in reversed(line):
            score *= 5
            score += corrupt_scores[ch]
        all_scores.append(score)

    all_scores.sort()
    return all_scores[len(all_scores) // 2]


def find_incomplete(line):
    stack = []
    for ch in line:
        if ch in MATCHING_BRACES:
            stack.append(ch)
        else:
            if ch != MATCHING_BRACES[stack.pop()]:
                return ch
    return [MATCHING_BRACES[remaining_ch] for remaining_ch in stack]


def find_first_corrupt_ch(line):
    stack = []
    for ch in line:
        if ch in MATCHING_BRACES:
            stack.append(ch)
        else:
            if ch != MATCHING_BRACES[stack.pop()]:
                return ch


if __name__ == "__main__":
    input_data = get_data(day=10)

    print(f"part 1: {part_1(input_data)}")
    print(f"part 2: {part_2(input_data)}")
