

# 1 : 2
# 4 : 4
# 7 : 3
# 8 : 7


def part_1():
    with open("data.txt") as f:
        data = f.readlines()
    return sum([sum([1 for word in line.split(" | ")[1].strip().split(" ") if len(word) in [2,3,4,7]]) for line in data])


def part_2():
    with open("data.txt") as f:
        data = f.readlines()

    total = 0
    for line in data:
        words = {}
        for word in sorted(line.split(" | ")[0].strip().split(" "),key=lambda x: len(x)):
            if len(word) == 2:
                words[1] = word
            elif len(word) == 3:
                words[7] = word
            elif len(word) == 4:
                words[4] = word
            elif len(word) == 7:
                words[8] = word
            elif len(word) == 5:
                if len(set(word) & set(words.get(7, "0"))) == 3:
                    words[3] = word
                elif len(set(word) & set(words.get(4,"0"))) == 3:
                    words[5] = word
                else: words[2] = word
            elif len(word) == 6:
                if len(set(word) & set(words.get(5,"0"))) == 5:
                    if len(set(word) & set(words.get(7,"0"))) == 2:
                        words[6] = word
                    else:
                        words[9] = word
                else:
                    words[0] = word

        number = []
        for word in line.split(" | ")[1].strip().split(" "):
            for n, w in words.items():
                if len(set(word) & set(w)) == len(word):
                    number.append(str(n))
                    break

        total += int("".join(number))




    return total




if __name__ == '__main__':
    print(part_1())
    print(part_2())

