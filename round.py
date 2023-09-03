from enumerations import *


class Round:
    def __init__(self):
        self.__cards = []
        self.__ground_cards = []
        self.__players_indices = []    # to know the index of each player who throw a card
        self.tarneeb_type = 0            # to know the type of tarneeb (koba, dyner, ...)

    def drop_card(self, card, player_index):
        self.__ground_cards.append(card)
        self.__players_indices.append(player_index)

    def get_ground_cards(self):
        return self.__ground_cards.copy()

    def nbr_of_ground_cards(self):
        return len(self.__ground_cards)

    def reset_ground_cards(self):
        self.__cards.extend(self.__ground_cards)
        self.__ground_cards.clear()

    def get_all_cards(self):
        return self.__cards.copy()

    def reset_all_cards(self):
        self.__cards.clear()

    def set_tarneeb(self, tarneeb):
        self.tarneeb_type = tarneeb

    def get_winner_index(self):
        # first check if there are any tarneeb cards on current ground cards
        if any(card[0] == self.tarneeb_type for card in self.__ground_cards):
            dominant_type = self.tarneeb_type       # if any then the strongest type is tarneeb
        else:
            dominant_type = self.__ground_cards[0][0]   # if no tarneeb then the strongest type is the fist card
        print(dominant_type)
        dominant_cards = list(filter(lambda a: a[0] == dominant_type, self.__ground_cards)) # get all cards that are tarneeb
        highest_card = max(dominant_cards, key=lambda a: a[1])
        highest_index = self.__ground_cards.index(highest_card)
        return self.__players_indices[highest_index]


# ground = Ground()
# ground.current_cards= [(4, 5), (2, 6), (2, 10), (2, 11)]
# ground.players=[3, 4, 1, 2]
# ground.set_tarneeb(2)
# print(ground.players[ground.get_winner_index()])

