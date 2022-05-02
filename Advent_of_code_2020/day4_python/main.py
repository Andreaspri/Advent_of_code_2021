




def part1_and_part2():
    arr = []
    eyeclr = ['amb\n', 'blu\n', 'brn\n', 'gry\n', 'grn\n', 'hzl\n', 'oth\n', 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl',
              'oth']
    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    count1, count12, count13, count14, count15, count16 = 0, 0, 0, 0, 0, 0

    with open("data.txt", "r") as f:
        arr.insert(len(arr), [])
        for i in f.readlines():
            if i == '\n':
                arr.insert(len(arr), [])
                count1 += 1
                continue
            arr[count1].insert(len(arr[count1]), i.split(" "))

    count1 = 0
    for pas in arr:
        for side in pas:
            for ele in side:
                if ele.split(':')[0] in valid:
                    count1 += 1
        if count1 == 7:
            count12 += 1
            for side2 in pas:
                for ele2 in side2:
                    if ele2.split(':')[0] == 'byr' and 1920 <= int(ele2.split(':')[1]) <= 2002:
                        count13 += 1
                    if ele2.split(':')[0] == 'iyr' and 2010 <= int(ele2.split(':')[1]) <= 2020:
                        count13 += 1
                    if ele2.split(':')[0] == 'eyr' and 2020 <= int(ele2.split(':')[1]) <= 2030:
                        count13 += 1

                    if ele2.split(':')[0] == 'hgt' and 'cm' in ele2.split(':')[1]:
                        if 150 <= int(ele2.split(':')[1].split("cm")[0]) <= 193:
                            count13 += 1

                    if ele2.split(':')[0] == 'hgt' and 'in' in ele2.split(':')[1]:
                        if 59 <= int(ele2.split(':')[1].split("in")[0]) <= 76:
                            count13 += 1

                    if ele2.split(':')[0] == 'hcl' and '#' == ele2.split(':')[1][0]:
                        for h in ele2.split(':')[1]:
                            if 0 <= ord(h) - ord('a') <= 5 or -49 <= ord(h) - ord('a') <= -40:
                                count14 += 1
                        if count14 == 6:
                            count13 += 1
                        count14 = 0

                    if ele2.split(':')[0] == 'ecl' and ele2.split(':')[1] in eyeclr:
                        count13 += 1

                    if ele2.split(':')[0] == 'pid':
                        for t in ele2.split(':')[1]:
                            if -49 <= ord(t) - ord('a') <= -40:
                                count15 += 1
                        if count15 == 9:
                            count13 += 1
                        count15 = 0

            if count13 == 7:
                count16 += 1
            count13 = 0
        count1 = 0

    print("Part 1: ", count12)
    print("Part 2: ", count16)

if __name__ == '__main__':
    part1_and_part2()