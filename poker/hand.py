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
        card_rank_count = dict()
        for card in self.cards:
            '''
            setdefault(key, default value) sets the key
            to default value if that key is not
            present in dict
            '''
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1
        
        for count in card_rank_count.values():
            '''
            flawed because if there are  pair
            then this will return Pair
            instead of returning double pair
            '''
            if count == 2:
                return "Pair"
        return "biggest card"