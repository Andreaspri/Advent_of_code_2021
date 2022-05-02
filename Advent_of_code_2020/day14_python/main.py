import copy
import itertools
import re

find_numbers = re.compile("\d+] = \d+")
with open("data.txt", "r") as f:
    f = f.readlines()

def part1():  
    collection = {}
    for line in f:
        decimal = 0
        if line.startswith('mask'): mask = line.split(" = ")[1].replace('\n','')
        else:
            mem,val = "".join(find_numbers.findall(line)).split("] = ")
            val = list(bin(int(val)).replace('0b',''))
            [val.insert(0,'0') for i in range(len(mask) - len(val))]
            [[val.pop(i),val.insert(i,x)] for i,x in enumerate(mask) if x != 'X']
            for digit in val: decimal = decimal*2 + int(digit)
            collection[mem] = decimal
    return sum(collection.values())

def part2():
    collection = {}
    for line in f:
        if line.startswith('mask'): mask = line.split(" = ")[1].replace('\n','')
        else:
            mem,val = "".join(find_numbers.findall(line)).split("] = ")
            mem = list(bin(int(mem)).replace('0b',''))
            [mem.insert(0,'0') for i in range(len(mask) - len(mem))]
            liste = [[1,0] for i in mask if i == 'X']
            for solutions in list(itertools.product(*liste)):
                temp_mem = copy.deepcopy(mem)
                i = 0
                for index,x in enumerate(mask):
                    if x == 'X':
                        temp_mem[index] = solutions[i]
                        i+=1
                    elif x == '0': continue
                    elif x == '1': temp_mem[index] = x
                decimal = 0
                for digit in temp_mem: decimal = decimal*2 + int(digit)
                collection[decimal] = int(val)
    return sum(collection.values())

print("Part 1:",part1())
print("Part 2:",part2())