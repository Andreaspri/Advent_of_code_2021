

strength_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


class Hand:
    def __init__(self, hand: str, j: bool=False) -> None:
        self.sorted_hand = list(sorted(list(hand.split(" ")[0]), key=lambda x: strength_map[x], reverse=True))
        self.original_hand = list(hand.split(" ")[0])
        self.bid = int(hand.split(" ")[1])
        self.strength = []
        self.j = j

        self.set_strength()



    def set_strength(self) -> None:

        # Count the cards
        hand = {}
        for card in self.sorted_hand:
            hand[card] = hand.get(card,0) + 1

        if self.j:
            js = hand.pop("J",0)

            if js != 5:
                hand[max(hand.items(), key= lambda x: x[1])[0]] += js
            else:
                hand["J"] = 5


        # Five of a kind
        if max(hand.values()) == 5:
            self.strength.append(27)
        # Four of a kind
        elif max(hand.values()) == 4:
            self.strength.append(26)
        # Full house
        elif max(hand.values()) == 3 and 2 in hand.values():
            self.strength.append(25)
        # Three of a kind
        elif max(hand.values()) == 3:
            self.strength.append(24)
        # Two pair
        elif list(hand.values()).count(2) == 2:
            self.strength.append(23)
        # One pair
        elif list(hand.values()).count(2) == 1:
            self.strength.append(22)
        # High card
        else:
            self.strength.append(21)

        for card in self.original_hand:
            if self.j:
                self.strength.append(strength_map[card] if card != "J" else 1)
            else:
                self.strength.append(strength_map[card])


    def __gt__(self, other) -> bool:
        for s, o in zip(self.strength, other.strength):
            if s > o: return True
            elif o > s: return False
        
        return False
    


def day_7(hands: list[Hand]) -> int:
    
    hands = sorted(hands)

    winnings = 0

    for rank, hand in enumerate(hands):
        winnings += (rank+1)*hand.bid

    return winnings



if __name__=='__main__':
    with open("input.txt") as f:
        data = f.readlines()
    hands = [Hand(i) for i in data]
    hands_2 = [Hand(i, True) for i in data]
    

    print("Part 1:", day_7(hands))
    print("Part 2:", day_7(hands_2))

