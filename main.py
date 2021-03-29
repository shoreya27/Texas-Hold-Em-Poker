from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand 
from poker.player import Player
from poker.playround import PlayGround


cards = Card.create_52_cards()
deck = Deck()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "shoreya", hand = hand1)
player2 = Player(name = "Boris", hand = hand2)

play_ground = PlayGround(deck = deck, player= [player1, player2])

play_ground.play()
#from main import deck, hand1,hand2,player1,player2, play_ground