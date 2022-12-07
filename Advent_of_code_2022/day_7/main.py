import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))



class File:
    def __init__(self, size = 0, parent=None, is_dir=True):
        self.size = size
        self.children = {}
        self.parent = parent
        self.is_dir = is_dir

    def add_child(self, name, child):
        self.children[name] = child


    def calc_size(self):
        self.size += sum(child.calc_size() for child in self.children.values())
        return self.size

    def go_to_child(self, name):
        return self.children[name]

    def go_to_parent(self):
        return self.parent

    def print_tree(self, indent=0, name='/'):
        for name, child in self.children.items():
            child.print_tree(indent + 4, name)

    def size_of_each_directory(self, sizes=[]):
        for child in self.children.values():
            if child.is_dir:
                sizes.append(child.size)
                child.size_of_each_directory(sizes)
        return sizes
        



def construct_tree(commands):
    head = File()
    current_dir = head
    for command in commands:
        match command.split(' '):
            case ['$', 'cd', *dir]:
                if dir == ['/']:
                    pass
                elif dir == ['..']:
                    current_dir = current_dir.go_to_parent()
                else:
                    current_dir = current_dir.go_to_child(dir[0])
            
            case ['$', 'ls', *dir]:
                pass

            case ['dir', *dir]:
                current_dir.add_child(dir[0], File(parent=current_dir))

            case _ as file:
                size, name = file
                current_dir.add_child(name, File(size=int(size), parent=current_dir, is_dir= False))
   
    head.calc_size()
    return head



def part_1(current):
    total = 0
    for child in current.children.values():
        if child.is_dir:
            total += part_1(child)
    if current.size <= 100000:
        return total + current.size
    
    return total




def part_2(current):
    sizes = current.size_of_each_directory()
    needed_space = 70000000-(filesystem.size+30000000)
    low = 70000000
    current = sizes[0]
    for size in sizes:
        curr_size = size + needed_space
        if curr_size >= 0 and curr_size < low:
            low = curr_size
            current = size

    return current




if __name__ == '__main__':
    with open('data.txt') as f:
        data = f.read().split('\n')
    filesystem = construct_tree(data)
    print("Part 1:", part_1(filesystem))
    print("Part 2:", part_2(filesystem))
