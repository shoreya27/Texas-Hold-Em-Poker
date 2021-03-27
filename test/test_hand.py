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
    
    def test_to_figure_flush_is_best_rank(self):
        '''
        flush is when min 5 cards
        have same suite
        '''
        cards = [
            Card(rank = rank, suite = "hearts")
            for rank in ["3", "4", "5", "10", "7"]
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )
    
    def test_to_figure_fullhouse_is_best_rank(self):
        '''
        full house is when there is 3 card of same rank
        and 2 card of same rank
        1 "three of a kind" and 1 "pair"
        '''
        cards = [
            Card(rank = "4", suite = "hearts"),
            Card(rank = "4", suite = "diamonds"),
            Card(rank = "4", suite = "clubs"),
            Card(rank = "2", suite = "diamonds"),
            Card(rank = "2", suite = "spades"),
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Full house"
        )

    def test_to_figure_four_of_a_kind_is_best_rank(self):
        '''
        four of a kind occurs when there are
        4 cads of same rank
        '''
        cards = [
            Card(rank = "4", suite = "hearts"),
            Card(rank = "4", suite = "diamonds"),
            Card(rank = "4", suite = "clubs"),
            Card(rank = "4", suite = "spades"),
            Card(rank = "2", suite = "spades"),
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Four of a kind"
        )
    
    def test_to_straight_flush_is_best_rank(self):
        '''
        straight flush occurs when
        all rank are sequential and
        suite is same
        '''
        cards = [
            Card(rank = "4", suite = "hearts"),
            Card(rank = "5", suite = "hearts"),
            Card(rank = "6", suite = "hearts"),
            Card(rank = "7", suite = "hearts"),
            Card(rank = "8", suite = "hearts"),
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_rank(),
            "Straight flush"
        )