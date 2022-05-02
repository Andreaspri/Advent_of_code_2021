import itertools

with open("data.txt", "r") as f:
    f = f.readlines()
f = [int(f[i]) for i in range(len(f))]

for i in range(len(f)):
    temp = [sum(p) for p in itertools.combinations(f[i:i+25],2)]
    if f[i+25] not in temp:
        special = f[i+25]
        break

for i in range(len(f)): # This is part2
    for j in range(len(f)):
        if sum(f[j:i+j]) == special:
            temp = f[j:i+j]
            temp.sort()
            sum_low_high = temp[0]+temp[len(temp)-1]

print("Part 1: ",special)
print("Part 2: ",sum_low_high)