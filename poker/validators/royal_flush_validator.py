from poker.validators import StraightFlushValidator

class RoyalFlushValidator():
    
    def __init__(self, cards):
        self.cards = cards
        self.name  = "Royal flush"

    def is_valid(self):
        straight_flush = StraightFlushValidator(cards=self.cards)
        if straight_flush.is_valid():
            cards = straight_flush.valid_cards()
            if cards[-1].rank == "Ace":
                return True
        
        return False
    
    def valid_cards(self):
        return StraightFlushValidator(cards=self.cards).valid_cards()
