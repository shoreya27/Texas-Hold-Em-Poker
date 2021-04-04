from poker.validators import StraightAndStraighFlushValidator
class StraightFlushValidator(StraightAndStraighFlushValidator):
    
    def __init__(self, cards):
        self.cards = cards
        self.name  = "Straight flush"

    
    def is_valid(self):
        if self.generate_straight_flush_list_of_cards:
            return True
        return False

    def valid_cards(self):
        return self.generate_straight_flush_list_of_cards[-1]


    @property
    def generate_straight_flush_list_of_cards(self):
        return [
            only_5card_list
            for only_5card_list in self._get_collection_of_straight_cards
            if len({card.suite for card in only_5card_list}) == 1
        ]
