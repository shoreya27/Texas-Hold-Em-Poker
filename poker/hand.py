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

    def get_highest_rank_card(self):
        return "biggest card"