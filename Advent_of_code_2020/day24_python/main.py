tiles = set()
with open("data.txt") as f:
    f = f.readlines()

for ops in f:
    temp = [0,0] # [W-E,N-S]
    if ops.count('e') - ops.count('se') - ops.count('ne') > 0: 
        temp[0]-= (ops.count('e') - ops.count('se') - ops.count('ne'))*2
    temp[1]-= ops.count('se')
    temp[0]-= ops.count('se')
    temp[1]-= ops.count('sw')
    temp[0]+= ops.count('sw')
    if ops.count('w') - ops.count('sw') - ops.count('nw') > 0: 
        temp[0]+= (ops.count('w') - ops.count('sw') - ops.count('nw'))*2
    temp[1]+= ops.count('nw')
    temp[0]+= ops.count('nw')
    temp[1]+= ops.count('ne')
    temp[0]-= ops.count('ne')
    if (temp[0],temp[1]) in tiles:
        tiles.remove((temp[0],temp[1]))
    else:
        tiles.add((temp[0],temp[1]))

print("Part 1:",len(tiles))


def odd_range():
    for n in range(-100,100):
        yield 2*n + 1

def pair_range():
    for n in range(-100,100):
        yield 2*n
count = 0
y = 0
for i in range(100):
    tempRemove = set()
    tempAdd = set()
    for y in range(-100,100):
        if y % 2 == 0: 
            rng = pair_range()
        else: 
            rng = odd_range()
        for x in rng:
            count = 0
            if (x-1,y-1) in tiles: count += 1 # upper left
            if (x+1,y-1) in tiles: count += 1 # upper right
            if (x-2,y) in tiles: count += 1 # middle left
            if (x+2,y) in tiles: count += 1 # middle right
            if (x-1,y+1) in tiles: count += 1 # lower left
            if (x+1,y+1) in tiles: count += 1 # lower right
            if (x,y) in tiles:
                if count == 0 or count > 2:
                    tempRemove.add((x,y))
            else:
                if count == 2:
                    tempAdd.add((x,y))
    tiles -= tempRemove
    tiles |= tempAdd


print("Part 2:",len(tiles))