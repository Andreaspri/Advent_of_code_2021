key1 = 3248366
key2 = 4738476

def find_loop(public):
    value = 1
    loop = 0
    while value != public:
        value *= 7
        value %= 20201227
        loop+=1
    return loop


def find_encrypt(loop,value,key):
    value = 1
    for i in range(loop):
        value *= key
        value %= 20201227
    return value

def part1():
    loop1 = find_loop(key1)
    #loop2 = find_loop(key2)
    return find_encrypt(loop1,key1,key2)

print("Part 1:",part1())