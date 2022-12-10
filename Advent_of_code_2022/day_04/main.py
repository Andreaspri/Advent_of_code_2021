import os



os.chdir(os.path.dirname(os.path.abspath(__file__)))



def part_1(data):
    count = 0
    for line in data:
        first, second = line.split(",")
        first_set  = set(range(int(first.split("-")[0]), int(first.split("-")[1]) + 1))
        second_set = set(range(int(second.split("-")[0]), int(second.split("-")[1]) + 1))
        if first_set.issubset(second_set):
            count += 1
        elif second_set.issubset(first_set):
            count += 1

    return count



def part_2(data):
    count = 0
    for line in data:
        first, second = line.split(",")
        first_set = set(range(int(first.split("-")[0]), int(first.split("-")[1]) + 1))
        second_set = set(range(int(second.split("-")[0]), int(second.split("-")[1]) + 1))
        if first_set & second_set:
            count += 1

    return count



if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))