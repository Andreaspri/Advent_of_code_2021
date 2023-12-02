

def parse_input(input):
    # Structure: {game(int): {step(int): {color(str): amount(int)}}}
    games = {}
    for line in input:
        game = int(line.split(":")[0].split(" ")[1])
        steps = line.split(": ")[1].split("; ")
        games[game] = {i:{color.split(" ")[1]:int(color.split(" ")[0]) for color in step.split(", ")} for i, step in enumerate(steps)}

    return games


def part_1(input):
    # Data from AOE
    red = 12
    green = 13
    blue = 14

    total = 0
    for game, steps in input.items():
        for colors in steps.values():
            if colors.get("red", 0) > red or colors.get("green", 0) > green or colors.get("blue", 0) > blue:
                break
        # If the loop didn't break, this else will run
        else:
            total += game
             
    return total


def part_2(input):
    
    total = 0

    for steps in input.values():
        total +=    max([step.get("red", 0) for step in steps.values()]) * \
                    max([step.get("green", 0) for step in steps.values()]) * \
                    max([step.get("blue", 0) for step in steps.values()])
        
    return total



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read().splitlines()
    input = parse_input(input)
    print("Part 1:", part_1(input))
    print("Part 2:", part_2(input))