

# I decided not to use regex for a reason. Regex is cheating on this simple problem.

def part_1(input):
    
    get_numbers = lambda x: [i for i in x if i.isdigit()]

    total = 0
    for line in input:
        numbers = get_numbers(line)
        total += int(numbers[0] + numbers[-1])

    return total




def part_2(input):
    # Finds all numbers in a line
    get_numbers = lambda x: [i for i in x if i.isdigit()]
    
    # Finds first instance of number in line from the left
    get_index = lambda x, y: (y, x.find(y)) if x.find(y) != -1 else None

    # Finds first instance of number in line from the right
    get_index_reverse = lambda x, y: (y, x.rfind(y)) if x.rfind(y) != -1 else None
    
    # Maps number words to numbers
    number_map = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    total = 0
    for line in input:
        
        left = set([get_index(line, number) for number in number_map if get_index(line, number) != None])
        right = set([get_index_reverse(line, number) for number in number_map if get_index_reverse(line, number) != None])

        existing_numbers = sorted(list(left.union(right)), key=lambda x: x[1])    
        
        if len(existing_numbers) > 1:
            line = line[:existing_numbers[-1][1]] + number_map[existing_numbers[-1][0]] + line[existing_numbers[-1][1]:]
            line = line[:existing_numbers[0][1]] + number_map[existing_numbers[0][0]] + line[existing_numbers[0][1]:]
        elif len(existing_numbers) == 1:
            line = line[:existing_numbers[0][1]] + number_map[existing_numbers[0][0]] + line[existing_numbers[0][1]:]
        
        numbers = get_numbers(line)

        total += int(numbers[0] + numbers[-1])
    
    return total



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read().splitlines()

    print("Part 1: ", part_1(input))
    print("Part 2: ", part_2(input))
