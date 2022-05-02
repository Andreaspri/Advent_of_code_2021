import pandas as pd
import math




def part1_and_part2(f):
    threes_hit = []

    step = [{1: 1}, {3: 1}, {5: 1}, {7: 1}, {1: 2}]
    x, count1, threes, multiplied = 0, 0, 0, 1
    for pair in step:
        for right, down in pair.items():
            for i in f.values:
                if count1 % down == 0:
                    if i[0][x] == '#':
                        threes += 1
                    if x + right > 30:
                        x -= 31
                    x += right
                count1 += 1
            threes_hit.append(threes)
            threes, x = 0, 0
        count1 = 0
    return threes_hit


if __name__ == '__main__':
    data = pd.read_csv("data.txt", header=None)
    result = part1_and_part2(data)
    print("Part 1: ", max(result))
    print("Part 2: ", math.prod(result))

