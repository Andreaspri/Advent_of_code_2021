import re

placement = []
ticket = []
pairs = {}
valids = set()
nearby_tic = []
start = False
error = 0
count1 = 0
count = 0
cnt = 1
with open("data.txt", "r") as f:
    f = f.readlines()

valid = re.compile("(\d+)-(\d+) or (\d+)-(\d+)")
name = re.compile("^[a-z]+ ?\w?\w?\w?")


for i in range(len(f)):
    try: 
        pairs.update({name.findall(f[i])[0]:set()})
        if name.findall(f[i])[0] != 'your tic' and name.findall(f[i])[0] != 'nearby tic':
            placement.append([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    except: pass
    cnt = 1
    try:
        while cnt <= 3:
            count1 = int(valid.findall(f[i])[0][cnt-1])
            while count1 <=  int(valid.findall(f[i])[0][cnt]):
                pairs[name.findall(f[i])[0]].add(count1)
                count1+=1
            cnt += 2
    except: pass
    try: 
        if name.findall(f[i])[0] == 'your tic':
            pairs[name.findall(f[i])[0]] = f[i+1].replace("\n","").split(",")
    except: pass
    try: 
        if name.findall(f[i])[0] == 'nearby tic': break
    except: pass


for i in range(len(f)):
    cnt = 1
    try:
        while cnt <= 3:
            count = int(valid.findall(f[i])[0][cnt-1])
            while count <=  int(valid.findall(f[i])[0][cnt]):
                valids.add(count)
                count+=1
            cnt += 2
    except: pass
    if f[i] == 'nearby tickets:\n':
        start = True
        continue
    if start:
        count = 0
        for rands in f[i].replace("\n","").split(","):
            if int(rands) not in valids:
                error += int(rands)
                count += 1
        if count >= 1: continue 
        nearby_tic.append(f[i].replace("\n","").split(","))

for tickets in nearby_tic:
    some = 0
    for k,v in pairs.items():
        if k == 'your tic' or k == 'nearby tic': continue
        for index,nums in enumerate(tickets):
            if int(nums) not in v:
                try: placement[some].remove(index)
                except: pass
        some +=  1
lalala = 0
for p in range(20):
    for i in placement:
        if len(i) == 1:
            for j in placement:
                if len(j) != 1:
                    try:
                        j.remove(i[0])
                    except: pass
    lalala += 1
total = 1
for i in range(6):
    total *= int(pairs['your tic'][placement[i][0]])
print("Part 1:",error)
print("Part 2:",total)