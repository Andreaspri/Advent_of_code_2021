count1 = 0
with open("data.txt", "r") as f:
    g = f.readlines()
    f = [list(i) for i in g]

def part1(count1):
    check = 0
    collection = []
    for y in range(len(f)):
        for x in range(len(f[0])):
            count1 = 0
            leftX = x-1
            rightX = x+1
            uppY = y-1
            downY = y+1

            if f[y][leftX] == '#' and leftX >= 0: count1+=1
            try: 
                if f[y][rightX] == '#' and rightX >= 0: count1+=1 
            except: pass
            for i in range(-1,2):
                posX = x+i
                try:
                    if f[uppY][posX] == '#' and posX >= 0 and uppY >= 0: count1+=1
                except: pass
                try:
                    if f[downY][posX] == '#': count1+=1
                except: pass
            collection.insert(len(collection),(y,x,count1))
    for pos in collection:
        y,x,v = pos
        try:
            if v >= 4 and f[y][x] == '#': 
                f[y][x] = 'L'
                check += 1
        except: pass
        try:
            if v == 0 and f[y][x] == 'L': 
                f[y][x] = '#'
                check += 1
        except: pass
    collection = []
    if check != 0:
        part1(count1)

part1(count1)
for i in f:
        for j in i:
            if j == '#':
                count1 += 1
print('Part 1:',count1)

f = [list(i) for i in g]


def part2(count1):
    check = 0
    collection = []
    for y in range(len(f)):
        for x in range(len(f[0])):
            count1 = 0
            i = 1
            try:
                while f[y][x+i] == '.':
                    i+=1
                if f[y][x+i] == '#': count1+=1
            except: pass

            i = 1
            try:
                while f[y][x-i] == '.':
                    i+=1
                if f[y][x-i] == '#' and x-i >= 0: count1+=1
            except: pass
            i = 1
            try:
                while f[y+i][x] == '.':
                    i+=1
                if f[y+i][x] == '#': count1+=1
            except: pass

            i = 1
            try:
                while f[y-i][x] == '.':
                    i+=1
                if f[y-i][x] == '#' and y-i >= 0: count1+=1
            except: pass
            i = 1
            try:
                while f[y+i][x+i] == '.':
                    i+=1
                if f[y+i][x+i] == '#': count1+=1
            except: pass

            i = 1
            try:
                while f[y-i][x-i] == '.':
                    i+=1
                if f[y-i][x-i] == '#' and x-i >= 0 and y-i >= 0: count1+=1
            except: pass
            i = 1
            try:
                while f[y-i][x+i] == '.':
                    i+=1
                if f[y-i][x+i] == '#' and y-i >= 0: count1+=1
            except: pass
            i = 1
            try:
                while f[y+i][x-i] == '.':
                    i+=1
                if f[y+i][x-i] == '#' and x-i >= 0: count1+=1
            except: pass
            collection.insert(len(collection),(y,x,count1))
    for pos in collection:
        y,x,v = pos
        try:
            if v >= 5 and f[y][x] == '#': 
                f[y][x] = 'L'
                check += 1
        except: pass
        try:
            if v == 0 and f[y][x] == 'L': 
                f[y][x] = '#'
                check += 1
        except: pass
    collection = []
    if check != 0:
        part2(count1)
part2(count1)

count1 = 0


for i in f:
        for j in i:
            if j == '#':
                count1 += 1
print('Part 2:',count1)