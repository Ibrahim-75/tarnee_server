# import numpy as np
from enumerations import PlayerState

class PlayerData:
    def __init__(self, player_name, sid, room_id):
        self.room_id = room_id
        self.player_state = PlayerState.waiting.value
        self.player_name = player_name
        self.sid = sid


class Score:
    __slots__ = ("request", "score", "sign")    # this will make objects use less memory and work faster

    def __init__(self, request):
        self.request = request
        self.score = 0
        self.sign = 1

    def set_score(self, score):
        self.score = score
        if self.score < self.request:
            self.sign = -1


class Player(object):
    __slots__ = ("player_name", "player_index", "player_id", "total_score", "cards", "scores")

    # using slot will not create the __dict__ attribute, so we have to define it explicitly
    # @property
    # def __dict__(self):
    #     return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}

    def __init__(self, player_name, player_index, player_id):
        self.player_name = player_name
        self.player_index = player_index
        self.player_id = player_id
        self.total_score = 0  # = sum (score * sign)
        self.cards = []
        # request_score is a list of dictionaries that stores requests and scores for each round. element 0 => first round
        self.scores = []  # (request, score, sign) sing = -1 => lost this round else wins

    def get_cards(self, player_cards):
        self.cards = player_cards

    def request(self, request):
        score = Score(request)
        self.scores.append(score)

    def register_score(self, round_no, score):
        self.scores[round_no - 1].set_score(score)
        self.total_score += self.scores[round_no - 1].score * self.scores[round_no - 1].sign

    def throw_card(self, card):
        self.cards.remove(card)

    def player_data(self):
        # data = vars(self) # can be used to convert object into dictionary, but not in case using __slots__
        data = {slot: getattr(self, slot) for slot in self.__slots__}
        return data

    # def set_score(self, score):

    def __str__(self):
        return f"Player {self.player_name} with index {self.player_index}"

if __name__ == '__main__':
    p = Player('id', 1, '123')
    print(p.player_data())