from Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        self.deck = []
        shapes = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        while len(self.deck) < 52:
            new_card = Card(randint(1, 13), shapes[randint(1, 4)])
            if new_card not in self.deck:
                self.deck.append(new_card)
            else:
                continue

    def show(self):
        print(f"{self.deck}")

    def shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop(randint(0, len(self.deck)-1))
