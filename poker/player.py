class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def best_hand(self):
        return self.hand.best_rank()
    
    def add_cards(self, cards):
        self.hand.add_cards(cards)
    
    def wants_to_fold(self):
        return False
    
    def __gt__(self, other):
        current_player_best_rank_position = self.best_hand()[0]
        other_player_best_rank_position = other.best_hand()[0]

        if current_player_best_rank_position < other_player_best_rank_position:
            return True
        return False