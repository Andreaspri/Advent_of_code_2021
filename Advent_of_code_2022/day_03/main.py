import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))



def part_1(data):
    priority = 0
    for line in data:
        item = (set(line[:len(line) // 2]) & set(line[len(line) // 2:])).pop()
        if 0 < ord(item) - 96 < 27:
            priority += ord(item) - 96
        else:
            priority += ord(item) - 38

    return priority


def part_2(data):
    priority = 0
    for i in range(0, len(data), 3):
        item = (set(data[i]) & set(data[i+1]) & set(data[i+2])).pop()
        if 0 < ord(item) - 96 < 27:
            priority += ord(item) - 96
        else:
            priority += ord(item) - 38

    return priority



if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))