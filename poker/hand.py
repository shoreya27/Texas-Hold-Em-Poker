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
                         StraightFlushValidator,
                         RoyalFlushValidator)
class Hand():
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardValidator
    )

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
    

    def best_rank(self):

        for index, validator_klass in enumerate(self.VALIDATORS):
            obj = validator_klass(cards = self.cards)
            if obj.is_valid():
                return index, obj.name, obj.valid_cards()
            