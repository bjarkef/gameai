from player import Player

from dominion.base_cards import Province
from dominion.pile import Pile, PileType

class State():
    def __init__(self, players):
        if isinstance(players, int):
            players = [Player() for x in range(3)]
        self.num_players = len(players)
        self.current_turn = players[0]

        initial_victory_cards = 12
        if self.num_players == 2:
            initial_victory_cards = 8
        self.province_pile = Pile(PileType.VICTORY_CARDS, [Province() for i in range(initial_victory_cards)])
        self.victory_cards = [self.province_pile]

        self.all_supply_piles = [self.victory_cards]
    
    def is_finished(self):
        if self.province_pile.is_empty():
            return True
        # TODO: Check for more than 3 empty piles
        return False

    def whoes_turn(self):
        return self.current_turn