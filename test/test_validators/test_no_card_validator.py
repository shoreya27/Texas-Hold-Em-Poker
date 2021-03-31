import unittest
from poker.validators import NoCardValidator

class TestNoCardValidator(unittest.TestCase):

    def test_best_rank_has_no_cards(self):
        
        no_card = NoCardValidator(cards = [])
        
        self.assertEqual(
            no_card.is_valid(),
            True
        )

    def test_valid_cards(self):
        no_card = NoCardValidator(cards = [])
        
        self.assertEqual(
            no_card.valid_cards(),
            []
        )