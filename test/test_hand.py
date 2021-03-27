from unittest import suite
from poker.hand import Hand 
from poker.card import Card
import unittest

class TestHand(unittest.TestCase):
    
    def test_hand_has_cards(self):
        cards = [
            Card(rank = "Ace", suite = "clubs"), 
            Card(rank = "7", suite = "spades")
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.cards, 
            cards
        )

    def test_hand_has_biggest_rank_card(self):
        cards = [
            Card(rank = "Ace", suite="clubs"),
            Card(rank = "7", suite = "spades")
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.get_highest_rank_card(), 
            "biggest card"
        )