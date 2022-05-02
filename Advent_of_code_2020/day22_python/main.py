

def calculate_winner(deck):
    return sum([deck[-i] * i for i in range(1, len(deck) + 1)])



def part1(p1,p2):

    while p1 and p2:
        if p1[0] > p2[0]:
            p1.append(p1.pop(0))
            p1.append(p2.pop(0))
        elif p1[0] < p2[0]:
            p2.append(p2.pop(0))
            p2.append(p1.pop(0))

    if p1:
        return calculate_winner(p1)
    else:
        return calculate_winner(p2)



def part2(p1,p2, depth=0):
    p1_hands = set()
    p2_hands = set()

    while p1 and p2:
        if tuple(p1) in p1_hands or tuple(p2) in p2_hands:
            if depth == 0:
                return calculate_winner(p1)
            else:
                return True
        else:
            p1_hands.add(tuple(p1))
            p2_hands.add(tuple(p2))

        player1_card = p1.pop(0)
        player2_card = p2.pop(0)

        if player1_card <= len(p1) and player2_card <= len(p2):
            player1_is_winner = part2([p1[i] for i in range(player1_card)], [p2[i] for i in range(player2_card)],depth+1)
            if player1_is_winner:
                p1.append(player1_card)
                p1.append(player2_card)
            else:
                p2.append(player2_card)
                p2.append(player1_card)
        else:
            if player1_card > player2_card:
                p1.append(player1_card)
                p1.append(player2_card)
            elif player1_card < player2_card:
                p2.append(player2_card)
                p2.append(player1_card)
            else:
                print("This was not supposed to happen i think")

    if p1 and depth > 0:
        return True
    elif p2 and depth > 0:
        return False
    elif p1 and depth == 0:
        return calculate_winner(p1)
    else:
        return calculate_winner(p2)


if __name__ == '__main__':
    with open("data.txt", "r") as f:
        data = f.read()

    data = data.replace("Player 1:", "")
    data = data.split("Player 2:")

    data[0] = data[0].split("\n")
    data[1] = data[1].split("\n")

    data[0].pop()
    data[0].pop()
    data[0].pop(0)
    data[1].pop(0)

    player1 = [int(i) for i in data[0]]
    player2 = [int(i) for i in data[1]]



    print("Part 1:",part1(player1.copy(),player2.copy()))
    print("Part 2:",part2(player1,player2))
