class PlayGround():

    def __init__(self, deck, player):
        self.deck = deck
        self.players = player
    
    def play(self):
        self._shuffle_deck()
        self._add_two_cards_to_each_player_from_deck()
        self._wager()
        self._flop_round_give_community_card()
        self._wager()
        self._river_round_give_community_card()
        self._wager()
        self._turn_round_give_community_card()
        self._wager()

    def _shuffle_deck(self):
        self.deck.shuffle()
    
    def _add_two_cards_to_each_player_from_deck(self):
        #now remove 2 cards for each player present
        #in game
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)
    
    def _wager(self):
        #check if plaer wants to fold
        #if wants to then remove from the list of
        #players
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)
    
    def _deal_with_community_cards(self, numbers):
        community_cards = self.deck.remove_cards(numbers)
        for player in self.players:
            player.add_cards(community_cards)

    def _flop_round_give_community_card(self):
        self._deal_with_community_cards(3)
    
    def _river_round_give_community_card(self):
        self._deal_with_community_cards(1)
    
    def _turn_round_give_community_card(self):
        self._deal_with_community_cards(1)