import unittest
from poker.deck import Deck
from poker.player import Player
from unittest.mock import MagicMock
from poker.playround import PlayGround

class TestPlayround(unittest.TestCase):

    def test_play_round_has_a_deck_and_players(self):
        '''
        I am using a mock objects bcause if I create a player
        object then I have to create a hand object too and
        also card object for deck class
        Which goes too deep for simple test
        '''
        deck_mock = MagicMock()
        players = [
            MagicMock(), 
            MagicMock()
        ]
        
        play_round = PlayGround(deck = deck_mock,player = players)
        
        self.assertEqual(
            play_round.players,
            players
        )
        self.assertEqual(
            play_round.deck, 
            deck_mock
        )
    
    def test_play_ground_has_a_shuffle_method(self):  
        deck_mock = MagicMock()
        players = [
            MagicMock(), 
            MagicMock()
        ]
        
        play_round = PlayGround(deck = deck_mock,player = players)

        play_round.play()
        deck_mock.shuffle.assert_called_once()