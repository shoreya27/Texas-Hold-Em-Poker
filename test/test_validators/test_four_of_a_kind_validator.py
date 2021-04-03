import unittest
from unittest import suite

from poker.card import Card
from poker.validators import FourOfAKindValidator


class TestFourOfAKindvalidator(unittest.TestCase):

    def setUp(self):
        two =                    Card(rank = "2", suite = "spades")
        self.four_hearts   =     Card(rank = "4", suite = "hearts")
        self.four_diamonds =     Card(rank = "4", suite = "diamonds")
        self.four_clubs    =    Card(rank = "4", suite = "clubs")
        self.four_spades   =    Card(rank = "4", suite = "spades")

        self.cards = [
            two,
            self.four_clubs,
            self.four_diamonds,
            self.four_hearts,
            self.four_spades
        ]
    
    def test_is_valid(self):

        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    
    def test_valid_cards(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
            self.four_clubs,
            self.four_diamonds,
            self.four_hearts,
            self.four_spades
            ]
        )
