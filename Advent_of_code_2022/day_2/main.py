import os






os.chdir(os.path.dirname(os.path.abspath(__file__)))






def part_1(data):
    score = 0
    for round in data:
        match round.strip().split():
            case ["A", *response]:
                if response[0] == "X":
                    score += 4
                elif response[0] == "Y":
                    score += 8
                else:
                    score += 3

            case ["B", *response]:
                if response[0] == "Y":
                    score += 5
                elif response[0] == "Z":
                    score += 9
                else:
                    score += 1

            case ["C", *response]:
                if response[0] == "Z":
                    score += 6
                elif response[0] == "X":
                    score += 7
                else:
                    score += 2

    return score


def part_2(data):
    score = 0
    for round in data:
        match round.strip().split():
            case ["A", *response]:
                if response[0] == "X":
                    score += 3
                elif response[0] == "Y":
                    score += 4
                else:
                    score += 8

            case ["B", *response]:
                if response[0] == "X":
                    score += 1
                elif response[0] == "Y":
                    score += 5
                else:
                    score += 9

            case ["C", *response]:
                if response[0] == "X":
                    score += 2
                elif response[0] == "Y":
                    score += 6
                else:
                    score += 7


    return score







if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = f.readlines()
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))