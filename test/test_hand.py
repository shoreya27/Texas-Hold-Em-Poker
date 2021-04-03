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
    
    
    def test_2_cards_cant_be_straight(self):

        cards = [
            Card(rank = "5", suite = "diamonds"),
            Card(rank = "6", suite = "hearts"),
        ]
        hand = Hand()
        hand.add_cards(cards)
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
        hand = Hand()
        hand.add_cards(cards)
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
        hand = Hand()
        hand.add_cards(cards)
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
        hand = Hand()
        hand.add_cards(cards)
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
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
            "Straight flush"
        )


    def test_to_royal_flush_is_best_rank(self):
        '''
        royal flush occurs when
        all rank are sequential and
        suite is same and the last card is Ace
        '''
        cards = [
            Card(rank = "10", suite = "hearts"),
            Card(rank = "Jack", suite = "hearts"),
            Card(rank = "Queen", suite = "hearts"),
            Card(rank = "King", suite = "hearts"),
            Card(rank = "Ace", suite = "hearts"),
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
            "Royal flush"
        )