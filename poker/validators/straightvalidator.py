from poker.validators import StraightAndStraighFlushValidator
class StraightValidator(StraightAndStraighFlushValidator):
    
    def __init__(self, cards):
        self.cards = cards
        self.name  = "Straight"
    
    def is_valid(self):
        if self._get_collection_of_straight_cards:
            return True
        return False

    def valid_cards(self):
        return self._get_collection_of_straight_cards[-1]
