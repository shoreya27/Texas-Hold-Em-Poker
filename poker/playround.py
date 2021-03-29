class PlayGround():

    def __init__(self, deck, player):
        self.deck = deck
        self.players = player
    
    def play(self):
        self._shuffle_deck()
        self._add_two_cards_to_each_player_from_deck()
    
    
    def _shuffle_deck(self):
        self.deck.shuffle()
    
    def _add_two_cards_to_each_player_from_deck(self):
        #now remove 2 cards for each player present
        #in game
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)