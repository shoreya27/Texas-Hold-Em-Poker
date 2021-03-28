import unittest
from unittest.mock import MagicMock
from poker.player import Player
from poker.hand import Hand

class TestPlayer(unittest.TestCase):

    def test_player_has_a_name_and_hand(self):
        hand = Hand(cards = [])

        player = Player(name = "shoreya", hand = hand)
        self.assertEqual(player.name, "shoreya")
        self.assertEqual(player.hand, hand)

    def test_player_has_a_best_hand(self):
        hand_mock = MagicMock()
        player = Player(name = "shoreya", hand = hand_mock)

        player.best_hand()
        hand_mock.best_rank.assert_called()