import os
import re
os.chdir(os.path.dirname(os.path.abspath(__file__)))



def flip_part_1(row, col, direction, grid):
    if direction == "W":
            new_col_dot = len(grid[row]) -1 - grid[row][::-1].index(".")
            new_col_hash = len(grid[row]) -1 - grid[row][::-1].index("#")
            if new_col_dot > new_col_hash:
                new_col = new_col_dot
            else:
                new_col = new_col_hash
            if grid[row][new_col] == ".":
                return row, new_col

    elif direction == "E":
        new_col_dot = grid[row].index(".")
        new_col_hash = grid[row].index("#")
        if new_col_dot < new_col_hash:
            new_col = new_col_dot
        else:
            new_col = new_col_hash
        if grid[row][new_col] == ".":
            return row, new_col

    elif direction == "N":
        col_list = [r[col] for r in grid]
        new_row_dot = len(col_list) -1 - col_list[::-1].index(".")
        new_row_hash = len(col_list) -1 - col_list[::-1].index("#")
        if new_row_dot > new_row_hash:
            new_row = new_row_dot
        else:
            new_row = new_row_hash
        if grid[new_row][col] == ".":
            return new_row, col

    elif direction == "S":
        col_list = [r[col] for r in grid]
        new_row_dot = col_list.index(".")
        new_row_hash = col_list.index("#")
        if new_row_dot < new_row_hash:
            new_row = new_row_dot
        else:
            new_row = new_row_hash
        if grid[new_row][col] == ".":
            return new_row, col



def move(grid, row, col, direction):

    if direction == "W":
        col -= 1
    elif direction == "E":
        col += 1
    elif direction == "N":
        row -= 1
    elif direction == "S":
        row += 1

    
    if  0 <= row < len(grid) and 0 <= col < len(grid[row]):
        if grid[row][col] == "#":
            return None
        elif grid[row][col] == ".":
            return row, col
        else:
            return flip_part_1(row, col, direction, grid)

            
    else:
        return flip_part_1(row, col, direction, grid)



def change_direction(direction, turn):
    if turn == "L":
        if direction == "W":
            return "S"
        elif direction == "S":
            return "E"
        elif direction == "E":
            return "N"
        elif direction == "N":
            return "W"
    elif turn == "R":
        if direction == "W":
            return "N"
        elif direction == "N":
            return "E"
        elif direction == "E":
            return "S"
        elif direction == "S":
            return "W"
        
    

def part_1(grid, movements):
    move_values = {"W": 2, "E": 0, "N": 3, "S": 1}
    row = 0
    column = grid[row].index(".")
    direction = "E"
    moves = set()

    for movement in movements:
        if isinstance(movement, int):
            for _ in range(movement):
                new_pos = move(grid, row, column, direction)
                if new_pos is not None:
                        row, column = new_pos
                        moves.add((row, column, direction))
                else:
                    break
        else:
            direction = change_direction(direction, movement)

    return 1000*(row+1) + (column+1) * 4 + move_values[direction]




def flip_part_2(row, col, direction, grid):
    if direction == "W":
        if 0 <= row < 50 and col == 50:
            row = 149 - row
            col = 0
            direction = "E"
            if grid[row][col] == ".":
                return row, col, direction
        elif 50 <= row < 100 and col == 50:
            col = row - 50
            row = 100
            direction = "S"
            if grid[row][col] == ".":
                return row, col, direction
        elif 100 <= row < 150 and col == 0:
            row = 149 - row
            col = 50
            direction = "E"
            if grid[row][col] == ".":
                return row, col, direction
        elif 150 <= row < 200 and col == 0:
            col = 50 + (row - 150)
            row = 0
            direction = "S"
            if grid[row][col] == ".":
                return row, col, direction

    elif direction == "E":
        if 0 <= row < 50 and col == 149:
            row = 149 - row
            col = 99
            direction = "W"
            if grid[row][col] == ".":
                return row, col, direction
        elif 50 <= row < 100 and col == 99:
            col = row + 50
            row = 49
            direction = "N"
            if grid[row][col] == ".":
                return row, col, direction
        elif 100 <= row < 150 and col == 99:
            row = 149 - row
            col = 149
            direction = "W"
            if grid[row][col] == ".":
                return row, col, direction
        elif 150 <= row < 200 and col == 49:
            col = row - 100
            row = 149
            direction = "N"
            if grid[row][col] == ".":
                return row, col, direction

    elif direction == "N":
        if 0 <= col < 50 and row == 100:
            row = 50 + col
            col = 50
            direction = "E"
            if grid[row][col] == ".":
                return row, col, direction
        elif 50 <= col < 100 and row == 0:
            row = 100 + col
            col = 0
            direction = "E"
            if grid[row][col] == ".":
                return row, col, direction
        elif 100 <= col < 150 and row == 0:
            col = col - 100
            row = 199
            if grid[row][col] == ".":
                return row, col, direction

    elif direction == "S":
        if 0 <= col < 50 and row == 199:
            col = 100 + col
            row = 0
            if grid[row][col] == ".":
                return row, col, direction
        elif 50 <= col < 100 and row == 149:
            row = col + 100
            col = 49
            direction = "W"
            if grid[row][col] == ".":
                return row, col, direction
        elif 100 <= col < 150 and row == 49:
            row = col - 50
            col = 99
            direction = "W"
            if grid[row][col] == ".":
                return row, col, direction




def move_part_2(grid, row, col, direction):

    if direction == "W":
        col -= 1
    elif direction == "E":
        col += 1
    elif direction == "N":
        row -= 1
    elif direction == "S":
        row += 1

    if  0 <= row < len(grid) and 0 <= col < len(grid[row]):
        if grid[row][col] == "#":
            return None
        elif grid[row][col] == ".":
            return (row, col, direction)


def part_2(grid, movements):
    move_values = {"W": 2, "E": 0, "N": 3, "S": 1}
    row = 0
    column = grid[row].index(".")
    direction = "E"
    moves = set()

    for movement in movements:
        if isinstance(movement, int):
            for _ in range(movement):
                new_pos = flip_part_2(row, column, direction, grid)
                if new_pos is not None:
                        row, column, direction = new_pos
                        moves.add((row, column, direction))
                else:
                    new_pos = move_part_2(grid, row, column, direction)
                    if new_pos is not None:
                        row, column, direction = new_pos
                        moves.add((row, column, direction))
                    else:
                        break
        else:
            direction = change_direction(direction, movement)


    return 1000*(row+1) + (column+1) * 4 + move_values[direction]




if __name__ == "__main__":
    with open("data.txt") as f:
        grid_data, movements = f.read().split("\n\n")
    

    
    grid = []
    for line in grid_data.splitlines():
        grid.append(list(line))

    max_len = max([len(x) for x in grid])
    for i in range(len(grid)):
        grid[i] += [" "] * (max_len - len(grid[i]))

    movements = re.split("(\d+)", movements)
    movements = [x for x in movements if x != ""]
    movements = [int(x) if x.isdigit() else x for x in movements]

    print("Part 1:", part_1(grid, movements))


    print("Part 2:", part_2(grid, movements))

