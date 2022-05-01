import json
import math


def add(number, depth):

    if isinstance(number,int):
        if number > 9:
            left = math.floor(number/2)
            right = math.ceil(number/2)
            return [left,right], "split"
        else:
            return number, "no action"

    if depth > 3 and isinstance(number[0],int) and isinstance(number[1], int):
        return number, "explode"

    for i in range(len(number)):
        response, action = add(number[i],depth+1)

        if action == "split":
            number[i] = response
        elif action == "explode":
            number[i] = 0




def part_1():
    with open("data.txt") as f:
        data = f.readlines()

    print(json.loads(data[0]))


    print([[1,2]+[[3,4],5]])

    total = []
    for line in data:
        total = [total + json.loads(line)]

    return add(total,1)


if __name__ == '__main__':
    part_1()

