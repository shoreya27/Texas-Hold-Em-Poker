class PlayGround():

    def __init__(self, deck, player):
        self.deck = deck
        self.players = player
    
    def play(self):
        self.deck.shuffle()