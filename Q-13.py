cards = [1, 5, 3, 4, 2, 3, 2]

def nextCard(cards):
    next = cards[0]
    newHand = cards[1:] + [cards[0]]
    return next, newHand

for i in range(len(cards)):
    card, cards = nextCard(cards)
    print("Card from the top of the deck: ", card)
