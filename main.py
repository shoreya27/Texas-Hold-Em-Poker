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
hand3 = Hand()

player1 = Player(name = "shoreya", hand = hand1)
player2 = Player(name = "Boris", hand = hand2)
player3 = Player(name = "Tom", hand = hand3 )

play_ground = PlayGround(deck = deck, player= [player1, player2, player3])

play_ground.play()

players = [player1, player2, player3]
for player in players:
    print(f"{player.name} has received following cards {player.hand}")

    index, best_rank, best_cards = player.best_hand()
    winning_cards = [str(card) for card in best_cards]
    winn_cards    = ' and '.join(winning_cards)
    print(f"{player.name} has a rank:{best_rank} due to such cards:{winn_cards}")


winning_player = max(players)
print(f"winner is: {winning_player.name}..........")