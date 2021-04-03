from poker.validators import RankValidator

class FourOfAKindValidator(RankValidator):

    def __init__(self, cards):
        self.cards = cards
        self.name = "Four of a kind"
    def is_valid(self):
        rank_count_dict = self._filter_rank_count_dict(4)
        return len(rank_count_dict) == 1
    
    def valid_cards(self):
        rank_count_dict = self._filter_rank_count_dict(4)
        return [card for 
                card in self.cards
                if card.rank in rank_count_dict ]