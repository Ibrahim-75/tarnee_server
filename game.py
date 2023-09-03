import random
from cards import TarneebCardSet
from round import Round
from player import Player
from enumerations import GameState


class CardGame:
    def __init__(self, min_shuffles, max_shuffles, room_id):
        self.min_shuffles = min_shuffles
        self.max_shuffles = max_shuffles
        self.room_id = room_id
        self.round = 0
        self.nbr_of_human_players = 0
        self.state = GameState.idle.value

    def start_game(self):
        self.state = GameState.started.value

    def terminate_game(self):
        self.state = GameState.terminated.value

    def wait_game(self):
        self.state = GameState.waiting.value

    def end_game(self):
        self.state = GameState.ended.value


class TarneebGame(CardGame):
    def __init__(self, min_shuffles, max_shuffles, room_id):
        super().__init__(min_shuffles, max_shuffles, room_id)
        self.__cards = TarneebCardSet(min_shuffles, max_shuffles)
        self.__round = Round()
        self.players = []
        self.player_cards = []

    def start_round(self):
        self.player_cards = self.__cards.distribute_cards()
        self.round += 1

    def end_round(self):
        self.__cards = self.__round.get_all_cards()
        self.__round.reset_all_cards()

    def add_player(self, player):
        # player.card_set = self.player_cards[self.nbr_of_human_players - 1]
        player.player_index = self.nbr_of_human_players
        self.nbr_of_human_players += 1
        self.players.append(player)

    def remove_player(self, player):
        self.nbr_of_human_players -= 1

    # ???????????????

    def player_play(self, player_index, card):
        self.players[player_index].throw_card(card)
        self.__round.drop_card(card, player_index)
        if self.__round.nbr_of_ground_cards() == 4:
            self.__round.reset_ground_cards()

    def player_request(self, player_index, request):
        self.players[player_index].request(self.round, request)

    def choose_partner(self, player_index):
        # the player with index 0 will always choose his partner
        # his partner must be put at index 2
        # 0 partner with 2, and 1 partner with 3
        self.players[player_index].player_index = 2     # set index of chosen partner to 2
        self.players[2].player_index = player_index     # set index of player 2 to that of chosen partner
        self.players[player_index], self.players[2] = self.players[2], self.players[player_index]   # swap the players in the players list

    def number_of_players(self):
        return len(self.players)