with open("data.txt") as f:
    f = f.readlines()
    f = [line.strip() for line in f]



borders = {}
total = []
for i in range(len(f)):
    if 'Tile' in f[i]:
        tileID = int(f[i].split(" ")[1].split(":")[0])
        borders[tileID] = []
        borders[tileID].append(f[i+1])
        borders[tileID].append(f[i+10])
        total.append(f[i+10])
        total.append(f[i+1])
        tempR = []
        tempL = []
        for j in range(10):
            tempR.append(f[i+j+1][-1])
            tempL.append(f[i+j+1][0])
        borders[tileID].append("".join(tempR))
        borders[tileID].append("".join(tempL))
        total.append("".join(tempR))
        total.append("".join(tempL))



for key,value in borders.items():
    count = 0
    for border in value:
        if total.count(border) < 2:
            count += 1
    if count == 2:
        print(key)


