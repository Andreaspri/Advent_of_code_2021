



def part_1():
    with open("data.txt") as f:
        data = f.readlines()

    x = 0
    depth = 0
    for line in data:
        command, value = line.split(" ")
        if command == "forward":
            x += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)
    return x*depth


def part_2():
    with open("data.txt") as f:
        data = f.readlines()

    x = 0
    depth = 0
    aim = 0
    for line in data:
        command, value = line.split(" ")
        if command == "forward":
            x += int(value)
            depth += aim*int(value)
        elif command == "down":
            aim += int(value)
        elif command == "up":
            aim -= int(value)
    return x*depth




if __name__ == '__main__':
    print(part_1())
    print(part_2())

