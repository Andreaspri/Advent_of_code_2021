import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))




def part_1(text):
    for i in range(len(text)):
        if len(set(list(text[i:i+4]))) == 4:
            return i + 4



def part_2(text):
    for i in range(len(text)):
        if len(set(list(text[i:i+14]))) == 14:
            return i + 14




if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()


    print("Part 1: ", part_1(data))
    print("Part 2: ", part_2(data))