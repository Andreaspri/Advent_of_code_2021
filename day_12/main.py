



def parse_data():
    with open("data.txt") as f:
        data = f.readlines()

    paths = {}
    for line in data:
        start, stop = line.strip().split("-")
        paths[start] = paths.get(start,[]) + [stop]
        paths[stop] = paths.get(stop,[]) + [start]

    return paths




def part_1(paths, current_position, small_caves_visited):

    if current_position == "end":
        return 1

    total = 0

    for cave in paths[current_position]:
        if cave == "start":
            continue
        elif list(cave)[0] <= 'Z' or cave == "end":
            total += part_1(paths, cave, small_caves_visited)

        elif list(cave)[0] > 'Z' and small_caves_visited.get(cave,0) < 1:
            small_caves_visited[cave] = small_caves_visited.get(cave,0) + 1
            total += part_1(paths,cave, small_caves_visited)
            small_caves_visited[cave] = small_caves_visited.get(cave,0) - 1



    return total




def part_2(paths, current_position, small_caves_visited):
    
    if current_position == "end":
        return 1

    total = 0
    for cave in paths[current_position]:
        if cave == "start":
            continue
        elif list(cave)[0] <= 'Z' or cave == "end":
            total += part_2(paths, cave, small_caves_visited)

        elif list(cave)[0] > 'Z':
            if any(i > 1 for i in small_caves_visited.values()):
                if small_caves_visited.get(cave,0) > 0:
                    continue
            small_caves_visited[cave] = small_caves_visited.get(cave,0) + 1
            total += part_2(paths, cave, small_caves_visited)
            small_caves_visited[cave] = small_caves_visited.get(cave,0) - 1


    return total



if __name__ == '__main__':
    parsed_data = parse_data()
    print(part_1(parsed_data, "start", {}))
    print(part_2(parsed_data, "start", {}))


