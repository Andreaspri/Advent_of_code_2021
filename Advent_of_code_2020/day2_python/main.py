


def part1(f):
    count1 = 0
    for fil in f:
        collection = {}
        fil1 = fil.split(":")
        first = fil1[0].split("-")
        second = first[1].split(" ")
        start = first[0]
        stop = second[0]
        char = second[1]
        password = fil1[1]
        for temp_char in password:
            if temp_char in collection.keys():
                value = collection.get(temp_char)
                value += 1
                collection.update({temp_char: value})
            else:
                collection.update({temp_char: 1})
        try:
            if int(start) <= collection.get(char) <= int(stop):
                count1 += 1
        except:
            pass
    return count1


def part2(f):
    count1 = 0
    for fil in f:
        fil1 = fil.split(":")
        first = fil1[0].split("-")
        second = first[1].split(" ")
        start = int(first[0])
        stop = int(second[0])
        char = second[1]
        password = list(fil1[1])

        if password[0] == " ":
            password.pop(0)

        if password[password.__len__() - 1] == "\n":
            password.pop()

        if char == password[start - 1] and char == password[stop - 1]:
            continue

        elif char == password[start - 1] and char != password[stop - 1]:
            count1 += 1

        elif char == password[stop - 1] and char != password[start - 1]:
            count1 += 1


    return count1


if __name__ == '__main__':
    with open("data.txt", "r") as file:
        data = file.readlines()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))


