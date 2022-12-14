import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def make_path(points: list[list[str]]) -> list[tuple[int, int]]:
    start, end = points
    x_start, y_start = [int(i) for i in start]
    x_end, y_end = [int(i) for i in end]

    if x_start == x_end:

        if y_start < y_end:
            return [(x_start, y) for y in range(y_start, y_end+1)]
        else:
            return [(x_start, y) for y in range(y_end, y_start+1)]
    if y_start == y_end:

        if x_start < x_end:
            return [(x, y_start) for x in range(x_start, x_end+1)]
        else:
            return [(x, y_start) for x in range(x_end, x_start+1)]



def make_obstacles(data: list[str]) -> tuple[set[tuple[int, int]], int]:
    obstacles = set()
    lines = [[i.split(",") for i in line.split(" -> ")] for line in data]
    depth_low = int(lines[0][0][1])
    for line in lines:
        for i in range(len(line)-1):
            for point in make_path(line[i:i+2]):
                obstacles.add(point)
                if point[1] > depth_low:
                    depth_low = point[1]
    return obstacles, depth_low



def part_1(obstacles: set[tuple[int, int]], depth_low: int) -> int:
    current_sand_blocks = 0
    while True:
        sand_pos = (500, 0)
        while True:
            if sand_pos[1]+1 > depth_low:
                # Is out of bounds
                return current_sand_blocks
            if (sand_pos[0],sand_pos[1]+1) not in obstacles:
                sand_pos = (sand_pos[0], sand_pos[1]+1)
            elif (sand_pos[0]-1, sand_pos[1]+1) not in obstacles:
                sand_pos = (sand_pos[0]-1, sand_pos[1]+1)
            elif (sand_pos[0]+1, sand_pos[1]+1) not in obstacles:
                sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
            else:
                # Cant move
                obstacles.add(sand_pos)
                current_sand_blocks += 1
                break


def part_2(obstacles: set[tuple[int, int]], depth_low: int) -> int:
    current_sand_blocks = 0
    while True:
        sand_pos = (500, 0)
        if sand_pos in obstacles:
            break
        while True:
            if sand_pos[1]+1 <= depth_low+1:
                if (sand_pos[0],sand_pos[1]+1) not in obstacles:
                    sand_pos = (sand_pos[0], sand_pos[1]+1)
                elif (sand_pos[0]-1, sand_pos[1]+1) not in obstacles:
                    sand_pos = (sand_pos[0]-1, sand_pos[1]+1)
                elif (sand_pos[0]+1, sand_pos[1]+1) not in obstacles:
                    sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
                else:
                    # Cant move
                    obstacles.add(sand_pos)
                    current_sand_blocks += 1
                    break
            else:
                # Is at the bottom
                obstacles.add(sand_pos)
                current_sand_blocks += 1
                break

    return current_sand_blocks

if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().splitlines()

    obstacle_set, depth = make_obstacles(data)
    print("Part 1:", part_1(obstacle_set.copy(), depth))
    print("Part 2:", part_2(obstacle_set, depth))

