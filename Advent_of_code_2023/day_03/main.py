
import re

class Number:
    def __init__(self, value, grid, x: tuple, y:int):
        self.value = value
        self.grid = grid
        self.x = x
        self.y = y
        

    def __repr__(self):
        return f"Number({self.value})"
    
    def __mul__(self, other):
        return self.value * other.value

    def get_neighbours(self):
        neighbours = []
        for x in range(self.x[0]-1, self.x[1]+1):
            if x < 0 or x > len(self.grid[self.y]):
                continue
            for y in range(self.y-1, self.y+2):
                if x == self.x and y == self.y or y < 0 or y > len(self.grid):
                    continue
                try:
                    neighbours.append(self.grid[y][x])
                except IndexError:
                    continue
        return neighbours

    def is_neighbour(self, other: tuple):
        # self.x is a tuple of the start and end index of the number
        # self.y is the line number
        # other is a tuple of the x and y coordinate of the other point
        if other[0] < self.x[0]-1 or other[0] > self.x[1]:
            return False
        if other[1] < self.y-1 or other[1] > self.y+1:
            return False
        return True
        

def parse(lines):
    numbers = []
    for i, line in enumerate(lines):
        matches = [(match.start(), match.group()) for match in re.finditer(r'\d+', line)]
        for match in matches:
            numbers.append(Number(int(match[1]), lines, (match[0], match[0]+len(match[1])), i))
    
    return numbers



def part_1(numbers):
    total = 0
    for number in numbers:
        neighbours = "".join(number.get_neighbours())
        # Check if any of the neighbours are anything else than a digit or a .
        matches = re.findall(r'[^0-9.]', neighbours)
        if matches:
            total += number.value
    return total
            

def part_2(numbers):
    total = 0
    # Just get the stupid grid from one of the numbers
    grid = numbers[0].grid
    for i, line in enumerate(grid):
        gears = [(match.start(), i) for match in re.finditer(r'\*', line)]
        for gear in gears:
            neighbours = []
            for number in numbers:
                if number.is_neighbour(gear):
                    neighbours.append(number)
        
            if len(neighbours) == 2:
                total += neighbours[0] * neighbours[1]
    
    return total




if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    numbers = parse(lines)
    
    print("Part 1:", part_1(numbers)) 
    print("Part 2:", part_2(numbers))