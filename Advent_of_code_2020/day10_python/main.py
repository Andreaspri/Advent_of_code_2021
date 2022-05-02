jolt1=0
jolt3=0
with open("data.txt", "r") as f:
    f = f.readlines()
f = [int(f[i]) for i in range(len(f))]  
f.append(0)
f.sort()
f.append(f[len(f)-1]+3)

for i in range(1,len(f)):
    if f[i] - f[i-1] == 1:
        jolt1 += 1
    elif f[i] - f[i-1] == 3:
        jolt3 += 1
print("Part 1: ",jolt1*(jolt3))




i=1
current = 1
temp = []
while i < len(f):
    if f[i-1] == f[i]-1:
        temp.append(f[i-1])
    elif f[i-1]+1 != f[i]:
        if len(temp) == 2:
            current *= 2
        elif  len(temp) == 3:
            current *= 4
        elif len(temp) == 4:
            current *= 7
        temp = []
    i+=1

print("Part 2: ",current)
