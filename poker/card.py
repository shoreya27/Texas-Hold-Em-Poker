'''
This is the module which will have main class Card.
I have to insert __eq__() because the object which I am asserting in
test class is not the same.
'''

class Card():
    SUITES = ("clubs","diamonds","spades","hearts")
    RANKS = ("2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace")
    
    def __init__(self, rank, suite):
        if rank not in self.RANKS:
            raise ValueError(f"sorry, invalid rank given . Please see the available rank:{self.RANKS}")
        if suite not in self.SUITES:
            raise ValueError(f"sorry invalid suite name provided.")
        self.rank = rank
        self.suite = suite
        self.rank_index = self.RANKS.index(rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suite}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suite}')"
    
    @classmethod
    def create_52_cards(cls):
        return [
            Card(rank = rank, suite = suite)
            for suite in cls.SUITES
            for rank in cls.RANKS
        ]
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suite == other.suite
    
    def __lt__(self, other):
        return self.rank_index < other.rank_index