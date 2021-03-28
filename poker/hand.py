'''
Best Practice to create a small small piece
of code like classes which does specific task
Dont over burder single class object with diff
tasks
duplicacy is cheaper than wrong abstraction
we created individual small methods for checking 
best rank of hand , This keeps each
method to small purpose and is flexible
to add more
'''

class Hand():
    def __init__(self, cards):
        cards.sort()
        self.cards = cards

    @property
    def _best_rank_validators(self):
        return (
            ("Royal flush", self._royalflush),
            ("Straight flush", self._straightflush),
            ("Four of a kind", self._four_of_a_kind),
            ("Full house", self._fullhouse),
            ("Flush", self._flush),
            ('Straight', self._straight),
            ('Three of kind', self._three_of_kind),
            ('Two Pair', self._two_pair),
            ('Pair', self._pair),
            ('Highest card', self._highest_card),
            ('No cards', self._no_card)
        )

    def best_rank(self):
        '''
        It can be Highest Rank,
        >flush
        >pair
        > pairs
        '''
        for rank in self._best_rank_validators:
            name, validator = rank
            if validator():
                return name
    
    def _royalflush(self):
        is_straight_flush = self._straightflush()
        if not is_straight_flush:
            return False
        last_card = self.cards[-1].rank == "Ace"
        return is_straight_flush and last_card

    def _straightflush(self):
        return self._flush() and self._straight()
    
    def _four_of_a_kind(self):
        rank_count_dict = self._filter_rank_count_dict(4)
        return len(rank_count_dict) == 1

    def _fullhouse(self):
        return self._three_of_kind() and self._pair()   
    
    def _flush(self):
        suite_count_dict = self.create_suite_count_dict
        suit_count_dict = {
            suite:count
            for suite, count in suite_count_dict.items()
            if count >= 5
        }
        return len(suit_count_dict) == 1

    def _straight(self):
        if len(self.cards) < 5:
            return False
        rank_indexes = [card.rank_index for card in self.cards]
        starting_end = rank_indexes[0]
        ending       = rank_indexes[-1] + 1
        rank_indexes_range = list(
                            range(starting_end,ending)
                                )
        return rank_indexes == rank_indexes_range

    def _three_of_kind(self):
        third_rank_of_same_kind = self._filter_rank_count_dict(3)
        return len(third_rank_of_same_kind) == 1
    
    def _two_pair(self):
        pair_rank_count = self._filter_rank_count_dict(2)
        return  len(pair_rank_count) == 2
    
    def _pair(self):
        pair_rank_count = self._filter_rank_count_dict(2)
        return  len(pair_rank_count) == 1

    def _highest_card(self):
        return not self._no_card()
    
    def _no_card(self):
        return len(self.cards) == 0

    def _filter_rank_count_dict(self, count):
        return {
            rank : rank_count
            for rank, rank_count in self.create_rankcount_dict.items()
            if rank_count == count
        }

    @property
    def create_suite_count_dict(self):
        card_suite_count = dict()
        for card in self.cards:
            '''
            setdefault(key, default value) sets the key
            to default value if that key is not
            present in dict
            '''
            card_suite_count.setdefault(card.suite, 0)
            card_suite_count[card.suite] += 1
        
        return card_suite_count        

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