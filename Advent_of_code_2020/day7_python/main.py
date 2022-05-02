import re

outer = re.compile(r'^([\w\s]+) ')
inner = re.compile(r'(\d) ([\w\s]+) ')

collection = {}
all_bags = set()

with open("data.txt","r") as f:
    for i in f.readlines():
        i = i.split(" contain ")
        tempouter = outer.findall(i[0])
        tempinner = inner.findall(i[1])
        collection.update({tempouter[0]:{}})
        for j in tempinner:
            collection[tempouter[0]].update({j[1]:j[0]})

def part1(color):
    temp = set()
    global all_bags
    temp = set([bags for bags in collection if color in collection[bags]])
    all_bags |= temp
    [part1(bags) for bags in temp]
    return len(all_bags)

def part2(color):
    total = 1
    for bags in collection[color]:
        value = int(collection[color][bags])
        total += value * part2(bags)
    return total


print("Part 1: ",part1('shiny gold'))
print("Part 2: ",part2('shiny gold')-1)