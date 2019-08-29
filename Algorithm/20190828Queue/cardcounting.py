import sys
sys.stdin = open('card_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    C = input()
    cards = [C[i:i+3:] for i in range(0, len(C)-2, 3)]

    deck = []
    need = [13]*4
    for card in cards:
        if card not in deck:
            if card[0] == 'S':
                need[0] -= 1
            elif card[0] == 'D':
                need[1] -= 1
            elif card[0] == 'H':
                need[2] -= 1
            elif card[0] == 'C':
                need[3] -= 1
            deck.append(card)

    if len(deck) != len(cards):
        print('#{} {}'.format(tc, 'ERROR'))
    else:
        res = ' '.join(map(str, need))
        print('#{} {}'.format(tc,res))





