class TwoPairValidator():
    
    def __init__(self, cards):
        self.cards = cards
        self.name = "Two Pair"
    
    def is_valid(self):
        pair_rank_count = self._filter_rank_count_dict(2)
        return  len(pair_rank_count) == 2

    def valid_cards(self):
        pair_rank_count = self._filter_rank_count_dict(2)
        return [card 
                for card in self.cards 
                if card.rank in pair_rank_count
               ]
    

    def _filter_rank_count_dict(self, count):
        return {
    rank : rank_count
    for rank, rank_count in self.create_rankcount_dict.items()
    if rank_count == count
    }

    @property
    def create_rankcount_dict(self):
        card_rank_count = dict()
        for card in self.cards:
            '''
            setdefault(key, default value) sets the key
            to default value if that key is not
            present in dict
            '''
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1
        
        return card_rank_count