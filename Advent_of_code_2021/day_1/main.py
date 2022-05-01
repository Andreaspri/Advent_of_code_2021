



def part_1():
    with open("data.txt") as f:
        data = f.readlines()
    count = 0

    for i in range(len(data)-1):
        if int(data[i]) < int(data[i+1]):
            count += 1

    return count


def part_2():
    with open("data.txt") as f:
        data = f.readlines()
    count = 0
    previous = 0
    for i in range(len(data)-3):
        current = int(data[i]) + int(data[i+1]) + int(data[i+2])
        if previous < current:
            count += 1
        previous = current

    return count





if __name__ == '__main__':
    print(part_1())
    print(part_2())


