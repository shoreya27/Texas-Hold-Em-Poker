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
from .validators import (HighCardValidator,
                         NoCardValidator,
                         PairValidator,
                         TwoPairValidator,
                         ThreeOfAKindValidator ,
                         StraightValidator, 
                         FlushValidator)
class Hand():
    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards = [str(card) for card in self.cards]
        return ", ".join(cards)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy
    

    @property
    def _best_rank_validators(self):
        return (
            ("Royal flush", self._royalflush),
            ("Straight flush", self._straightflush),
            ("Four of a kind", self._four_of_a_kind),
            ("Full house", self._fullhouse),
            ("Flush", FlushValidator(cards = self.cards).is_valid ),
            ('Straight', StraightValidator(cards = self.cards).is_valid),
            (ThreeOfAKindValidator(cards=self.cards).name, ThreeOfAKindValidator(cards=self.cards).is_valid),
            (TwoPairValidator(cards=self.cards).name, TwoPairValidator(cards=self.cards).is_valid),
            ('Pair', PairValidator(cards=self.cards).is_valid),
            (HighCardValidator(cards=self.cards).name, HighCardValidator(cards=self.cards).is_valid),
            (NoCardValidator(cards = self.cards).name, NoCardValidator(cards = self.cards).is_valid)
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
        return FlushValidator(cards = self.cards).is_valid and StraightValidator(cards = self.cards).is_valid()
    
    def _four_of_a_kind(self):
        rank_count_dict = self._filter_rank_count_dict(4)
        return len(rank_count_dict) == 1

    def _fullhouse(self):
        return ThreeOfAKindValidator(cards=self.cards).is_valid() and PairValidator(cards=self.cards).is_valid() 
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