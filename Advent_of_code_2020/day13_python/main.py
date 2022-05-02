import numpy as np


def part1(input_data):
    target = int(input_data[0])

    parse = input_data[1].split(',')
    busses = [int(x) for x in parse if x != 'x']

    busses_wait_time = {}
    for i in busses:
        remainder = target % i
        busses_wait_time[i - remainder] = i

    return min(busses_wait_time) * busses_wait_time[min(busses_wait_time)]


def calculate_inverse(x, n):
    a = 1
    b = 0
    c = 0
    d = 1

    while x != n:

        if x < n:
            temp = n // x
            if n - x * temp == 0:
                temp = 1
            n -= x * temp
            c -= a * temp
            d -= b * temp
        else:
            temp = x // n
            if x - n * temp == 0:
                temp = 1
            x -= n * temp
            a -= c * temp
            b -= d * temp
    if x > 1 or n > 1:
        print("The gcd of x and n is not 1")
    return a


def part2(input_data):
    parse = input_data[1].split(',')
    busses = [int(x) if x != 'x' else x for x in parse]
    buss_id_mod = {}

    for i, b in enumerate(busses):
        if b != 'x':
            buss_id_mod[np.longlong(b)] = b - i % b
    b = buss_id_mod.values()
    N = np.prod(list(buss_id_mod.keys()))
    n = [N // i for i in buss_id_mod.keys()]
    x = [calculate_inverse(i, b) for i, b in zip(n, buss_id_mod)]
    solution = sum([b_i * n_i * x_i for b_i, n_i, x_i in zip(b, n, x)])
    return solution % N


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = f.readlines()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
