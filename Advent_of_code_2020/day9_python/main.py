
def check_target(integer_list, target_num):
    dict_integers = dict()
    for i,num in enumerate(integer_list):
        dict_integers[num] = dict_integers.get(num,i)
        complement = target_num - num
        if complement in dict_integers:
            if complement == num and dict_integers[complement] != i or complement != num:
                return True

    return False


def day9_part1(arr,preamble):
    for i in range(preamble,len(arr)-preamble):
        if not check_target(arr[i:preamble+i],arr[preamble+i]):
            return arr[preamble+i]


def day9_part2(arr,target):
    n = 3
    while True:
        for p in range(len(arr)):
            sliced_arr = arr[p:n+p]
            if sum(sliced_arr) == target:
                return min(sliced_arr) + max(sliced_arr)

        n += 1

if __name__ == '__main__':

    with open("data.txt","r") as f:
        data = [int(i) for i in f.readlines() if i != '\n']

    part1 = day9_part1(data,25)
    part2 = day9_part2(data,part1)

    print("Part 1:",part1)
    print("Part 2:",part2)