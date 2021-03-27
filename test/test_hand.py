from unittest import suite
from poker.hand import Hand 
from poker.card import Card
import unittest

class TestHand(unittest.TestCase):
    
    def test_hand_has_cards(self):
        cards = [
            Card(rank = "Ace", suite = "clubs"), 
            Card(rank = "7", suite = "spades")
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.cards, 
            cards
        )

    def test_hand_has_biggest_rank_card(self):
        cards = [
            Card(rank = "Ace", suite="clubs"),
            Card(rank = "7", suite = "spades")
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(), 
            "Highest card"
        )
    
    def test_hand_has_a_pair(self):
        cards = [
            Card(rank = "Ace", suite="clubs"),
            Card(rank = "Ace", suite = "spades")
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(), 
            "Pair"
        )
    
    def test_to_figure_hand_has_double_pair(self):
        '''
        Note to have a hand 2 pairs=4cards,
        so that can only happen after a Flop stage
        '''
        cards = [
            Card(rank = "Ace", suite = "hearts"),
            Card(rank = "Ace", suite = "clubs"),
            Card(rank = "5", suite = "spades"),
            Card(rank = "King", suite = "hearts"),
            Card(rank = "King", suite = "clubs")
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )
    
    def test_to_figure_hand_has_three_of_same_kind(self):
        '''
        Note: Always first write your code even
        if duplicacy is occurring .
        '''
        cards = [
            Card(rank = "Ace", suite = "hearts"),
            Card(rank = "Ace", suite = "clubs"),
            Card(rank = "5", suite = "spades"),
            Card(rank = "Ace", suite = "hearts"),
            Card(rank = "King", suite = "clubs")
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Three of kind"
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

        hand = Hand(cards)
        self.assertEqual(
            hand.cards,
        [
            Card(rank = "5", suite = "hearts"),
            Card(rank = "King", suite = "clubs"),
            Card(rank = "Ace", suite = "clubs")

        ]
        )
    
    def test_to_figure_hand_has_a_straight(self):

        cards = [
            Card(rank = "5", suite = "diamonds"),
            Card(rank = "6", suite = "hearts"),
            Card(rank = "7", suite = "clubs"),
            Card(rank = "8", suite = "spades"),
            Card(rank = "9", suite = "diamonds")
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )
    
    def test_2_cards_cant_be_straight(self):

        cards = [
            Card(rank = "5", suite = "diamonds"),
            Card(rank = "6", suite = "hearts"),
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Highest card"
        )