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
                         FlushValidator,
                         FullHouseValidator,
                         FourOfAKindValidator,
                         StraightFlushValidator)
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
            ("Straight flush", StraightFlushValidator(cards= self.cards).is_valid),
            (FourOfAKindValidator(cards = self.cards).name, FourOfAKindValidator(cards = self.cards).is_valid),
            (FullHouseValidator(cards = self.cards).name, FullHouseValidator(cards = self.cards).is_valid),
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
        is_straight_flush = StraightFlushValidator(cards=self.cards).is_valid()
        if not is_straight_flush:
            return False
        last_card = self.cards[-1].rank == "Ace"
        return is_straight_flush and last_card

    