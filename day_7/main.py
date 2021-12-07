

def part_1():
    with open("data.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    fuel_consumption = {}

    for i in range(min(data),max(data)):
        fuel_consumption[i] = sum([crab-i if crab > i else i-crab for crab in data])


    return min(fuel_consumption.values())


def part_2():
    with open("data.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    fuel_consumption = {}

    for i in range(min(data), max(data)):
        fuel_consumption[i] = sum([abs((crab-i))*(abs(crab-i) + 1)/2 for crab in data])


    return min(fuel_consumption.values())


if __name__ == '__main__':
    print(part_1())
    print(part_2())


