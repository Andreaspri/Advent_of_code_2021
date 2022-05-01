

def check_if_error(stack,p):
    return (stack[-1] == "(" and p != ")") or (stack[-1] == "[" and p != "]")\
                        or (stack[-1] == "{" and p != "}") or (stack[-1] == "<" and p != ">")


def part_1():

    with open("data.txt") as f:
        data = f.readlines()

    total = 0
    for line in data:
        stack = []
        for p in line.strip():
            if p in " ({[<":
                stack.append(p)
            else:
                if check_if_error(stack,p):
                    if p == ")":
                        total += 3
                    elif p == "]":
                        total += 57
                    elif p == "}":
                        total += 1197
                    elif p == ">":
                        total += 25137
                stack.pop()
    return total




def part_2():
    with open("data.txt") as f:
        data = f.readlines()

    all_scores = []

    for line in data:
        stack = []
        line_total = 0
        for p in line.strip():

            if p in " ({[<":
                stack.append(p)
            else:
                if check_if_error(stack, p):
                    stack = []
                    break
                stack.pop()

        if stack:
            stack.reverse()

            for p in stack:
                if p == "(":
                    line_total = line_total*5 + 1
                elif p == "[":
                    line_total = line_total*5 + 2
                elif p == "{":
                    line_total = line_total*5 + 3
                elif p == "<":
                    line_total = line_total*5 + 4

            all_scores.append(line_total)

    all_scores.sort()

    return all_scores[int(len(all_scores)/2)]











if __name__ == '__main__':
    print(part_1())
    print(part_2())


