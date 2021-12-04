import numpy as np



def parsing_data():
    with open("data.txt") as f:
        raw_data = f.readlines()

    bingo_numbers = raw_data.pop(0).strip()
    raw_data.pop(0)

    boards = {}

    board_count = 0
    for line in raw_data:
        if line == "\n":
            for transposed_line in np.transpose(boards[board_count]):
                boards[board_count].append(list(transposed_line))
            board_count += 1
            continue
        if board_count in boards:
            boards[board_count].append([int(i) for i in line.strip().split(" ") if i != ""])
        else:
            boards[board_count] = [[int(i) for i in line.strip().split(" ") if i != ""]]


    for transposed_line in np.transpose(boards[board_count]):
        boards[board_count].append(list(transposed_line))

    return boards, bingo_numbers


def part_1():
    boards, bingo_numbers = parsing_data()

    current_numbers = set()

    for number in bingo_numbers.split(","):
        current_numbers.add(int(number))

        for board in boards.values():
            if any(set(row).issubset(current_numbers) for row in board):
                return int(sum([sum([num for num in row if num not in current_numbers]) for row in
                                board]) / 2) * int(number)



def part_2():
    boards, bingo_numbers = parsing_data()

    current_numbers = []

    for number in bingo_numbers.split(","):
        current_numbers.append(int(number))

        for key in list(boards):
            is_subset = any(set(row).issubset(current_numbers) for row in boards[key])
            if is_subset and len(boards) > 1:
                boards.pop(key)
            elif is_subset and len(boards) == 1:
                return int(sum([sum([num for num in row if num not in current_numbers]) for row in
                                boards[key]]) / 2) * int(number)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
