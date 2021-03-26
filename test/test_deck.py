from poker.deck import Deck
from poker.card import Card
import unittest


class TestDeck(unittest.TestCase):

    def test_deck_cards(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )
    
    def test_add_cards_to_deck(self):
        card = Card(rank = "2", suite="clubs")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )