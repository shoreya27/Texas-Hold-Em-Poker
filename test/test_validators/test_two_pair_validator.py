import unittest
from poker.validators import TwoPairValidator
from poker.card import Card

class TestTwOPairdValidator(unittest.TestCase):

    def setUp(self):
        self.five_diamond = Card(rank = "5", suite = "diamonds")
        self.king_hearts  = Card(rank = "King", suite = "hearts")
        self.king_clubs  = Card(rank = "King", suite = "clubs")
        self.ace_clubs   = Card(rank = "Ace", suite = "clubs")
        self.ace_hearts   = Card(rank = "Ace", suite = "hearts")

        self.cards = [
            self.five_diamond,
            self.king_hearts,
            self.king_clubs,
            self.ace_clubs,
            self.ace_hearts
        ]
        self.cards.sort()

    def test_two_pair_is_valid(self):

        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
         validator.is_valid(),
         True   
        )
    
    def test_two_pair_of_valid_card(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
         validator.valid_cards(),
         [self.king_clubs,self.king_hearts,
         self.ace_clubs,self.ace_hearts]
        )