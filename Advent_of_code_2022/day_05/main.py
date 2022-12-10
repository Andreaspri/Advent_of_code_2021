import os
from copy import deepcopy


os.chdir(os.path.dirname(os.path.abspath(__file__)))



def part_1(stack, instructions):
    for instruction in instructions:
        stack[instruction[2]-1] += reversed(stack[instruction[1]-1][-instruction[0]:])
        del stack[instruction[1]-1][-instruction[0]:]

    return "".join([i[-1] for i in stack])
        


def part_2(stack, instructions):
    for instruction in instructions:
        stack[instruction[2]-1] += stack[instruction[1]-1][-instruction[0]:]
        del stack[instruction[1]-1][-instruction[0]:]

    return "".join([i[-1] for i in stack])



if __name__ == "__main__":
    with open("data.txt") as f:
        stack, instructions = f.read().split("\n\n")

    stack = [[s[i] for s in reversed(stack.split("\n")[:-1]) if "A" <= s[i] <= "Z"] for i, c in enumerate(stack.split("\n")[-1:][0]) if "1" <= c <= "9"]
    instructions = [[int(l.split(" ")[1]), int(l.split(" ")[3]), int(l.split(" ")[5])] for l in instructions.split("\n")]

    print("Part 1:", part_1(deepcopy(stack), instructions))
    print("Part 2:", part_2(stack, instructions))