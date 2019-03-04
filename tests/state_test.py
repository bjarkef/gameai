import unittest

from dominion.state import State
from player import Player

class TestState(unittest.TestCase):
	def test_initial_state_is_not_finished(self):
		initial_state = State(2)
		self.assertFalse(initial_state.is_finished())

	def test_initial_whoes_turn(self):
		players = [Player() for x in range(3)]
		state = State(players)
		self.assertIs(players[0], state.whoes_turn())

if __name__ == "__main__":
	unittest.main()