import re



def part_1(input):
    total = 0
    # Regex to extract the numbers after 1: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 into two groups of numbers
    regex = "Card *\d+: +([\d ]*) \| ([\d ]*)"
    for line in input:
        numbers = re.findall(regex, line)
        winning_numbers = numbers[0][0].split(" ")
        your_numbers = numbers[0][1].split(" ")
        # Remove empty strings
        winning_numbers = list(filter(None, winning_numbers))
        your_numbers = list(filter(None, your_numbers))
        winning_numbers = list(map(int, winning_numbers))
        your_numbers = list(map(int, your_numbers))
        
        # Find number of matching numbers
        score = 0
        for number in winning_numbers:
            if number in your_numbers:
                if score == 0:
                    score += 1
                else:
                    score *= 2
                    

        total += score

    return total
        



# I just left this here for the sake of remembering how naive I am at times
def part_2_fail_xD(input):
    cards = {}
    # Extracts the numbers in the format [("card number", "winning numbers", "your numbers")]
    regex = "Card *(\d+): +([\d ]*) \| ([\d ]*)"
    for line in input:
        numbers = re.findall(regex, line)
        card = int(numbers[0][0])
        winning_numbers = numbers[0][1].split(" ")
        your_numbers = numbers[0][2].split(" ")
        # Remove empty strings
        winning_numbers = list(filter(None, winning_numbers))
        your_numbers = list(filter(None, your_numbers))
        winning_numbers = list(map(int, winning_numbers))
        your_numbers = list(map(int, your_numbers))

        cards[card] = [card+1+i for i in range(len([1 for number in winning_numbers if number in your_numbers]))]

    cards_left = list(cards.keys())
    your_cards = []

    while len(cards_left) > 0:
        card = cards_left.pop(0)
        your_cards += cards[card]
        cards_left += cards[card]

    return len(your_cards) + len(cards.keys())




def part_2(input):
    cards = {}
    # Extracts the numbers in the format [("card number", "winning numbers", "your numbers")]
    regex = "Card *(\d+): +([\d ]*) \| ([\d ]*)"
    for line in input:
        numbers = re.findall(regex, line)
        card = int(numbers[0][0])
        winning_numbers = numbers[0][1].split(" ")
        your_numbers = numbers[0][2].split(" ")
        # Remove empty strings
        winning_numbers = list(filter(None, winning_numbers))
        your_numbers = list(filter(None, your_numbers))
        winning_numbers = list(map(int, winning_numbers))
        your_numbers = list(map(int, your_numbers))

        cards[card] = [card+1+i for i in range(len([1 for number in winning_numbers if number in your_numbers]))]



    def map_card(card):
        if isinstance(cards[card], int):
            return cards[card]
        elif len(cards[card]) == 0:
            return 0
        else:
            total = 0
            for card in cards[card]:
                total += map_card(card) + 1
            return total

    # Bottom up approach, makes it alot faster than the top down approach
    for card in sorted(list(cards.keys()), reverse=True):
        cards[card] = map_card(card)

    return sum(cards.values()) + len(cards.keys())



if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().splitlines()

    print("Part 1: ", part_1(input))
    print("Part 2: ", part_2(input))