import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))



def draw_grid(grid, width, height, tail_pos, head_pos):
    for y in range(height):
        for x in range(width):
            if (x, y) == tail_pos:
                print("T", end="")
            elif (x, y) == head_pos:
                print("H", end="")
            elif (x, y) in grid:
                print("#", end="")
            else:
                print(".", end="")
        print()



def move_tail(tail_pos, head_pos, visited):

    if abs(head_pos[0] - tail_pos[0]) > 1:
        if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0] + 1, tail_pos[1] + 1)
        elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
            tail_pos = (tail_pos[0] + 1, tail_pos[1] - 1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0] - 1, tail_pos[1] + 1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
            tail_pos = (tail_pos[0] - 1, tail_pos[1] - 1)


    elif  abs(head_pos[1] - tail_pos[1]) > 1:
        if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0] + 1, tail_pos[1] + 1)
        elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
            tail_pos = (tail_pos[0] + 1, tail_pos[1] - 1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0] - 1, tail_pos[1] + 1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
            tail_pos = (tail_pos[0] - 1, tail_pos[1] - 1)

    if abs(head_pos[0] - tail_pos[0]) == 2 or abs(head_pos[1] - tail_pos[1]) == 2:
        if head_pos[0] > tail_pos[0]:
            tail_pos = (tail_pos[0] + 1, tail_pos[1])
        elif head_pos[0] < tail_pos[0]:
            tail_pos = (tail_pos[0] - 1, tail_pos[1])
        elif head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0], tail_pos[1] + 1)
        elif head_pos[1] < tail_pos[1]:
            tail_pos = (tail_pos[0], tail_pos[1] - 1)


    visited.add(tail_pos)

    return tail_pos




def part_1(operations):
    head_pos = (0, 0)
    tail_pos = (0, 0)
    visited = set()
    visited.add((0, 0))
    for operation in operations:

        match operation.split(" "):
            case ["U", num]:
                for i in range (int(num)):
                    head_pos = (head_pos[0], head_pos[1] + 1)
                    tail_pos = move_tail(tail_pos, head_pos, visited)
                
            case ["D", num]:
                for i in range (int(num)):
                    head_pos = (head_pos[0], head_pos[1] - 1)
                    tail_pos = move_tail(tail_pos, head_pos, visited)

            case ["L", num]:
                for i in range (int(num)):
                    head_pos = (head_pos[0] - 1, head_pos[1])
                    tail_pos = move_tail(tail_pos, head_pos, visited)

            case ["R", num]:
                for i in range (int(num)):
                    head_pos = (head_pos[0] + 1, head_pos[1])
                    tail_pos = move_tail(tail_pos, head_pos, visited)


        print("Head: ", head_pos)
        print("Tail: ", tail_pos)
        print(draw_grid(visited,10,10, tail_pos, head_pos))

    return len(visited)








if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n")

    print("Part 1: ", part_1(data))
    #print("Part 2: ", part_2(data))

