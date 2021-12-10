



def part_1():
    with open("data.txt") as f:
        data = f.readlines()

    data = [[int(num) for num in list(line.strip())] for line in data]

    total = 0
    for y in range(len(data)):
        for x in range(len(data[y])):

            if y - 1 >= 0 and data[y-1][x] <= data[y][x]:
                continue

            if y + 1 < len(data) and data[y+1][x] <= data[y][x]:
                continue

            if x - 1 >= 0 and data[y][x-1] <= data[y][x]:
                continue

            if x + 1 < len(data[y]) and data[y][x+1] <= data[y][x]:
                continue

            total += 1 + data[y][x]


    return total



def part_2():
    with open("data.txt") as f:
        data = f.readlines()

    data = [[int(num) for num in list(line.strip())] for line in data]

    low_points = set()

    for y in range(len(data)):
        for x in range(len(data[y])):

            if y - 1 >= 0 and data[y-1][x] <= data[y][x]:
                continue

            if y + 1 < len(data) and data[y+1][x] <= data[y][x]:
                continue

            if x - 1 >= 0 and data[y][x-1] <= data[y][x]:
                continue

            if x + 1 < len(data[y]) and data[y][x+1] <= data[y][x]:
                continue

            low_points.add((y,x))


    basin_sizes = set()

    # BFS because why not
    while low_points:
        closed_list = set()
        open_list = set()
        open_list.add(low_points.pop())
        while open_list:
            current = open_list.pop()
            closed_list.add(current)
            up = (current[0]-1,current[1])
            down = (current[0]+1,current[1])
            left = (current[0],current[1]-1)
            right = (current[0],current[1]+1)
            if up[0] >= 0 and data[up[0]][up[1]] < 9 and \
                    (up not in closed_list and up not in open_list):
                open_list.add(up)

            if down[0] < len(data) and data[down[0]][down[1]] < 9 and \
                    (down not in closed_list and down not in open_list):
                open_list.add(down)

            if left[1] >= 0 and data[left[0]][left[1]] < 9 and \
                    (left not in closed_list and left not in open_list):
                open_list.add(left)

            if right[1] < len(data[right[0]]) and data[right[0]][right[1]] < 9 and \
                    (right not in closed_list and right not in open_list):
                open_list.add(right)


        basin_sizes.add(len(closed_list))

    largest = max(basin_sizes)
    basin_sizes.discard(largest)
    larger = max(basin_sizes)
    basin_sizes.discard(larger)
    large = max(basin_sizes)

    return large * larger * largest





if __name__ == '__main__':
    print(part_1())
    print(part_2())

