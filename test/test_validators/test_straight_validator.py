import unittest
from unittest import suite

from poker.card import Card
from poker.validators import StraightValidator

class TestStraight(unittest.TestCase):
    def setUp(self):
        two  = Card(rank = "2", suite = "clubs")
        self.five = Card(rank = "5", suite = "diamonds")
        self.six  = Card(rank = "6", suite = "hearts")
        self.seven= Card(rank = "7", suite = "clubs")
        self.eight= Card(rank = "8", suite = "spades")
        self.nine = Card(rank = "9", suite = "spades")
        self.ten  = Card(rank = "10", suite = "spades")
        
        self.cards = [
            two,
            self.five,
            self.six,
            self.seven,
            self.eight,
            self.nine,
            self.ten
        ]    

    def test_to_figure_hand_has_a_straight(self):
        validator = StraightValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_2_cards_cant_be_straight(self):
        cards = [
            Card(rank = "5", suite = "diamonds"),
            Card(rank = "6", suite = "hearts"),
        ]
        validator = StraightValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            False
        )
    
    
    def test_valid_cards(self):
        validator = StraightValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
            self.six,
            self.seven,
            self.eight,
            self.nine,
            self.ten 
            ]
        )
    