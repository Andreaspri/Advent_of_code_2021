
import numpy as np






def part_1(steps):
    with open("data.txt") as f:
        data = f.readlines()

    data = np.array([[int(i) for i in line.strip()] for line in data])

    total_flashes = 0
    for _ in range(steps):
        data += 1
        flashed = set()

        current_flashes = 1

        while current_flashes:
            current_flashes = 0
            for row in range(len(data)):
                for num in range(len(data[row])):
                    a = data[row][num]
                    if data[row][num] > 9 and (row,num) not in flashed:
                        data[row][num] = 0
                        current_flashes += 1
                        flashed.add((row,num))
                        if num < (len(data[row]) - 1) and (row,num+1) not in flashed:
                            data[row][num+1] += 1
                        if num > 0 and (row,num-1) not in flashed:
                            data[row][num-1] += 1
                        if row < (len(data)-1) and (row+1,num) not in flashed:
                            data[row+1][num] += 1
                        if row < (len(data)-1) and num < (len(data[row])-1) and (row+1,num+1) not in flashed:
                            data[row+1][num+1] += 1
                        if row < (len(data)-1) and num > 0 and (row+1,num-1) not in flashed:
                            data[row+1][num-1] += 1
                        if row > 0 and (row-1,num) not in flashed:
                            data[row-1][num] += 1
                        if row > 0 and num < (len(data[row])-1) and (row-1,num+1) not in flashed:
                            data[row-1][num+1] += 1
                        if row > 0 and num > 0 and (row-1,num-1) not in flashed:
                            data[row-1][num-1] += 1

            total_flashes += current_flashes

    return total_flashes



def part_2():
    with open("data.txt") as f:
        data = f.readlines()

    data = np.array([[int(i) for i in line.strip()] for line in data])

    simulations = 0
    while True:
        simulations += 1
        data += 1
        flashed = set()

        current_flashes = 1

        while current_flashes:
            current_flashes = 0
            for row in range(len(data)):
                for num in range(len(data[row])):
                    a = data[row][num]
                    if data[row][num] > 9 and (row, num) not in flashed:
                        data[row][num] = 0
                        current_flashes += 1
                        flashed.add((row, num))
                        if num < (len(data[row]) - 1) and (row, num + 1) not in flashed:
                            data[row][num + 1] += 1
                        if num > 0 and (row, num - 1) not in flashed:
                            data[row][num - 1] += 1
                        if row < (len(data) - 1) and (row + 1, num) not in flashed:
                            data[row + 1][num] += 1
                        if row < (len(data) - 1) and num < (len(data[row]) - 1) and (row + 1, num + 1) not in flashed:
                            data[row + 1][num + 1] += 1
                        if row < (len(data) - 1) and num > 0 and (row + 1, num - 1) not in flashed:
                            data[row + 1][num - 1] += 1
                        if row > 0 and (row - 1, num) not in flashed:
                            data[row - 1][num] += 1
                        if row > 0 and num < (len(data[row]) - 1) and (row - 1, num + 1) not in flashed:
                            data[row - 1][num + 1] += 1
                        if row > 0 and num > 0 and (row - 1, num - 1) not in flashed:
                            data[row - 1][num - 1] += 1


            if len(flashed) == len(data) * len(data[0]):
                return simulations



if __name__ == '__main__':
    print(part_1(100))
    print(part_2())

