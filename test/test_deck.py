from poker.deck import Deck
from poker.card import Card
import unittest
from unittest.mock import patch
import random

class TestDeck(unittest.TestCase):

    def test_length_of_deck(self):
        deck = Deck()
        self.assertEqual(
            len(deck),
            0
        )

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
    
    
    def test_to_remove_number_of_cards_from_deck(self):

        deck  = Deck()
        ace   = Card(rank = "Ace", suite = "spades")
        eight = Card(rank = "8", suite = "diamonds")

        cards = [ace, eight]

        deck.add_cards(cards)

        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )

        self.assertEqual(
            deck.cards,
            [eight]
        )