



def part1(arr):
    for ia,a in enumerate(arr):
        for ib,b in enumerate(arr):
            if int(a)+int(b) == 2020 and ia != ib:
                return int(a)*int(b)




def part2(arr):
    for ia,a in enumerate(arr):
        for ib,b in enumerate(arr):
            for ic,c in enumerate(arr):
                if int(a)+int(b)+int(c) == 2020 and ia != ib and ia != ic and ib != ic:
                    return int(a)*int(b)*int(c)


if __name__ == '__main__':
    with open("data.txt", "r") as f:
        f = f.read().split("\n")
        print("Part 1: ", part1(f))
        print("Part 2: ", part2(f))
