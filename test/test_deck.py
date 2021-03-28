from poker.deck import Deck
from poker.card import Card
import unittest
from unittest.mock import patch
import random

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
    
    @patch('random.shuffle')
    def test_deck_shuffles_the_cards(self, mock_shuffle):

        deck = Deck()

        cards = [
            Card(rank = "Ace", suite = "clubs"),
            Card(rank = "8", suite = "clubs")
        ]
        deck.add_cards(cards)
        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)