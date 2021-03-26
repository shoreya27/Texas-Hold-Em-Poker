from poker.card import Card
from poker.deck import Deck
# card1 = Card(rank = "2", suite="clubs")
# card2 = Card(rank = "5", suite="spades")

cards = Card.create_52_cards()
deck = Deck()
deck.add_cards(cards)