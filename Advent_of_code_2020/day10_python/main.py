
def day10_part1(arr):
    arr.sort()
    jolt1 = 1
    jolt3 = 1
    try:
        for i,num in enumerate(arr):
            jolt = arr[i+1]-num
            if jolt == 1:
                jolt1 += 1
            elif jolt == 3:
                jolt3 += 1

    except IndexError:
        return jolt1 * jolt3


def day10_part2(arr):
    arr.sort()
    arr.insert(0,0)
    arr.append(arr[-1]+3)
    count = 0
    combinations = 1
    for i,num in enumerate(arr):
        try:
            if arr[i+1]-num == 1:
                count += 1
            elif arr[i+1]-num != 1:

                if count == 2:
                    combinations *= 2
                elif count == 3:
                    combinations *= 4
                elif count == 4:
                    combinations *= 7
                count = 0

        except IndexError:

            return combinations

if __name__ == '__main__':
    with open("data.txt", "r") as f:
        nums = f.readlines()
    nums = [int(i) for i in nums]
    print("Part 1:",day10_part1(nums))
    print("Part 2:",day10_part2(nums))