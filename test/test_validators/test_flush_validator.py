import unittest
from poker.card import Card

from poker.validators import FlushValidator

class TestFlushValidator(unittest.TestCase):
    
    def setUp(self):
        
        self.three_of_hearts = Card(rank = "3", suite = "hearts")
        self.four_of_hearts  = Card(rank = "4", suite = "hearts")
        self.five_of_hearts  = Card(rank = "5", suite = "hearts")

        self.ten_of_hearts   = Card(rank = "10", suite = "hearts")
        self.ace_of_hearts   = Card(rank = "Ace", suite = "hearts")

        self.cards = [
            self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            Card(rank = "7", suite = "clubs"),
            self.ten_of_hearts,
            self.ace_of_hearts
        ]
    
    def test_to_figure_flush_is_best_rank(self):
        '''
        flush is when min 5 cards
        have same suite
        '''
        validator = FlushValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_valid_cards(self):
        validator = FlushValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
            self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.ten_of_hearts,
            self.ace_of_hearts
            ]
        )