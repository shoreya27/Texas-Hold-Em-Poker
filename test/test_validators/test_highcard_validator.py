import unittest
from unittest import suite
from poker.validators import HighCardValidator
from poker.card import Card

class TestHighCardValidator(unittest.TestCase):

    def test_best_rank_is_high_card(self):
        cards = [
            Card(rank = "Ace", suite="clubs"),
            Card(rank = "7", suite = "spades")
        ]

        high_card = HighCardValidator(cards = cards)

        self.assertEqual(
            high_card.is_valid(), 
            True
        )
    
    def test_cards_which_is_the_highest_card(self):
        ace_of_diamond = Card(rank = "Ace", suite = "diamonds")
        cards = [
            Card(rank = "2", suite = "diamonds"),
            Card(rank = "7", suite = "hearts"),
            ace_of_diamond
        ]

        high_card = HighCardValidator(cards = cards)
        self.assertEqual(
            high_card.valid_cards(),
            [ace_of_diamond]
        )