'''
I cannot create 52 cards creation function
from Deck file bcoz to do so,
I would have to import Card class
and then I will have to loop through
each card suite and rank ,therefore this
is not a good practice when 1 type of object know
too much about other class.
'''
import random
class Deck():
    
    def __init__(self):
        self.cards = []
    
    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)
    
    
    def remove_cards(self, number):
        card_to_remove = self.cards[:number]
        del self.cards[:number]
        return card_to_remove
    

    def shuffle(self):
        random.shuffle(self.cards)