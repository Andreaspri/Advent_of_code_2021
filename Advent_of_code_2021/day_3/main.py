






def bit_counter(data):

    bit_count = {}

    for line in data:
        for i, bit in enumerate(line):
            if bit == '\n':
                continue
            if bit == '1':
                bit_count[i] = bit_count.get(i, 0) + 1
            else:
                bit_count[i] = bit_count.get(i, 0)

    return bit_count


def part_1():
    with open("data.txt") as f:
        data = f.readlines()

    bit_count = bit_counter(data)

    gamma = ""
    epsilon = ""

    for i in range(len(bit_count)):
        if bit_count[i] >= len(data) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma,2) * int(epsilon,2)



def part_2():
    with open("data.txt") as f:
        data = f.readlines()

    oxygen = data.copy()
    co2 = data.copy()

    bit_position = 0

    while len(oxygen) > 1:
        bit_count_oxygen = bit_counter(oxygen)
        removed = 0

        if bit_count_oxygen[bit_position] >= len(oxygen) / 2:
            for i in range(len(oxygen)):
                if oxygen[i-removed][bit_position] == '0':
                    oxygen.pop(i-removed)
                    removed += 1
        else:
            for i in range(len(oxygen)):
                if oxygen[i-removed][bit_position] == '1':
                    oxygen.pop(i-removed)
                    removed += 1

        bit_position += 1


    bit_position = 0

    while len(co2) > 1:
        bit_count_co2 = bit_counter(co2)
        removed = 0
        if bit_count_co2[bit_position] >= len(co2) / 2:
            for i in range(len(co2)):
                if co2[i-removed][bit_position] == '1':
                    co2.pop(i-removed)
                    removed += 1
        else:
            for i in range(len(co2)):
                if co2[i-removed][bit_position] == '0':
                    co2.pop(i-removed)
                    removed += 1


        bit_position += 1

    return int(oxygen[0], 2) * int(co2[0], 2)



if __name__ == '__main__':
    print(part_1())
    print(part_2())

