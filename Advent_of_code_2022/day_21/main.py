import os
import sympy


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def part_1(monkey):
    if isinstance(monkeys[monkey], str):
        if '+' in monkeys[monkey]:
            a, b = monkeys[monkey].split(" + ")
            return part_1(a) + part_1(b)
        elif '-' in monkeys[monkey]:
            a, b = monkeys[monkey].split(" - ")
            return part_1(a) - part_1(b)
        elif '*' in monkeys[monkey]:
            a, b = monkeys[monkey].split(" * ")
            return part_1(a) * part_1(b)
        elif '/' in monkeys[monkey]:
            a, b = monkeys[monkey].split(" / ")
            return part_1(a) / part_1(b)
    else:
        return monkeys[monkey]


def part_2():
    def make_equation(monkey):
        if isinstance(monkeys[monkey], str):
            if '+' in monkeys[monkey]:
                a, b = monkeys[monkey].split(" + ")
                a = make_equation(a)
                b = make_equation(b)
                if isinstance(a, str) or isinstance(b, str):
                    return f"({a}) + ({b})"
                else:
                    return a + b

            elif '-' in monkeys[monkey]:
                a, b = monkeys[monkey].split(" - ")
                a = make_equation(a)
                b = make_equation(b)
                if isinstance(a, str) or isinstance(b, str):
                    return f"({a}) - ({b})"
                else:
                    return a - b
            elif '*' in monkeys[monkey]:
                a, b = monkeys[monkey].split(" * ")
                a = make_equation(a)
                b = make_equation(b)
                if isinstance(a, str) or isinstance(b, str):
                    return f"({a}) * ({b})"
                else:
                    return a * b
            elif '/' in monkeys[monkey]:
                a, b = monkeys[monkey].split(" / ")
                a = make_equation(a)
                b = make_equation(b)
                if isinstance(a, str) or isinstance(b, str):
                    return f"({a}) / ({b})"
                else:
                    return a / b
            elif '=' in monkeys[monkey]:
                a, b = monkeys[monkey].split(" = ")
                return f"{make_equation(a)} - {make_equation(b)}"
            elif monkeys[monkey] == "x":
                return "x"
        else:
            return monkeys[monkey]

    equation = make_equation("root")
    x = sympy.Symbol("x")
    return sympy.solve(equation, x)[0]


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().splitlines()

    monkeys = {}
    for line in data:
        monkey, rest = line.split(": ")
        try:
            monkeys[monkey] = int(rest)
        except:
            monkeys[monkey] = rest

    print("Part 1:", int(part_1("root")))
    
    monkeys["root"] = monkeys["root"].replace(" + ", " = ")
    monkeys["humn"] = "x"

    print("Part 2:", int(part_2()))