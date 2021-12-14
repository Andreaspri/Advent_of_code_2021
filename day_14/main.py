

def parse_data():
    with open("data.txt") as f:
        data = f.readlines()

    rule_pairs = {}
    pairs = {}
    count_dict = {}

    current_string = data.pop(0).strip()
    for i in range(len(current_string)-1):
        first = current_string[i]
        second = current_string[i + 1]
        pairs[first+second] = pairs.get(first+second,0) + 1

    for line in data:
        if " -> " in line:
            pair, char = line.strip().split(" -> ")
            rule_pairs[pair] = char


    for char in current_string:
        count_dict[char] = count_dict.get(char,0) + 1


    return rule_pairs, pairs, count_dict





def day_14(simulations):

    rule_pairs, pairs, count_dict = parse_data()

    for _ in range(simulations):
        new_pairs = {}
        for pair in pairs:
            first, second = list(pair)
            new_pairs[first+rule_pairs[pair]] = new_pairs.get(first+rule_pairs[pair],0) + pairs[pair]
            new_pairs[rule_pairs[pair]+second] = new_pairs.get(rule_pairs[pair]+second,0) + pairs[pair]
            count_dict[rule_pairs[pair]] = count_dict.get(rule_pairs[pair],0) + pairs[pair]

        pairs = new_pairs

    return max(count_dict.values()) - min(count_dict.values())




if __name__ == '__main__':
    print("Part 1:",day_14(10))
    print("Part 2:",day_14(40))

