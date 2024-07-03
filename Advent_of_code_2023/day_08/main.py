
from math import lcm

import sys

sys.setrecursionlimit(10**6)


def parse() -> tuple:
    with open("input.txt") as f:
        data = f.readlines()

    actions = list(data[0].strip())

    # Removing actions and newline
    data.pop(0)
    data.pop(0)

    positions = {}

    for pos in data:
        start, rest = pos.split(" = (")
        left, right = rest.replace(")","").strip().split(", ")

        positions[start] = (left, right)

    return actions, positions


def part1(actions: list, positions: dict) -> int:
    start = "AAA"

    def move(depth: int, pos, action_num: int) -> int:
        if pos == "ZZZ":
            return depth
        
        action = actions[action_num % len(actions)]

        if action == "L":
            return move(depth + 1, positions[pos][0], action_num + 1)
        elif action == "R":
            return move(depth + 1, positions[pos][1], action_num + 1)
        
    return move(0, start, 0)
        



def part2(actions: list, positions: dict) -> int:
    all_start_pos = [pos for pos in positions if pos[-1] == 'A']

    cycles = {}

    
    # Star by finding their cycle
    for pos in all_start_pos:
        action_num = 0
        curr_pos = pos
        visits = set()
        last_visit_pos = {}
        while True:
            action = actions[action_num % len(actions)]
            if curr_pos[-1] == 'Z':
                visits.add((curr_pos, action_num % len(actions)))
                last_visit_pos[curr_pos] = action_num

            if action == "L":
                curr_pos = positions[curr_pos][0]

            elif action == "R":
                curr_pos = positions[curr_pos][1]
            

            action_num += 1

            if (curr_pos, action_num % len(actions)) in visits:
                cycles[pos] = action_num - last_visit_pos[curr_pos]
                break

    # For some reason all of them start at their cycle and not in the middle of one.
    # This makes it possible to only use lcm, avoiding the chinease reminder theorem
    return lcm(*[i for i in cycles.values()])

            

if __name__=='__main__':
    actions, positions = parse()

    print("Part 1:", part1(actions, positions))
    print("Part 2:", part2(actions, positions))
