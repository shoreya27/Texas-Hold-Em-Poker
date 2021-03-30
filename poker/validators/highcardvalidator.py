class HighCardValidator():
    
    def __init__(self,cards):
        self.cards = cards
        self.name = "Highest card"
    def is_valid(self):
        return len(self.cards) >= 2
    
    def highest_card(self):
        return self.cards[-1:]