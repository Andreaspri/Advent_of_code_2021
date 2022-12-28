import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def snafu_to_decimal(snafu):
    number = []
    for char in snafu:
        if char == '-':
            number.append(-1)
        elif char == '=':
            number.append(-2)
        else:
            number.append(int(char))
    number.reverse()
    return sum([number[i] * 5**i for i in range(len(number))])


def decimal_to_snafu(decimal):
    number = []
    # Convert the decimal to 5 base
    while decimal > 0:
        number.append(decimal % 5)
        decimal //= 5
    # Reverse it to get it in the right order
    number.reverse()
    # Convert the 5 base to snafu
    for i in range(len(number)-1, -1, -1):
        if number[i] == 3:
            number[i] = '='
            if i != 0:
                number[i-1] += 1
            else:
                number.insert(0, 1)
        elif number[i] == 4:
            number[i] = '-'
            if i != 0:
                number[i-1] += 1
            else:
                number.insert(0, 1)
        elif number[i] == 5:
            number[i] = 0
            if i != 0:
                number[i-1] += 1
            else:
                number.insert(0, 1)

    return "".join(map(str,number))



if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().splitlines()

    print("Day 25:", decimal_to_snafu(sum(map(snafu_to_decimal,data))))


    

