def simulate_fish(simulations):
    with open("data.txt") as f:
        data = f.read()
    fish = [int(i) for i in data.split(",")]

    fish_dict = {}

    for i in range(-1, 9):
        fish_dict[i] = 0

    for f in fish:
        fish_dict[f] += 1

    for i in range(simulations):
        for index in range(len(fish_dict) - 1):
            fish_dict[index - 1] = fish_dict[index]
        new_fish = fish_dict[-1]
        fish_dict[-1] = 0
        fish_dict[8] = new_fish
        fish_dict[6] += new_fish




    return sum(fish_dict.values())


if __name__ == '__main__':
    print("Part 1:",simulate_fish(80))
    print("Part 2:",simulate_fish(256))
