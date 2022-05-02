

class Node:

    def __init__(self, cost, position, goal):
        self.cost = cost
        self.position = position
        self.goal = goal


    def __eq__(self, other):
        return self.position == other.position

    def is_winner(self):
        return self.goal == self.position


    def move_up(self,maze):
        if self.position[0] -1 < 0:
            return False

        new_position = (self.position[0]-1,self.position[1])


        return Node(self.cost+maze[self.position[0]-1][self.position[1]],new_position, self.goal)

    def move_down(self, maze):
        if self.position[0] + 1 >= len(maze):
            return False

        new_position = (self.position[0]+1, self.position[1])

        return Node(self.cost + maze[self.position[0]+1][self.position[1]], new_position, self.goal)

    def move_left(self, maze):
        if self.position[1] - 1 < 0:
            return False

        new_position = (self.position[0], self.position[1]-1)


        return Node(self.cost + maze[self.position[0]][self.position[1]-1], new_position, self.goal)

    def move_right(self, maze):
        if self.position[1] + 1 >= len(maze[0]):
            return False

        new_position = (self.position[0], self.position[1] + 1)

        return Node(self.cost + maze[self.position[0]][self.position[1]+1],new_position, self.goal)






def part_1():
    with open("data.txt") as f:
        data = f.readlines()

    maze = [[int(p) for p in i.strip()] for i in data]


    open_list = [Node(0,(0,0),(len(maze)-1,len(maze[0])-1))]
    closed_list = []
    while open_list:
        open_list.sort(key=lambda x: x.cost)
        current_node = open_list.pop(0)
        closed_list.append(current_node)

        up_node = current_node.move_up(maze)
        down_node = current_node.move_down(maze)
        left_node = current_node.move_left(maze)
        right_node = current_node.move_right(maze)

        if up_node and up_node not in open_list and up_node not in closed_list:
            if up_node.is_winner():
                return up_node.cost
            open_list.append(up_node)

        if down_node and down_node not in open_list and down_node not in closed_list:
            if down_node.is_winner():
                return down_node.cost
            open_list.append(down_node)

        if left_node and left_node not in open_list and left_node not in closed_list:
            if left_node.is_winner():
                return left_node.cost
            open_list.append(left_node)

        if right_node and right_node not in open_list and right_node not in closed_list:
            if right_node.is_winner():
                return right_node.cost
            open_list.append(right_node)

    print("shit...")




def part_2():
    with open("data.txt") as f:
        data = f.readlines()

    maze = [[int(p) for p in i.strip()] for i in data]

    for row in range(len(maze)):
        for col in range(len(maze[row])*4):
            new_val = maze[row][col] + 1
            if new_val > 9:
                new_val = 1
            maze[row].append(new_val)


    for row in range(len(maze)*4):
        maze.append([])
        for col in range(len(maze[row])):
            new_val = maze[row][col] + 1
            if new_val > 9:
                new_val = 1
            maze[len(maze)-1].append(new_val)


    open_list = [Node(0,(0,0),(len(maze)-1,len(maze[0])-1))]
    closed_list = []
    while open_list:
        open_list.sort(key=lambda x: x.cost)
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        print(len(maze)-1-current_node.position[0]+len(maze)-1-current_node.position[1])

        up_node = current_node.move_up(maze)
        down_node = current_node.move_down(maze)
        left_node = current_node.move_left(maze)
        right_node = current_node.move_right(maze)

        if up_node and up_node not in open_list and up_node not in closed_list:
            if up_node.is_winner():
                return up_node.cost
            open_list.append(up_node)

        if down_node and down_node not in open_list and down_node not in closed_list:
            if down_node.is_winner():
                return down_node.cost
            open_list.append(down_node)

        if left_node and left_node not in open_list and left_node not in closed_list:
            if left_node.is_winner():
                return left_node.cost
            open_list.append(left_node)

        if right_node and right_node not in open_list and right_node not in closed_list:
            if right_node.is_winner():
                return right_node.cost
            open_list.append(right_node)

    print("shit...")




if __name__ == '__main__':
    print(part_1())

    #print(part_2())
