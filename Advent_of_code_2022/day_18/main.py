import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))



class Node:
    def __init__(self, point, parent=None):
        self.point = point
        self.parent = parent
        
    def get_children(self, x_max, y_max, z_max):
        x,y,z = self.point
        children = []
        if x >= 0:
            children.append(Node((x-1, y, z), self))
        if x < x_max:
            children.append(Node((x+1, y, z), self))
        if y >= 0:
            children.append(Node((x, y-1, z), self))
        if y < y_max:
            children.append(Node((x, y+1, z), self))
        if z >= 0:
            children.append(Node((x, y, z-1), self))
        if z < z_max:
            children.append(Node((x, y, z+1), self))
        return children

    def __eq__(self, other):
        return self.point == other.point
    
    def __hash__(self):
        return hash(self.point)
    



def part_1(points):
    surface_area = 0
    for i in range(len(points)):
        neighbors = 0
        for j in range(len(points)):
            if i == j:
                continue
            distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) + abs(points[i][2] - points[j][2])
            if distance == 1:
                neighbors += 1
        surface_area += 6 - neighbors
    return surface_area


def part_2(points):
    # 3D bfs to find the surface area
    x_max = max([point[0] for point in points])+1
    y_max = max([point[1] for point in points])+1
    z_max = max([point[2] for point in points])+1
    points = set(points)
    surface = []
    visited = set()
    queue = [Node((0, 0, 0))]
    while queue:
        point = queue.pop(0)
        if point.point in points:
            surface.append(point.parent)
            continue
        if point in visited:
            continue
        visited.add(point)

        queue.extend(point.get_children(x_max, y_max, z_max))
    return len(surface)
        

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
        points = [tuple(map(int, line.split(","))) for line in data]
    print("Part 1:", part_1(points))
    print("Part 2:", part_2(points))