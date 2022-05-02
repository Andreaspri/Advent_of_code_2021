

import re


def parse(input_data):
    rules = {}
    possible_solutions = []

    for line in input_data:
        if '0' <= line[0] <= '9':
            rules[line.split(': ')[0].strip()] = line.split(': ')[1].strip()
        elif line != '\n':
            possible_solutions.append(line.strip())

    return rules,possible_solutions


def find_rule(rule, rules, depth=0):
    if depth > 15:
        return ""
    if rule == 'a':
        return 'a'
    elif rule == 'b':
        return 'b'
    if isinstance(rule, list):
        return rule
    updated_rules = rule.split(' ')
    for i in range(len(updated_rules)):
        if updated_rules[i] in rules.keys():
            updated_rules[i] = find_rule(rules[updated_rules[i]], rules,depth+1)

    return updated_rules


def day19_part1_and_part2(rules, possible_solutions):


    rules['0'] = find_rule(rules['0'], rules)

    solution_reg = str(rules['0']).replace(']',')').replace('[','(').replace(',','').replace("'",'').replace(' ','').replace('"','')

    count = 0
    for solution in possible_solutions:
        if re.match(solution_reg, solution):
            if re.match(solution_reg, solution).group() == solution:
                count += 1

    return count


if __name__ == '__main__':
    with open("data.txt", "r") as f:
        data = f.readlines()
    rls,psb = parse(data)
    print(day19_part1_and_part2(rls.copy(),psb))
    rls['8'] = '42 | 42 8'
    rls['11'] = '42 31 | 42 11 31'
    print(day19_part1_and_part2(rls,psb))
