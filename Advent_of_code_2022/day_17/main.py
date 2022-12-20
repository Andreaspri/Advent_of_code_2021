import os
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))




def part_1(moves: list, n: int) -> int:
    cave = {(x,0):True for x in range(1,8)}
    rock_types = [
        [(3,0),(4,0),(5,0),(6,0)], # Horizontal line
        [(3,1),(4,1),(5,1),(4,2),(4,0)], # + shape
        [(3,0),(4,0),(5,0),(5,1),(5,2)], # Inverted L shape
        [(3,0),(3,1),(3,2),(3,3)], # Vertical line
        [(3,0),(3,1),(4,0),(4,1)] # Square
    ]
    move_mod = len(moves)
    rock_mod = len(rock_types)
    highest = 0
    move_nmbr = 0
    for rock_nmbr in range(n):
        rock = rock_types[rock_nmbr % rock_mod].copy()
        for i in range(len(rock)):
            rock[i] = (rock[i][0], rock[i][1] + highest + 4)
        while True:
            if moves[move_nmbr] == '<':
                if not any([x[0] == 1 for x in rock]) and not any((x[0] - 1, x[1]) in cave for x in rock):
                    rock = [(x[0] - 1, x[1]) for x in rock]
            elif moves[move_nmbr] == '>':
                if not any([x[0] == 7 for x in rock]) and not any((x[0] + 1, x[1]) in cave for x in rock):
                    rock = [(x[0] + 1, x[1]) for x in rock]
            move_nmbr += 1
            move_nmbr %= move_mod
            # Move stone down if no collision with cave or rock
            if not any([(x[0], x[1] - 1) in cave for x in rock]):
                rock = [(x[0], x[1] - 1) for x in rock]
            else:
                cave.update({x:True for x in rock})
                highest = max([x[1] for x in rock]+[highest])
                break

    
    
    return highest





def part_2(moves: list, n: int) -> int:
    y_vals = []
    cave = {(x,0):True for x in range(1,8)}
    rock_types = [
        [(3,0),(4,0),(5,0),(6,0)], # Horizontal line
        [(3,1),(4,1),(5,1),(4,2),(4,0)], # + shape
        [(3,0),(4,0),(5,0),(5,1),(5,2)], # Inverted L shape
        [(3,0),(3,1),(3,2),(3,3)], # Vertical line
        [(3,0),(3,1),(4,0),(4,1)] # Square
    ]
    move_mod = len(moves)
    rock_mod = len(rock_types)
    highest = 0
    move_nmbr = 0
    for rock_nmbr in range(n):
        rock = rock_types[rock_nmbr % rock_mod].copy()
        for i in range(len(rock)):
            rock[i] = (rock[i][0], rock[i][1] + highest + 4)
        while True:
            if moves[move_nmbr] == '<':
                if not any([x[0] == 1 for x in rock]) and not any((x[0] - 1, x[1]) in cave for x in rock):
                    rock = [(x[0] - 1, x[1]) for x in rock]
            elif moves[move_nmbr] == '>':
                if not any([x[0] == 7 for x in rock]) and not any((x[0] + 1, x[1]) in cave for x in rock):
                    rock = [(x[0] + 1, x[1]) for x in rock]
            move_nmbr += 1
            move_nmbr %= move_mod
            # Move stone down if no collision with cave or rock
            if not any([(x[0], x[1] - 1) in cave for x in rock]):
                rock = [(x[0], x[1] - 1) for x in rock]
            else:
                cave.update({x:True for x in rock})
                highest = max([x[1] for x in rock]+[highest])
                y_vals.append(highest/(rock_nmbr+1))
                break

    
    
    return y_vals



if __name__ == '__main__':
    with open("data.txt") as f:
        data = list(f.read())
    print("Part 1:", part_1(data, 2022))



    #y_vals = part_2(data, 10000)
    #x_vals = [i for i in range(len(y_vals))]
    #plt.plot(x_vals, y_vals)
    #plt.show()
    # From inspection of plot i found:
    # 5718 -> 7413 -> 9108 Phase on 1695

    # It starts out of phase with the first 633 stones
    # The first 633 stones gives 1027 height
    # One phase gives 2671 height
    # It ends out of phase with the last 172 stones
    # The last 172 stones gives 289 height
    # So the heigh will be 1027 + 289 + 2671*((1000000000000-633-172)//1695)
    print("Part 2:",1027 + 289 + 2671*((1000000000000-633-172)//1695))