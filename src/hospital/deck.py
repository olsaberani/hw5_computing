import random

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            print("no cards left in the deck")
            return None
        card = self.cards.pop()
        print(f"{card.value} of {card.suit}")
        return card
