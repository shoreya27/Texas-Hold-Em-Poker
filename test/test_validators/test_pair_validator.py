import unittest
from poker.validators import PairValidator
from poker.card import Card

class TestPairValidator(unittest.TestCase):

    def test_valid_rank_is_pair(self):
        cards = [
            Card(rank = "5", suite = "hearts"),
            Card(rank = "7", suite = "spades"),
            Card(rank = "9", suite = "clubs"),
            Card(rank = "9", suite = "diamonds"),
            Card(rank = "King", suite = "hearts")
        ]
        pair = PairValidator(cards = cards)

        self.assertEqual(
         pair.is_valid(),
         True   
        )
    
    def test_valid_cards_making_a_pair(self):
        
        nine_diamonds = Card(rank = "9", suite = "diamonds")
        nine_clubs    = Card(rank = "9", suite = "clubs")

        cards = [
            Card(rank = "5", suite = "hearts"),
            Card(rank = "7", suite = "spades"),
            nine_diamonds,
            nine_clubs,
            Card(rank = "King", suite = "hearts")
            ]
        cards.sort()
        pair = PairValidator(cards = cards)

        self.assertEqual(
            pair.valid_cards(),
            [nine_clubs,nine_diamonds]
        )
