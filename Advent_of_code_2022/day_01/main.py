import os



os.chdir(os.path.dirname(os.path.abspath(__file__)))



def sum_elfs(data):
    nums = []
    total = 0
    for i in data:
        if i != '\n':
            total += int(i)
        else:
            nums.append(total)
            total = 0
    return nums

if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    calories = sum_elfs(data)
    calories.sort(reverse=True)
    print("Part 1:", calories[0])
    print("Part 2:", sum(calories[:3]))