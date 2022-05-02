





def part_1():
    with open("data.txt") as f:
        data = f.read().strip()

    x_1 = int(data.split("x=")[1].split("..")[0])
    x_2 = int(data.split("x=")[1].split("..")[1].split(",")[0])
    y_1 = int(data.split("y=")[1].split("..")[0])
    y_2 = int(data.split("y=")[1].split("..")[1])

    possible_x = set(range(1, x_2 + 1))

    max_y = set()
    for i in possible_x:
        x_vector = i
        count = 0
        while True:
            local_max_y = set()
            y_vector = count
            local_x_vector = x_vector
            height = 0
            length = 0
            while True:
                height += y_vector
                y_vector -= 1
                length += local_x_vector
                if local_x_vector > 0:
                    local_x_vector -= 1
                local_max_y.add(height)
                if y_1 <= height <= y_2 and x_1 <= length <= x_2:
                    max_y.add(max(local_max_y))


                elif length > x_2 or height < y_1:
                    break
            if count > 200:
                break

            count += 1

    return max(max_y)




def part_2():
    with open("data.txt") as f:
        data = f.read().strip()

    x_1 = int(data.split("x=")[1].split("..")[0])
    x_2 = int(data.split("x=")[1].split("..")[1].split(",")[0])
    y_1 = int(data.split("y=")[1].split("..")[0])
    y_2 = int(data.split("y=")[1].split("..")[1])

    possible_x = set(range(1,x_2+1))

    max_y = []
    for i in possible_x:
        x_vector = i
        count = 0
        while True:
            local_max_y = []
            y_vector = count + y_1
            local_x_vector = x_vector
            height = 0
            length = 0
            while True:
                height += y_vector
                y_vector -= 1
                length += local_x_vector
                if local_x_vector > 0:
                    local_x_vector -= 1
                local_max_y.append(height)
                if y_1 <= height <= y_2 and x_1 <= length <= x_2:
                    max_y.append((x_vector,count-10))


                elif length > x_2 or height < y_1:
                    break
            if count > 400:
                break

            count += 1

    return len(set(max_y))


if __name__ == '__main__':
    print(part_1())
    print(part_2())