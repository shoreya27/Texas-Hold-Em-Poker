from unittest import suite
from poker.hand import Hand 
from poker.card import Card
import unittest

class TestHand(unittest.TestCase):

    def test_to_check_technical_representation_of_hand(self):
        hand = Hand()
        cards = [
            Card(rank = "7", suite = "spades"),
            Card(rank = "Ace", suite = "clubs")
        ]
        hand.add_cards(cards)
        self.assertEqual(
            repr(hand),
            "7 of spades, Ace of clubs"
        )

    def test_hand_has_no_cards_on_initiaisation(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])
    
    def test_hand_has_cards(self):
        cards = [
            Card(rank = "7", suite = "spades"),
            Card(rank = "Ace", suite = "clubs") 

        ]

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.cards, 
            cards
        )

    
    '''
    Before figuring the best rank to straight
    I want to sort the cards because straight rank
    is sequence order of rank eg 5 , 6 ,7 ,8 ,9
    '''
    def test_hand_cards_are_sorted(self):
        cards = [
            Card(rank = "5", suite = "hearts"),
            Card(rank = "Ace", suite = "clubs"),
            Card(rank = "King", suite = "clubs"),
        ]

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.cards,
        [
            Card(rank = "5", suite = "hearts"),
            Card(rank = "King", suite = "clubs"),
            Card(rank = "Ace", suite = "clubs")

        ]
        )