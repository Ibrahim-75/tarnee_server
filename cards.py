import random


class Card:
    def __init(self, card_type, card_no):
        self.card_type = card_type
        self.card_no = card_no


class CardSet:
    pass


class TarneebCardSet(CardSet):
    _card_set = [
        [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12),
         (1, 13), (1, 14)],
        [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12),
         (2, 13), (2, 14)],
        [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
         (3, 13), (3, 14)],
        [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12),
         (4, 13), (4, 14)]]
    card_set_size = len(_card_set) * len(_card_set[0])

    def __init__(self, min_shuffles, max_shuffles):
        self.card_set = [self._card_set[i][j] for i in range(len(self._card_set)) for j in
                         range(len(self._card_set[0]))]
        self.min_shuffles = min_shuffles
        self.max_shuffles = max_shuffles

    def shuffle_cards(self):
        nbr_of_shuffles = random.randint(self.min_shuffles, self.max_shuffles)
        for i in range(nbr_of_shuffles):
            while True:
                start_card = random.randint(1, self.card_set_size)
                end_card = random.randint(1, self.card_set_size)
                if end_card != start_card:
                    break
            if start_card > end_card:
                start_card, end_card = end_card, start_card
            card_slice = self.card_set[start_card:end_card]
            self.card_set[start_card:end_card] = []
            self.card_set.extend(card_slice)

    def distribute_cards(self):
        self.shuffle_cards()
        c1 = sorted(self.card_set[0:13], key=lambda e: e[0])
        c2 = sorted(self.card_set[13:26], key=lambda e: e[0])
        c3 = sorted(self.card_set[26:39], key=lambda e: e[0])
        c4 = sorted(self.card_set[39:52], key=lambda e: e[0])
        self.card_set.clear()
        return [c1, c2, c3, c4]
