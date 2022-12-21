import os
import re
import multiprocessing

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def parse_data(data):
    blueprints = {}
    regex = re.compile(r" (\w+) robot costs (\d+) (\w+) ?a?n?d? ?(\d+)? ?(\w+)?")
    for blueprint in data:
        blueprint = blueprint.split(": ")
        name = int(blueprint[0].replace("Blueprint ", ""))
        blueprints[name] = {}
        cost = blueprint[1]
        cost = regex.findall(cost)
        blueprints[name][cost[0][0]] = {cost[0][2]: int(cost[0][1])}
        blueprints[name][cost[1][0]] = {cost[1][2]: int(cost[1][1])}
        blueprints[name][cost[2][0]] = {cost[2][2]: int(cost[2][1]), cost[2][4]: int(cost[2][3])}
        blueprints[name][cost[3][0]] = {cost[3][2]: int(cost[3][1]), cost[3][4]: int(cost[3][3])}

    for blueprint in blueprints:
        max_dict = {}
        for robot in blueprints[blueprint]:
            for material in blueprints[blueprint][robot]:
                max_dict[material] = max(max_dict.get(material, 0), blueprints[blueprint][robot][material])
        blueprints[blueprint]["max"] = max_dict

    return blueprints

def day_19(blueprint, n):
    inventory = {"robots":{"ore": 1, "clay": 0, "obsidian": 0, "geode": 0},
     "materials":{"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}}

    def is_promising(inventory, current_best, n):
        current_geode = inventory["materials"]["geode"]
        current_production = inventory["robots"]["geode"]
        for i in range(n):
            current_production += i%2
            current_geode += current_production
        if current_geode > current_best:
            return True
        return False

            

    def can_build(inventory, blueprint, robot):
        if robot != "geode" and blueprint["max"][robot] < inventory["robots"][robot]+1: 
            return False
        costs = {}
        for material in blueprint[robot]:
            if inventory["materials"][material] < blueprint[robot][material]:
                return False
            else:
                costs[material] = blueprint[robot][material]
        return costs

    best_number_of_geodes = {24:0}
    best_geode = 0

    def dfs(inventory, blueprint, n, new_robot=False):
        nonlocal best_geode
        nonlocal best_number_of_geodes
        for material in inventory["materials"]:
            inventory["materials"][material] += inventory["robots"][material]
        if n == 0:
            if inventory["materials"]["geode"] > best_geode:
                best_geode = inventory["materials"]["geode"]
                print(f"Blueprint: {blueprint[0]} {inventory}")
            return
        # If new robot is to be built it is added to inventory

        if new_robot:
            inventory["robots"][new_robot] += 1
        if n not in best_number_of_geodes:
            best_number_of_geodes[n] = inventory["robots"]["geode"]
        elif best_number_of_geodes[n] > inventory["robots"]["geode"]:
            return
        if not is_promising(inventory, best_geode, n):
            return
        for robot in list(inventory["robots"])[::-1]:
            costs = can_build(inventory, blueprint[1], robot)
            if costs is not False:
                # Removing the materials from inventory
                for material in costs:
                    inventory["materials"][material] -= costs[material]
                dfs({k:{mater: val for mater, val in v.items()} for k, v in inventory.items()}, blueprint, n-1, robot)
                # Putting the materials back in inventory after dfs
                for material in costs:
                    inventory["materials"][material] += costs[material]

                



        dfs({k:{mater: val for mater, val in v.items()} for k, v in inventory.items()}, blueprint, n-1)




    dfs({k:{mater: val for mater, val in v.items()} for k, v in inventory.items()}, blueprint, n-1)

    print("Blueprint :", blueprint[0], "Done")
    return best_geode*blueprint[0]




if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().splitlines()
    blueprints = parse_data(data)

    # Run part 1 with multiprocessing where each blueprint is run in a separate process
    pool = multiprocessing.Pool()
    print("Part 1: ", sum(pool.starmap(day_19, [(blueprint, 24) for blueprint in blueprints.items()])))

    # Only run the three first blueprints
    blueprints = {k:blueprints[k] for k in list(blueprints)[:3]}
    values = pool.starmap(day_19, [(blueprint, 32) for blueprint in blueprints.items()])
    print("Part 2:", values[0]*(values[1]//2)*(values[2]//3))
