from multiprocessing import Process

with open("data.txt", 'r') as f:
    f = f.readlines()
    f = [line.strip() for line in f]


def get_active_part1():
    active = set()
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == '#':
                active.add((i, j, 0))
    return active


def get_active_part2():
    active = set()
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == '#':
                active.add((i, j, 0, 0))
    return active


def part1():
    active = get_active_part1()
    for r in range(6):
        new_active = set()

        for x in range(-10 - r, r + 10):
            for y in range(-10 - r, r + 10):
                for z in range(-10 - r, r + 10):
                    active_count = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            for k in range(-1, 2):
                                if not (i == 0 and k == 0 and j == 0):
                                    if (x + i, y + j, z + k,) in active:
                                        active_count += 1
                    if (x, y, z) in active and (active_count == 2 or active_count == 3):
                        new_active.add((x, y, z))
                    if (x, y, z) not in active and active_count == 3:
                        new_active.add((x, y, z))
        active = new_active

    print("Part 1:", len(active))


def part2():
    active = get_active_part2()
    for r in range(6):
        new_active = set()

        for x in range(-10 - r, r + 10):
            for y in range(-10 - r, r + 10):
                for z in range(-10 - r, r + 10):
                    for w in range(-10 - r, r + 10):
                        active_count = 0
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                for k in range(-1, 2):
                                    for p in range(-1, 2):
                                        if not (i == 0 and k == 0 and j == 0 and p == 0):
                                            if (x + i, y + j, z + k, w + p) in active:
                                                active_count += 1
                        if (x, y, z, w) in active and (active_count == 2 or active_count == 3):
                            new_active.add((x, y, z, w))
                        if (x, y, z, w) not in active and active_count == 3:
                            new_active.add((x, y, z, w))
        active = new_active
    print("Part 2:", len(active))


if __name__ == '__main__':
    p1 = Process(target=part1, name='part1')
    p2 = Process(target=part2, name='part1')
    p1.start()
    p2.start()