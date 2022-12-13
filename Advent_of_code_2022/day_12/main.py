import os
import heapq


os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Node:
    def __init__(self, x, y, depth, parent = None):
        self.x = x
        self.y = y
        self.depth = depth
        self.cost =  self.depth + self.calculate_cost()
        self.parent = parent

    def get_neighbours(self):
        return [Node(self.x+1, self.y, self.depth+1, self), Node(self.x-1, self.y, self.depth+1, self),\
             Node(self.x, self.y+1, self.depth+1, self), Node(self.x, self.y-1, self.depth+1, self)]

    def is_valid(self, parent, grid):
        if self.x < 0 or self.y < 0 or self.x >= len(grid) or self.y >= len(grid[0]):
            return False
        if grid[parent.x][parent.y] == "S":
            return True
        if (ord(grid[parent.x][parent.y]) - ord(grid[self.x][self.y])) < -1:
            return False
        if grid[self.x][self.y] == "E" and grid[parent.x][parent.y] != "z":
            return False
        return True

    def overwrite_node(self, other):
        self.cost = other.cost
        self.parent = other.parent
        self.depth = other.depth

    def calculate_cost(self):
        return abs(self.x - GOAL[0]) + abs(self.y - GOAL[1])

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def day_12(start, grid):
    nodes = [start]
    # nodes_lookup is used to access the nodes in the heap and check if they are already visited
    nodes_lookup = {start: start}
    while nodes:
        node = heapq.heappop(nodes)
        if grid[node.x][node.y] == "E":
            return node.depth

        for neighbour in node.get_neighbours():
            if neighbour in nodes_lookup and neighbour < nodes_lookup[neighbour]:
                nodes_lookup[neighbour].overwrite_node(neighbour)
                # Need to heapify after changing the cost of a node internaly
                heapq.heapify(nodes)

            elif neighbour.is_valid(node, grid) and neighbour not in nodes_lookup:
                nodes_lookup[neighbour] = neighbour
                heapq.heappush(nodes, neighbour)

            # Else discard the node
                
                

if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n")

    gl = [(k, i.find("E")) for k, i in enumerate(data) if "E" in i]
    GOAL = (gl[0][0], gl[0][1])
    start = [(k, i.find("S")) for k, i in enumerate(data) if "S" in i]
    start = Node(start[0][0], start[0][1], 0)

    print("Part 1:", day_12(start, data))

    start = sum([[(x,y) for y, char in enumerate(char_list) if char == "a" or char == "S"]for x, char_list in enumerate(data)], [])
    
    part_2 = [i for i in [day_12(Node(str_pos[0], str_pos[1], 0), data) for str_pos in start] if i is not None]
    print("Part 2:", min(part_2))

