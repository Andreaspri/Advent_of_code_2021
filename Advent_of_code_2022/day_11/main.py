import os
from copy import deepcopy


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def make_monkeys(data):
    monekys = {}

    for line in data:
        line = line.split("\n")
        monkey_id = int(line[0].split(":")[0].split(" ")[1])
        starting_items = [int(i)for i in line[1].split(":")[1].split(",")]
        operation = line[2].split("= ")[1]
        test = int(line[3].split(" ")[-1])
        true = int(line[4].split(" ")[-1])
        false = int(line[5].split(" ")[-1])
    
        monekys[monkey_id] = {
            "starting_items": starting_items,
            "operation": operation,
            "test": test,
            "true": true,
            "false": false,
            "inspections": 0
        }

    return monekys


def part_1(monkeys, n):
    for i in range(n):
        for monkey in monkeys:
            while monkeys[monkey]["starting_items"]:
                old = monkeys[monkey]["starting_items"].pop(0)
                new = eval(monkeys[monkey]["operation"])
                new //= 3
                if new % monkeys[monkey]["test"] == 0:
                    monkeys[monkeys[monkey]["true"]]["starting_items"].append(new)
                else:
                    monkeys[monkeys[monkey]["false"]]["starting_items"].append(new)
                
                monkeys[monkey]["inspections"] += 1
    
    most_inspected = sorted(monkeys.items(), key=lambda x: x[1]["inspections"], reverse=True)
    return most_inspected[0][1]["inspections"] * most_inspected[1][1]["inspections"]
    


def modify(monkeys):
    tests = [monkeys[i]["test"] for i in monkeys]
    for monkey in monkeys:
        temp_lst = []
        for value in monkeys[monkey]["starting_items"]:
            temp = {}
            for test in tests:
                temp[test] = value
            temp_lst.append(temp)
        monkeys[monkey]["starting_items"] = temp_lst




def part_2(monkeys, n):
    for i in range(n):
        for monkey in monkeys:
            while monkeys[monkey]["starting_items"]:
                old = monkeys[monkey]["starting_items"].pop(0)

                if "+" in monkeys[monkey]["operation"]:
                    for i in old:
                        old[i] += int(monkeys[monkey]["operation"].split("+ ")[-1])
                    
                elif "*" in monkeys[monkey]["operation"]:
                    num_old = monkeys[monkey]["operation"].split(" * ").count("old")
                    if num_old == 1:
                        for i in old:
                            old[i] *= int(monkeys[monkey]["operation"].split(" * ")[-1])
                    else:
                        for i in old:
                            old[i] *= old[i]

                # Use modulus on all values
                for i in old:
                    old[i] %= i
                


                if old[monkeys[monkey]["test"]] == 0:
                    monkeys[monkeys[monkey]["true"]]["starting_items"].append(old)
                else:
                    monkeys[monkeys[monkey]["false"]]["starting_items"].append(old)
                
                monkeys[monkey]["inspections"] += 1
    

    most_inspected = sorted(monkeys.items(), key=lambda x: x[1]["inspections"], reverse=True)
    return most_inspected[0][1]["inspections"] * most_inspected[1][1]["inspections"]





if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n\n")
    monkeys = make_monkeys(data)

    print(part_1(deepcopy(monkeys), 20))

    modify(monkeys)

    print(part_2(monkeys, 10000))