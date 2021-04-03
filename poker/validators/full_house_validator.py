from poker.validators import ThreeOfAKindValidator, PairValidator
class FullHouseValidator():
    
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full house"
    
    def is_valid(self):
        return ThreeOfAKindValidator(cards=self.cards).is_valid() and PairValidator(cards=self.cards).is_valid() 
    

    def valid_cards(self):
        all_cards = (ThreeOfAKindValidator(cards=self.cards).valid_cards() 
        + PairValidator(cards=self.cards).valid_cards())
        all_cards.sort()
        return all_cards