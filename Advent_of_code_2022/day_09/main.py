import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def move_tail(tail_pos, head_pos):

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

    return tail_pos


def day_9(operations, rope_length):
    nodes = [(0, 0)] * rope_length
    visited = set()
    visited.add((0, 0))
    for operation in operations:

        match operation.split(" "):
            case ["U", num]:
                for i in range (int(num)):
                    nodes[0] = (nodes[0][0], nodes[0][1] - 1)
                    for i in range(len(nodes)-1):
                        nodes[i+1] = move_tail(nodes[i+1], nodes[i])
                    visited.add(nodes[-1])
                
            case ["D", num]:
                for i in range (int(num)):
                    nodes[0] = (nodes[0][0], nodes[0][1] + 1)
                    for i in range(len(nodes)-1):
                        nodes[i+1] = move_tail(nodes[i+1], nodes[i])
                    visited.add(nodes[-1])

            case ["L", num]:
                for i in range (int(num)):
                    nodes[0] = (nodes[0][0] - 1, nodes[0][1])
                    for i in range(len(nodes)-1):
                        nodes[i+1] = move_tail(nodes[i+1], nodes[i])
                    visited.add(nodes[-1])

            case ["R", num]:
                for i in range (int(num)):
                    nodes[0] = (nodes[0][0] + 1, nodes[0][1]) 
                    for i in range(len(nodes)-1):
                        nodes[i+1] = move_tail(nodes[i+1], nodes[i])
                    visited.add(nodes[-1])

    return len(visited)



if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n")

    print("Part 1: ", day_9(data, 2))
    print("Part 2: ", day_9(data, 10))
