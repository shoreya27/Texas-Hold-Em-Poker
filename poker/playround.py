class PlayGround():

    def __init__(self, deck, player):
        self.deck = deck
        self.players = player
    
    def play(self):
        self.deck.shuffle()

        #now remove 2 cards for each player present
        #in game
        for player in self.players:
            self.deck.remove_cards(2)