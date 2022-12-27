import os
from math import lcm
import heapq

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Node:
    def __init__(self, x, y, t, goal):
        self.x = x
        self.y = y
        self.t = t
        self.h = abs(x - goal[0]) + abs(y - goal[1])
        self.f = self.t + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.f == other.f

    def __repr__(self):
        return f"Node(x={self.x}, y={self.y}, g={self.g}, h={self.h}, f={self.f})"

def get_states(data):
    states_rows = [set() for _ in range(len(data[0])-2)]
    states_cols = [set() for _ in range(len(data)-2)]
    border = set()
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == '>':
                col = j
                for state in states_rows:
                    state.add((i, col))
                    col += 1
                    if data[i][col] == '#':
                        col = 1
            elif char == '<':
                col = j
                for state in states_rows:
                    state.add((i, col))
                    col -= 1
                    if data[i][col] == '#':
                        col = len(data[0])-2
            elif char == '#':
                border.add((i, j))


    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == '^':
                row = i
                for state in states_cols:
                    state.add((row, j))
                    row -= 1
                    if data[row][j] == '#':
                        row = len(data)-2
            elif char == 'v':
                row = i
                for state in states_cols:
                    state.add((row, j))
                    row += 1
                    if data[row][j] == '#':
                        row = 1
            elif char == '#':
                border.add((i, j))

    # find lcm(lowest common multiple) of the lengths of the states rows and cols
    p = lcm(len(states_rows), len(states_cols))
    # Merge the states into p states which will form a cycle
    states = []
    for i in range(p):
        states.append(states_rows[i % len(states_rows)] | states_cols[i % len(states_cols)])
    

    return states, border

    

def part_1(states, borders, pos, goal):
    queue = [Node(pos[0], pos[1], 0, goal)]
    visited = set()
    while queue:
        node = heapq.heappop(queue)
        x, y, t = node.x, node.y, node.t
        if (x, y) == goal:
            return t
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)):
            nx, ny = x + dx, y + dy
            if (nx, ny) in borders:
                continue
            if (nx, ny) in states[(t+1) % len(states)]:
                continue
            if (nx, ny, t+1) in visited:
                continue
            visited.add((nx, ny, t+1))
            heapq.heappush(queue, Node(nx, ny, t+1, goal))


def part_2(states, borders, pos, goal):
    destinations = [pos, goal]
    queue = [Node(pos[0], pos[1], 0, goal)]
    visited = set()
    while queue:
        node = heapq.heappop(queue)
        x, y, t = node.x, node.y, node.t
        if (x, y) == goal:
            if len(destinations) > 0:
                goal = destinations.pop(0)
                queue = [Node(x, y, t, goal)]
                visited = set()
                continue
            return t
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)):
            nx, ny = x + dx, y + dy
            if (nx, ny) in borders:
                continue
            if (nx, ny) in states[(t+1) % len(states)]:
                continue
            if (nx, ny, t+1) in visited:
                continue
            visited.add((nx, ny, t+1))
            heapq.heappush(queue, Node(nx, ny, t+1, goal))


if __name__ == '__main__':
    with open('data.txt') as f:
        data = f.read().splitlines()
    states, borders = get_states(data)
    start = (0, data[0].index('.'))
    goal = (len(data)-1,data[-1].index('.'))
    borders.add((start[0]-1, start[1]))
    borders.add((goal[0]+1, goal[1]))
    print("Part 1:", part_1(states, borders, start, goal))
    print("Part 2:", part_2(states, borders, start, goal))
