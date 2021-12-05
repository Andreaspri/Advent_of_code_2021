

def parse_data():
    with open("data.txt") as f:
        data = f.readlines()

    points = {}

    for i, line in enumerate(data):
        points[i] = [[int(xy_int) for xy_int in xy.split(",")] for xy in line.split(" -> ")]

    return points


def part_1():
    points = parse_data()

    counter_dict = {}

    for point in points.values():
        if point[0][0] == point[1][0]:
            for i in range(point[0][1], point[1][1] + (-1 if point[0][1] > point[1][1] else 1),-1 if point[0][1] > point[1][1] else 1):
                counter_dict[(point[0][0], i)] = counter_dict.get((point[0][0], i),0) + 1
        elif point[0][1] == point[1][1]:
            for i in range(point[0][0], point[1][0] + (-1 if point[0][0] > point[1][0] else 1),-1 if point[0][0] > point[1][0] else 1):
                counter_dict[(i, point[0][1])] = counter_dict.get((i, point[0][1]),0) + 1

    return sum(1 for count in counter_dict.values() if count > 1)


def part_2():
    points = parse_data()
    counter_dict = {}

    for point in points.values():
        if point[0][0] == point[1][0]:
            for i in range(point[0][1], point[1][1] + (-1 if point[0][1] > point[1][1] else 1),-1 if point[0][1] > point[1][1] else 1):
                counter_dict[(point[0][0], i)] = counter_dict.get((point[0][0], i),0) + 1
        elif point[0][1] == point[1][1]:
            for i in range(point[0][0], point[1][0] + (-1 if point[0][0] > point[1][0] else 1),-1 if point[0][0] > point[1][0] else 1):
                counter_dict[(i, point[0][1])] = counter_dict.get((i, point[0][1]),0) + 1
        else:
            x_range = range(point[0][0], point[1][0] + (-1 if point[0][0] > point[1][0] else 1), -1 if point[0][0] > point[1][0] else 1)
            y_range = range(point[0][1], point[1][1] + (-1 if point[0][1] > point[1][1] else 1), -1 if point[0][1] > point[1][1] else 1)
            for x, y in zip(x_range,y_range):
                counter_dict[(x, y)] = counter_dict.get((x, y), 0) + 1

    return sum(1 for count in counter_dict.values() if count > 1)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
