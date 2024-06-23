import re
from math import sqrt, floor, ceil, prod

def parse_data() -> list:
    with open("input.txt") as f:
        data = f.readlines()

    data = list(zip((int(i) for i in re.findall(r"\D*(\d+)\D*", data[0])), (int(i) for i in re.findall(r"\D*(\d+)\D*", data[1]))))

    return data

def part1(races: list) -> int:
    
    combinations = []
    for time, distance in races:
        x_1 = ceil((time + sqrt(time**2 - 4*distance))/2-1)
        x_2 = floor((time - sqrt(time**2 - 4*distance))/2+1)
        combinations.append(x_1-x_2+1)

    return prod(combinations)

def part2(races: list) -> int:
    time = int("".join([str(i[0]) for i in races]))
    distance = int("".join([str(i[1]) for i in races]))
    x_1 = ceil((time + sqrt(time**2 - 4*distance))/2-1)
    x_2 = floor((time - sqrt(time**2 - 4*distance))/2+1)

    return x_1-x_2+1


if __name__=='__main__':
    races = parse_data()
    print("Part 1:", part1(races))
    print("Part 2:", part2(races))