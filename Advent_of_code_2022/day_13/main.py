import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def compare(left, right):

    for l, r in zip(left, right):
        if isinstance(l, list) and isinstance(r, list):
            result = compare(l, r)
            if result != None:
                return result

        elif isinstance(l, int) and isinstance(r, list):
            result = compare([l], r)
            if result != None:
                return result


        elif isinstance(l, list) and isinstance(r, int):
            result = compare(l, [r])
            if result != None:
                return result

        elif isinstance(l, int) and isinstance(r, int):
            # This stops the function with the first result check.
            # Even if the lists have more items
            # This was not specified as allowed in the problem
            # But it works for the given input
            if l < r:
                return True
            elif l > r:
                return False

    # Not entirely sure if this is correct
    # But it works for the given input
    # It will end this function by returning false or true without checking the rest of the outer list
    # Unless the lists are the same length
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False




def part_1(pairs):
    correct_pair = 0
    for i, pair in enumerate(pairs):
        left, right = pair
        if compare(left, right):
            correct_pair += i+1

    return correct_pair


def part_2(pairs):
    decoder_packets = [[[2]], [[6]]]
    reduced = sum(pairs, []) + decoder_packets
    
    # Bubble sort based on comparing with compare function
    flag = True
    while flag:
        flag = False
        for j in range(len(reduced)-1):
            if compare(reduced[j+1], reduced[j]):
                reduced[j], reduced[j+1] = reduced[j+1], reduced[j]
                flag = True

    first = reduced.index(decoder_packets[0]) + 1
    second = reduced.index(decoder_packets[1]) + 1

    return first * second


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n\n")
    
    lists = [i.split("\n") for i in data]
    lists = [[eval(j) for j in i] for i in lists]

    print("Part 1:", part_1(lists))
    print("Part 2:", part_2(lists))
