import unittest
from unittest import suite

from poker.card import Card
from poker.validators import FullHouseValidator

class TestFullHouseValidator(unittest.TestCase):

    def setUp(self):
        self.four_of_hearts  =    Card(rank = "4", suite = "hearts")
        self.four_of_diamonds=    Card(rank = "4", suite = "diamonds")
        self.four_of_clubs   =    Card(rank = "4", suite = "clubs")
        five_of_clubs   =    Card(rank = "5", suite = "clubs")
        self.two_of_diamonds =    Card(rank = "2", suite = "diamonds")
        self.two_of_spades   =    Card(rank = "2", suite = "spades")
        
        self.cards = [
            self.two_of_diamonds,
            self.two_of_spades,
            self.four_of_clubs,
            self.four_of_diamonds,
            self.four_of_hearts,
            five_of_clubs
        ]
    def test_is_valid(self):
        '''
        full house is when there is 3 card of same rank
        and 2 card of same rank
        1 "three of a kind" and 1 "pair"
        '''
        validator = FullHouseValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_valid_cards(self):
        validator = FullHouseValidator(cards = self.cards)
    
        self.assertEqual(
            validator.valid_cards(),
            [
            self.two_of_diamonds,
            self.two_of_spades,
            self.four_of_clubs,
            self.four_of_diamonds,
            self.four_of_hearts,   
            ]
        )