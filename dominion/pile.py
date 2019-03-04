from enum import Enum

class PileType(Enum):
    VICTORY_CARDS = 1

class Pile():
    def __init__(self, pile_type, inital_cards):
        self.pile_type = pile_type
        self.cards = inital_cards

    def is_empty(self):
        return self.cards == 0