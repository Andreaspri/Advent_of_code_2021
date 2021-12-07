

def part_1():
    with open("data.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    fuel_consumption = set()

    for i in range(min(data),max(data)):
        fuel_consumption.add(sum([abs(crab-i) for crab in data]))


    return min(fuel_consumption)


def part_2():
    with open("data.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    fuel_consumption = set()

    for i in range(min(data), max(data)):
        fuel_consumption.add(sum([abs((crab-i))*(abs(crab-i) + 1)/2 for crab in data]))


    return min(fuel_consumption)


if __name__ == '__main__':
    print(part_1())
    print(part_2())


