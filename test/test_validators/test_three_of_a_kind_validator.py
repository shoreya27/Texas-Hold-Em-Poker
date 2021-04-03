import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class TestThreeOfAKindValidator(unittest.TestCase):

    def setUp(self):
        self.five          = Card(rank = "5", suite = "spades")
        self.king          = Card(rank = "King",suite = "clubs")
        self.ace_of_clubs  = Card(rank = "Ace", suite = "clubs")
        self.ace_of_hearts = Card(rank = "Ace", suite = "hearts")
        self.ace_of_spades = Card(rank = "Ace", suite = "spades")

        self.cards = [
            self.five,
            self.king,
            self.ace_of_clubs,
            self.ace_of_hearts,
            self.ace_of_spades
            ]
    
    def test_three_of_a_kind_is_valid(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_valid_cards(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
            self.ace_of_clubs,
            self.ace_of_hearts,
            self.ace_of_spades]
        )