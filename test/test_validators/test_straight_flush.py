import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class TestStraightFlushValidator(unittest.TestCase):

    def test_straigh_flush_is_not_valid(self):
        '''
        straight flush occurs when
        all rank are sequential and
        suite is same
        '''
        cards = [
            Card(rank = "3", suite = "clubs"),
            Card(rank = "4", suite = "hearts"),
            Card(rank = "5", suite = "hearts"),
            Card(rank = "6", suite = "hearts"),
            Card(rank = "7", suite = "hearts"),
            Card(rank = "8", suite = "clubs"),
            Card(rank = "King", suite = "hearts")
        ]
        validator = StraightFlushValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_straigh_flush_is_not_valid(self):
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
            Card(rank = "King", suite = "hearts")
        ]
        validator = StraightFlushValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_valid_cards(self):
        cards = [
            Card(rank = "4", suite = "hearts"),
            Card(rank = "5", suite = "hearts"),
            Card(rank = "6", suite = "hearts"),
            Card(rank = "7", suite = "hearts"),
            Card(rank = "8", suite = "hearts"),
            Card(rank = "King", suite = "hearts")
        ]
        validator = StraightFlushValidator(cards = cards)
        self.assertEqual(
            validator.valid_cards(),
            [
            Card(rank = "4", suite = "hearts"),
            Card(rank = "5", suite = "hearts"),
            Card(rank = "6", suite = "hearts"),
            Card(rank = "7", suite = "hearts"),
            Card(rank = "8", suite = "hearts"),                
            ]
        )