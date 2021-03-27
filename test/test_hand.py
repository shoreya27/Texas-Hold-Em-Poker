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
            "biggest card"
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
            "double pair"
        )