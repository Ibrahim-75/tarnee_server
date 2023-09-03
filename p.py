# 1: koba, 2: deenary, 3: bastawny, 4: sbaity
# cards = [[(t, c) for c in range(1, 14)] for t in range(1, 5)]
# print(cards)
import random
from datetime import datetime

def shuffle_cards(cards_set):
    cards_set = [cards_set[i][j] for i in range(len(cards_set)) for j in range(len(cards_set[0]))]
    random.shuffle(cards_set)
    return cards_set


start_time = datetime.now()
# cards = [[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13)], [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13)], [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13)], [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13)]]
cardsInRound = shuffle_cards(cards)
print(cardsInRound)
random.shuffle(cardsInRound)
# print(cardsInRound)

####### Distribute cards on 4 players
player1_cards = [cardsInRound[i] for i in range(0, 52, 4)]
player2_cards = [cardsInRound[i] for i in range(1, 52, 4)]
player3_cards = [cardsInRound[i] for i in range(2, 52, 4)]
player4_cards = [cardsInRound[i] for i in range(3, 52, 4)]
end_time = datetime.now()
elapsed_time = end_time - start_time

print("Player1 cards:\n", player1_cards)
print("Player2 cards:\n", player2_cards)
print("Player3 cards:\n", player3_cards)
print("Player4 cards:\n", player4_cards)

print(elapsed_time.microseconds)
######### play round
playedCards = [[player1_cards[i], player2_cards[i], player3_cards[i], player4_cards[i]] for i in range(13)]
print(playedCards)

random.sample()