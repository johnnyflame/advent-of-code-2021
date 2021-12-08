from collections import defaultdict

from aocd import get_data

DIGITS_DISPLAY = {
    frozenset(["a", "b", "c", "e", "f", "g"]): "0",
    frozenset(["c", "f"]): "1",
    frozenset(["a", "c", "d", "e", "g"]): "2",
    frozenset(["a", "c", "d", "f", "g"]): "3",
    frozenset(["b", "c", "d", "f"]): "4",
    frozenset(["a", "b", "d", "f", "g"]): "5",
    frozenset(["a", "b", "d", "e", "f", "g"]): "6",
    frozenset(["a", "c", "f"]): "7",
    frozenset(["a", "b", "c", "d", "e", "f", "g"]): "8",
    frozenset(["a", "b", "c", "d", "f", "g"]): "9",
}

#
def part_1(input_data):
    count = 0
    lines = input_data.splitlines()
    unique = {2, 4, 3, 7}
    for line in lines:
        outputs = line.split("|")[1]
        for output in outputs.split():
            if len(output) in unique:
                count += 1
    return count


def part_2(input_data):
    lines = input_data.splitlines()
    total = 0
    for line in lines:

        inputs = line.split("|")[0]
        translation_lookup = create_translation(inputs)
        output_num = []
        for curr_combination in line.split("|")[1].split():
            post_translation = []
            for ch in curr_combination:
                post_translation.append(translation_lookup[ch])
            output_num.append(DIGITS_DISPLAY[frozenset(post_translation)])

        total += int("".join(output_num))

    return total


def create_translation(input_data):
    ch_counts = defaultdict(list)
    known = {}
    LED_display = {}
    known_mapping = {
        2: 1,
        4: 4,
        3: 7,
        7: 8,
    }

    for val in input_data.split():
        ch_counts[len(val)].append(frozenset(ch for ch in val))
        if len(val) in known_mapping:
            known[known_mapping[len(val)]] = frozenset(ch for ch in val)

    # 0, 6, 9
    assert (len(ch_counts[6])) == 3
    # 5, 2, 3
    assert (len(ch_counts[5])) == 3

    LED_display["".join(known[7] - known[1])] = "a"
    for candidate in ch_counts[6]:
        if len(frozenset.intersection(known[1], candidate)) == 1:
            known[6] = candidate

            for ch in known[1]:
                if ch in candidate:
                    LED_display[ch] = "f"
                else:
                    LED_display[ch] = "c"
        else:
            diff_with_8 = frozenset.difference(known[8], candidate)
            if diff_with_8.issubset(known[4]):
                known[0] = candidate
                LED_display["".join(diff_with_8)] = "d"
            else:
                known[9] = candidate
                LED_display["".join(diff_with_8)] = "e"

    for candidate in ch_counts[5]:
        if len(frozenset.difference(known[6], candidate)) == 1:
            diff = "".join(frozenset.difference(known[6], candidate))
            known[5] = candidate
            LED_display[diff] = "e"
        elif len(frozenset.difference(known[9], candidate)) == 1:
            diff = "".join(frozenset.difference(known[9], candidate))
            known[3] = candidate
            LED_display[diff] = "b"
        else:
            for ch in candidate:
                if ch not in LED_display.keys():
                    LED_display[ch] = "g"

    return LED_display


if __name__ == "__main__":
    data = get_data(day=8)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")
