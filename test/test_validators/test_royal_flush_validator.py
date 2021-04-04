import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator


class TestRoyalFlushValidator(unittest.TestCase):

    def test_to_royal_flush_is_best_rank(self):
        '''
        royal flush occurs when
        all rank are sequential and
        suite is same and the last card is Ace
        '''
        cards = [
            Card(rank = "9", suite = "hearts"),
            Card(rank = "10", suite = "hearts"),
            Card(rank = "Jack", suite = "hearts"),
            Card(rank = "Queen", suite = "hearts"),
            Card(rank = "King", suite = "hearts"),
            Card(rank = "Ace", suite = "diamonds"),
        ]
        validator = RoyalFlushValidator(cards= cards)
        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_is_valid(self):
        '''
        royal flush occurs when
        all rank are sequential and
        suite is same and the last card is Ace
        '''
        cards = [
            Card(rank = "9", suite = "hearts"),
            Card(rank = "10", suite = "hearts"),
            Card(rank = "Jack", suite = "hearts"),
            Card(rank = "Queen", suite = "hearts"),
            Card(rank = "King", suite = "hearts"),
            Card(rank = "Ace", suite = "hearts"),
        ]
        validator = RoyalFlushValidator(cards= cards)
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_valid_cards(self):
        cards =  [
            Card(rank = "9", suite = "hearts"),
            Card(rank = "10", suite = "hearts"),
            Card(rank = "Jack", suite = "hearts"),
            Card(rank = "Queen", suite = "hearts"),
            Card(rank = "King", suite = "hearts"),
            Card(rank = "Ace", suite = "hearts"),
        ]
        validator = RoyalFlushValidator(cards= cards)
        self.assertEqual(
            validator.valid_cards(),
            [
            Card(rank = "10", suite = "hearts"),
            Card(rank = "Jack", suite = "hearts"),
            Card(rank = "Queen", suite = "hearts"),
            Card(rank = "King", suite = "hearts"),
            Card(rank = "Ace", suite = "hearts"),
            ]
        )