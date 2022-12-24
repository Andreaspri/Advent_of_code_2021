import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


    def __repr__(self):
        return f"Node({self.value})"
    
    def __hash__(self) -> int:
        return hash(self.id)
    

class LList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.lookup = {}

    def __repr__(self):
        return f"LList({self.head}, {self.tail}, {self.size})"

    def append(self, value, i):
        node = Node(value)
        self.lookup[i] = node

        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size += 1

    def move_node(self, node, steps):
        steps = steps%(self.size-1)
        if steps == 0:
            return

        current = node
        current.prev.next = current.next
        current.next.prev = current.prev
        for _ in range(steps):
            node = node.next

        node.next.prev = current
        current.next = node.next
        node.next = current
        current.prev = node

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        return self.lookup[i]


    def __repr__(self) -> str:
        display = []
        node = self.head
        for _ in range(self.size):
            display.append(str(node.value))
            node = node.next
        return str(display)

    def find_zero(self):
        node = self.head
        for _ in range(self.size):
            if node.value == 0:
                return node
            node = node.next

    def get_value(self, node, steps):
        current = node
        for _ in range(steps):
            current = current.next
        return current.value


def part_1(l_list):
    for i in range(len(l_list)):
        current = l_list[i]
        l_list.move_node(current, current.value)
    zero = l_list.find_zero()
    
    return l_list.get_value(zero, 1000) + l_list.get_value(zero, 2000) + l_list.get_value(zero, 3000)


def part_2(l_list):
    for _ in range(10):
        for i in range(len(l_list)):
            current = l_list[i]
            l_list.move_node(current, current.value)
    zero = l_list.find_zero()
    
    return l_list.get_value(zero, 1000) + l_list.get_value(zero, 2000) + l_list.get_value(zero, 3000)



if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().splitlines()
    ll = LList()
    for i, num in enumerate(data):
        ll.append(int(num), i)

    print("Part 1:", part_1(ll))

    input_number = 811589153
    ll2 = LList()
    for i, num in enumerate(data):
        ll2.append(int(num)*input_number, i)

    print("Part 2:", part_2(ll2))

    # 11589 too high