from .rankvalidator import RankValidator
class ThreeOfAKindValidator(RankValidator):
    
    def __init__(self, cards):
        self.cards = cards
        self.name = "Three of kind"
    
    def is_valid(self):
        third_rank_of_same_kind = self._filter_rank_count_dict(3)
        return len(third_rank_of_same_kind) == 1
    
    def valid_cards(self):
        third_rank_of_same_kind = self._filter_rank_count_dict(3)
        return [card 
                for card in self.cards 
                if card.rank in third_rank_of_same_kind
                 ]