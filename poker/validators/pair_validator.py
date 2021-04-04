from .rankvalidator import RankValidator
class PairValidator(RankValidator):
    
    def __init__(self, cards):
        self.cards = cards
        self.name  = "Pair"
    
    def is_valid(self):
        pair_rank_count = self._filter_rank_count_dict(2)
        return  len(pair_rank_count) == 1
    
    def valid_cards(self):
        pair_rank_count = self._filter_rank_count_dict(2)
        return [card 
                for card in self.cards 
                if card.rank in pair_rank_count
               ]
