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
        mock_card1 = MagicMock()
        mock_card1.rank = "Ace"
        mock_card1.suite = "diamonds"
        mock_card2 = MagicMock()
        mock_card2.rank = "8"
        mock_card2.suite = "clubs"
        mock_card3 = MagicMock()
        mock_card3.rank = "5"
        mock_card3.suite = "spades"
        mock_card4 = MagicMock()
        mock_card4.rank = "King"
        mock_card4.suite = "spades"
        cards1 = [mock_card1 , mock_card2]
        cards2 = [mock_card3, mock_card4]
        deck_mock = MagicMock()
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()

        players = [mock_player1,mock_player2]
        
        deck_mock.remove_cards.side_effect = [cards1, cards2, [], [], []]
        
        play_round = PlayGround(deck = deck_mock,player = players)
        play_round.play()
        deck_mock.remove_cards.assert_has_calls(
            [call(2), 
            call(2)
            ]
        )

        mock_player1.add_cards.assert_has_calls(
            [call(cards1)]
        )
        mock_player2.add_cards.assert_has_calls([call(cards2)])
    
    def test_remove_players_who_wants_to_fold(self):

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()

        players = [mock_player1, mock_player2]

        mock_player1.wants_to_fold.return_value = True

        mock_player2.wants_to_fold.return_value = False

        play_ground = PlayGround(deck = Deck(), player=players)
        play_ground.play()
        self.assertEqual(
            play_ground.players,
            [mock_player2]   
        )
    
    def test_community_card_3_flop_1_river_1_turn(self):

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()

        players = [mock_player1, mock_player2]

        mock_player1.wants_to_fold.return_value = False

        mock_player2.wants_to_fold.return_value = False
        mock_deck = MagicMock()
        flop_cards = MagicMock()
        river_card = MagicMock()
        turn_card = MagicMock()
        mock_deck.remove_cards.side_effect = [
            [],[],flop_cards,river_card,turn_card
        ]
        play_ground = PlayGround(deck = mock_deck, player=players)
        play_ground.play()


        mock_deck.remove_cards.assert_has_calls(
            [call(3), call(1), call(1)]
        )
        cards = [flop_cards, river_card, turn_card]
        for card in cards:
            mock_player1.add_cards.assert_has_calls(card)
            mock_player2.add_cards.assert_has_calls(card)