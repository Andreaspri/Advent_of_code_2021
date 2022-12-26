import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))



def check_north(state, point):
    x,y = point
    if len([1 for x in range(x-1,x+2) if (x,y-1) in state]) == 0:
        return (x,y-1)

def check_south(state, point):
    x,y = point
    if len([1 for x in range(x-1,x+2) if (x,y+1) in state]) == 0:
        return (x,y+1)

def check_west(state, point):
    x,y = point
    if len([1 for y in range(y-1,y+2) if (x-1,y) in state]) == 0:
        return (x-1,y)

def check_east(state, point):
    x,y = point
    if len([1 for y in range(y-1,y+2) if (x+1,y) in state]) == 0:
        return (x+1,y)


def part_1(state,n):
    checks = [check_north, check_south, check_west, check_east]
    for _ in range(n):
        new_state = dict()
        count_state = dict()
        for point in state:
            possible_locations = list(map(lambda x: x(state, point), checks))
            if all(possible_locations):
                continue
            for new_point in possible_locations:
                if new_point:
                    new_state[point] = new_point
                    count_state[new_point] = count_state.get(new_point, 0) + 1
                    break
        for point, destination in new_state.items():
            if count_state[destination] == 1:
                state.remove(point)
                state.add(destination)

        checks.append(checks.pop(0))


    x_min, x_max = min([x for x,y in state]), max([x for x,y in state])
    y_min, y_max = min([y for x,y in state]), max([y for x,y in state])
    count = 0
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if (x,y) not in state:
                count += 1
    
    return count
    
    
def part_2(state):
    checks = [check_north, check_south, check_west, check_east]
    rounds = 0
    stop_counter = 0
    while True:
        if stop_counter == len(state):
            break
        rounds += 1
        stop_counter = 0
        new_state = dict()
        count_state = dict()
        for point in state:
            possible_locations = list(map(lambda x: x(state, point), checks))
            if all(possible_locations):
                stop_counter += 1
                continue
            for new_point in possible_locations:
                if new_point:
                    new_state[point] = new_point
                    count_state[new_point] = count_state.get(new_point, 0) + 1
                    break


            continue
        for point, destination in new_state.items():
            if count_state[destination] == 1:
                state.remove(point)
                state.add(destination)

        checks.append(checks.pop(0))


    return rounds


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().splitlines()

    data = set([(x,y) for y, line in enumerate(data) for x, char in enumerate(line) if char == "#"])

    print("Part 1:", part_1(data,10))
    print("Part 2:", part_2(data)-10)