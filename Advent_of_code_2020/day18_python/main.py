with open("data.txt", "r") as f:
    f = f.readlines()

def parapara(string):
    if string.count('(') > 0:
        for i,c in enumerate(string):
            if c == '(':
                left = i
            if c == ')':
                right = i+1
                break
        if string[left:right].count('(') > 1:
            string = string.replace(string[left:right],parapara(string[left:right]))
        else:
            string = string.replace(string[left:right],calc(string[left:right]))
        return parapara(string)
    else:
        return calc(string)


def calc(piece):
    piece = piece.replace(")","").replace("(","")
    piece = piece.split(" ")
    total = 0
    total += int(piece[0])
    i = 3
    while i <= len(piece):
        total = eval(f"{total}{''.join(piece[i-2:i])}")
        i += 2
    return str(total)


def parapara_part2(string):
    if string.count('(') > 0:
        for i,c in enumerate(string):
            if c == '(':
                left = i
            if c == ')':
                right = i+1
                break
        if string[left:right].count('(') > 1:
            string = string.replace(string[left:right],parapara_part2(string[left:right]))
        else:
            string = string.replace(string[left:right],calc_part2(string[left:right]))
        return parapara_part2(string)
    else:
        return calc_part2(string)


def calc_part2(piece):
    piece = pluss(piece.replace(")","").replace("(","").split(" "))
    total = 0
    total += int(piece[0])
    i = 3
    while i <= len(piece):
        total = eval(f"{total}{''.join(piece[i-2:i])}")
        i += 2
    return str(total)



def pluss(liste):
    if '+' not in liste:
        return liste
    i=0
    while i < len(liste):
        if liste[i] == '+':
            liste[i] = str(int(liste[i-1])+int(liste[i+1]))
            liste.pop(i-1)
            liste.pop(i)
        i += 1
    if '+' in liste:
        liste = pluss(liste)
    return liste

total1 = 0
total2 = 0
for line in f:
    total1 += int(parapara(line))
    total2 += int(parapara_part2(line))
print("Part 1:",total1)
print("Part 2:",total2)