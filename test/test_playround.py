import unittest
from poker.deck import Deck
from poker.player import Player
from unittest.mock import MagicMock, call
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
    
    def test_to_check_initial_2_cards_removed_for_each_player(self):
        '''
        I have 3 players , each player will get 2 cards
        total 3 times remove_card() of deck should
        be called
        special method in mock object to check
        the total calls happened for this funct
        each call(arg) represent 1 call to that
        remove_card function 
        '''
        deck_mock = MagicMock()
        players = [
            MagicMock(), 
            MagicMock(),
            MagicMock()
        ]
        
        play_round = PlayGround(deck = deck_mock,player = players)
        play_round.play()
        deck_mock.remove_cards.assert_has_calls(
            [call(2), 
            call(2),
            call(2)]
        )