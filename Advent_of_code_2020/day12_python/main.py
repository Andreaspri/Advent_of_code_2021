import re

action = re.compile(r"[^\d\n]")
number = re.compile(r"(\d+)")

with open("data.txt", "r") as f:
    f = f.readlines()


def part1():
    direction = 0
    ship = [0, 0, 0, 0]  # Index 0 is north, Index 1 is east, # Index 2 is south, Inded 3 is west
    for line in f:
        move = "".join(action.findall(line))
        amount = int("".join(number.findall(line)))

        if move == 'R':
            direction -= amount
            if direction < 0: direction += 360
        elif move == 'L':
            direction += amount
            if direction >= 360: direction -= 360
        elif move == 'F':
            if direction == 0:
                ship[1] += amount
            elif direction == 90:
                ship[0] += amount
            elif direction == 180:
                ship[3] += amount
            elif direction == 270:
                ship[2] += amount
        elif move == 'N':
            ship[0] += amount
        elif move == 'S':
            ship[2] += amount
        elif move == 'W':
            ship[3] += amount
        elif move == 'E':
            ship[1] += amount
    return abs(ship[0] - ship[2]) + abs(ship[1] - ship[3])


def part2():
    import numpy as np
    waypoint = np.array([1, 10, 0, 0])  # Index 0 is north, Index 1 is east, # Index 2 is south, Inded 3 is west
    ship = np.array([0, 0, 0, 0])  # Index 0 is north, Index 1 is east, # Index 2 is south, Inded 3 is west
    for line in f:
        move = "".join(action.findall(line))
        amount = int("".join(number.findall(line)))

        if move == 'R':
            waypoint = np.roll(waypoint, int(amount / 90))  # Shifts the array to the right
        elif move == 'L':
            waypoint = np.roll(waypoint, int(-amount / 90))  # Shifts the array to the left
        elif move == 'F':
            ship += amount * waypoint
        elif move == 'N':
            waypoint[0] += amount
        elif move == 'S':
            waypoint[2] += amount
        elif move == 'W':
            waypoint[3] += amount

        elif move == 'E':
            waypoint[1] += amount
    return abs(ship[0] - ship[2]) + abs(ship[1] - ship[3])


print("Part 1:", part1())
print("Part 2:", part2())