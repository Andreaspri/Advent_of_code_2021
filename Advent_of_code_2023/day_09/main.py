

def parse_data() -> list:
    with open("input.txt") as f:
        data = f.readlines()
    return [[int(num) for num in nums.split(" ")] for nums in data]



def part1(numbers: list):

    def get_pred(rng: list[int]):
        
        if rng[-1] == 0:
            return 0
        elif len(rng) == 1:
            return rng[0]
        
        new_rng = [rng[i+1]-rng[i] for i in range(0,len(rng)-1,1)]

        return rng[-1] + get_pred(new_rng)

    total = 0

    for num_rng in numbers:
        total += get_pred(num_rng)

    return total


def part2(numbers: list):

    def get_pred(rng: list[int]):
        
        if len(rng) == 1:
            return rng[0]
        
        new_rng = [rng[i+1]-rng[i] for i in range(0,len(rng)-1,1)]

        return rng[0] - get_pred(new_rng)

    total = 0

    for num_rng in numbers:
        total += get_pred(num_rng)

    return total



if __name__=='__main__':
    number_rngs = parse_data()

    print("Part 1:", part1(number_rngs))
    print("Part 2:", part2(number_rngs))

