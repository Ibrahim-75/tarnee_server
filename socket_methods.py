from flask import Flask, jsonify, request
from flask_socketio import SocketIO, join_room, leave_room, emit
from player import PlayerData, PlayerState
import game, player
import uuid
from enumerations import *

games = {}
connected_players = {}


# Listeners
def connect():
    sid = request.sid
    response = {
        'socket_id': sid,
        'msg': 'connection successful to server'
    }
    emit('connect_success', response, room=sid)
    ###
    print('Player connected with session number:', sid)


def disconnect():
    print("Player disconnect")


def create_game_private(req):
    # sid = request.sid
    player_id = req['player_id']
    player_name = req['player_name']
    connected_players[player_id] = PlayerData(player_name)

    room_id = str(uuid.uuid4())
    games[room_id] = game.TarneebGame(10, 20, room_id)
    join_room(room_id, sid=player_id)
    p1 = player.Player(player_name=player_name, player_index=0, player_id=player_id)
    games[room_id].add_player(p1)


def add_player_to_game(room_id, player_id, player_name):
    if connected_players.get(player_id) is not None:
        connected_players[player_id] = PlayerData(player_name)
    if games.get(room_id) is not None:
        my_game = games.get(room_id)
        nbr_players = my_game.number_of_players
        if nbr_players < 4:
            p = player.Player(player_name=player_name, player_index=nbr_players, player_id=player_id)
            my_game.add_player(p)

        
def join_game(req):
    sid = request.sid
    player_id = req['player_id']
    player_name = req['player_name']
    connected_players[player_id] = PlayerData(player_name)

    room_id = req['room_id']
    if games.get(room_id) is not None:
        my_game = games.get(room_id)
        nbr_players = my_game.number_of_players
        if nbr_players < 4:
            p = player.Player(player_name=player_name, player_index=nbr_players, player_id=player_id)
            my_game.add_player(p)


def create_game_public(req):
    pass





def play_game(req):
    pass
# connected_players['123'] = PlayerData()
# player_data = connected_players['123']
# del connected_players['123']
# print(connected_players)
