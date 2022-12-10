import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))




def part_1(operations):
    cycles = 0
    x = 1
    signal_strengths = []
    for operation in operations:
        match operation.split(" "):
            case ["addx", value]:
                cycles += 1
                if (cycles-20) % 40 == 0:
                    signal_strengths.append(x*cycles)
                cycles += 1
                if (cycles-20) % 40 == 0:
                    signal_strengths.append(x*cycles)
                x += int(value)

            case ["noop"]:
                cycles += 1
                if (cycles-20) % 40 == 0:
                    signal_strengths.append(x*cycles)
        
    return sum(signal_strengths)




def to_draw_or_not_to_draw(x, cycles):
    if (x-1) <= cycles%40 <= (x+1):
        return "#"
    else:
        return " "


def part_2(operations):
    screen = ["" for _ in range(6)]
    cycles = 0
    x = 1
    for operation in operations:
        match operation.split(" "):
            case ["addx", value]:
                screen[cycles//40] += to_draw_or_not_to_draw(x, cycles)
                cycles += 1

                screen[cycles//40] += to_draw_or_not_to_draw(x, cycles)
                cycles += 1
                
                x += int(value)

            case ["noop"]:
                screen[cycles//40] += to_draw_or_not_to_draw(x, cycles)
                cycles += 1

    print("\n".join(screen))




if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.read().split("\n")

    print("Part 1: ", part_1(data))
    print("Part 2: ")
    part_2(data)