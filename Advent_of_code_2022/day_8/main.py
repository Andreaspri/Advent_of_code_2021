import os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))



def part_1(grid):
    visible_trees = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[i]) - 1:
                visible_trees += 1
            else:
                col_true = np.all(grid[:, j][:i] < grid[i][j]) or np.all(grid[:, j][i+1:] < grid[i][j])
                row_true = np.all(grid[i][:j] < grid[i][j]) or np.all(grid[i][j+1:] < grid[i][j])
                if col_true or row_true:
                    visible_trees += 1
    return visible_trees


def count_trees(arr, tree):
    count = 0
    for k in range(len(arr)):
        count += 1
        if arr[k] >= tree:
            break
    return count
    

def part_2(grid):
    best_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            score = count_trees(grid[:, j][:i][::-1], grid[i][j]) * count_trees(grid[:, j][i+1:], grid[i][j]) * \
                count_trees(grid[i][:j][::-1], grid[i][j]) * count_trees(grid[i][j+1:], grid[i][j])

            if score > best_score:
                best_score = score
    return best_score


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = np.array([list(map(lambda x: int(x), list(i))) for i in f.read().split("\n")])
    print("Part 1: ", part_1(data))
    print("Part 2: ", part_2(data))