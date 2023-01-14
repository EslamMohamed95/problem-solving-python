CardsNo = int(input())
Cards = list(map(int, input().strip().split()))[:CardsNo]
Serej = 0
Dima = 0
turn = 1
card = 0
card_idx = 0
while len(Cards) > 0:
    if turn:
        card = Cards[0] if Cards[0] > Cards[-1] else Cards[-1]
        card_idx = Cards.index(card)
        Cards.pop(card_idx)
        Serej += card
        turn = 0
    else:
        card = Cards[0] if Cards[0] > Cards[-1] else Cards[-1]
        card_idx = Cards.index(card)
        Cards.pop(card_idx)
        Dima += card
        turn = 1

print(Serej, Dima)
