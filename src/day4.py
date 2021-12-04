from aocd import get_data


def bingo(data):
    numbers, boards = parse_input(data)
    winner, marking_sheet = get_first_winner(numbers, boards)
    return compute_score(winner, marking_sheet)


def get_last_winner_score(data):
    numbers, boards = parse_input(data)
    winners = get_all_winners(numbers, boards)

    return compute_score(winners[-1][0], winners[-1][1])


def compute_score(winner, marking_sheet):
    accum = 0
    multiplier = 0
    for row in range(len(marking_sheet)):
        for col in range(len(marking_sheet)):
            if marking_sheet[row][col] == 0:
                accum += winner[row][col]
            elif marking_sheet[row][col] == 2:
                multiplier = winner[row][col]

    return accum * multiplier


def get_all_winners(numbers, boards):
    rows = len(boards[0])
    cols = len(boards[0][0])
    marking_sheets = [[[0] * cols for _ in range(rows)] for _ in range(len(boards))]
    bingo_pack = list(zip(boards, marking_sheets))

    winners = []
    # iterate through all boards, for each row and column
    for number in numbers:
        for board, marking_sheet in bingo_pack:
            if (board, marking_sheet) in winners:
                continue

            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == number:
                        marking_sheet[row][col] = 1

                    col_vals = [row[col] for row in marking_sheet]
                    if set(col_vals) == {1}:
                        marking_sheet[row][col] = 2
                        winners.append((board, marking_sheet))
                        break

                    row_vals = marking_sheet[row]
                    if set(row_vals) == {1}:
                        marking_sheet[row][col] = 2
                        winners.append((board, marking_sheet))
                        break

    return winners


def get_first_winner(numbers, boards):
    rows = len(boards[0])
    cols = len(boards[0][0])
    marking_sheets = [[[0] * cols for _ in range(rows)] for _ in range(len(boards))]

    # iterate through all boards, for each row and column
    for number in numbers:
        for idx, board in enumerate(boards):
            marking_sheet = marking_sheets[idx]
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == number:
                        marking_sheet[row][col] = 1

                    col_vals = [row[col] for row in marking_sheet]
                    if set(col_vals) == {1}:
                        marking_sheet[row][col] = 2
                        return (board, marking_sheet)

                    row_vals = marking_sheet[row]
                    if set(row_vals) == {1}:
                        marking_sheet[row][col] = 2
                        return (board, marking_sheet)


def parse_input(data):
    data = data.splitlines()
    numbers = [int(num) for num in data[0].split(",")]

    boards = []
    board = []
    for line in data[2:]:
        if line == "":
            boards.append(board)
            board = []
        else:
            board.append([int(num) for num in line.split(" ") if num])
    boards.append(board)

    return numbers, boards


if __name__ == "__main__":
    data = get_data(day=4)
    print(f"part 1 answer: {bingo(data)}")
    print(f"part 2 answer: {get_last_winner_score(data)}")
