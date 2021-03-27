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
        # card_rank_count = dict()
        # for card in self.cards:
        #     '''
        #     setdefault(key, default value) sets the key
        #     to default value if that key is not
        #     present in dict
        #     '''
        #     card_rank_count.setdefault(card.rank, 0)
        #     card_rank_count[card.rank] += 1
        
        card_rank_count = {
            rank : rank_count
            for rank, rank_count in self.create_rankcount_dict.items()
            if rank_count == 2
        }

        if len(card_rank_count) == 2:
            return "double pair"
        elif len(card_rank_count) == 1:
            return "Pair"
        
        # for count in card_rank_count.values():
        #     '''
        #     flawed because if there are  pair
        #     then this will return Pair
        #     instead of returning double pair
        #     '''
        #     if count == 2:
        #         return "Pair"
        return "biggest card"

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