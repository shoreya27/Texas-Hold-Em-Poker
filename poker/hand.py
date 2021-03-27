'''
Best Practice to create a small small piece
of code like classes which does specific task
Dont over burder single class object with diff
tasks
duplicacy is cheaper than wrong abstraction
'''

class Hand():
    def __init__(self, cards):
        self.cards = cards

    def best_rank(self):
        '''
        It can be Highest Rank,
        >flush
        >pair
        > pairs
        '''

        third_rank_of_same_kind = self._filter_rank_count_dict(3)

        pair_rank_count = self._filter_rank_count_dict(2)

        if len(third_rank_of_same_kind) == 1:
            return "Three same kind"

        if len(pair_rank_count) == 2:
            return "double pair"
        elif len(pair_rank_count) == 1:
            return "Pair"
        return "biggest card"

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