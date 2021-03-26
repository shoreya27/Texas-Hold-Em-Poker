from logging import setLoggerClass
import unittest
from poker.card import Card

class TestCardClass(unittest.TestCase):

    def test_check_rank(self):
        card = Card(rank = "Queen", suite = "clubs")
        self.assertEqual(card.rank, "Queen")
    
    def test_check_suite(self):
        card = Card(rank = "2", suite = "spades")
        self.assertEqual(card.suite, "spades")
    

    def test_string_representation_of_card(self):
        card = Card(rank = "2", suite= "clubs")
        self.assertEqual(str(card), "2 of clubs")
    
    def test_technical_representation(self):
        card = Card(rank = "Ace", suite= "clubs")
        self.assertEqual(repr(card), "Card('Ace', 'clubs')")
    
    def test_card_has_4_suits(self):
        self.assertEqual(
            Card.SUITES,
            ("clubs","diamonds","spades","hearts")
        )
    
    def test_card_has_13_ranks(self):
        self.assertEqual(
            Card.RANKS,
            ("2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace")
            )
    
    def test_card_has_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank= "two", suite="Jack")
    
    def test_card_has_valid_suite(self):
        with self.assertRaises(ValueError):
            Card(rank= "2", suite="jack")
    
    def test_standard_52_card_creation_class_method(self):
        #I cant check all 52 card objects
        #but I can test for inital card
        #and last card object which will assert me
        #that 52 cards has been created
        self.assertEqual(
            Card.create_52_cards()[0],
            Card(rank = "2", suite= "clubs")
        )

        self.assertEqual(
            Card.create_52_cards()[-1],
            Card(rank = "Ace", suite= "hearts")
        )