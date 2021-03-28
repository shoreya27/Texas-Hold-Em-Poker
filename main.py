from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand 
from poker.player import Player
# card1 = Card(rank = "2", suite="clubs")
# card2 = Card(rank = "5", suite="spades")

cards = Card.create_52_cards()
deck = Deck()
deck.add_cards(cards)

hand1 = Hand(cards = [])
hand2 = Hand(cards = [])

player1 = Player(name = "shoreya", hand = hand1)
player2 = Player(name = "Boris", hand = hand2)

#from main import hand1,hand2,player1,player2