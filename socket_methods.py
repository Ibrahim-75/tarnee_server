from flask import Flask, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
from player import PlayerData, PlayerState
import game, player
import uuid
from enumerations import *

games = {}
connected_players = {}


# Listeners
def connect(sid):
    response = {
        'socket_id': sid,
        'msg': 'connection successful to server ideeb'
    }
    emit('connect_success', response, room=sid)
    ###
    print('Player connected with session number:', sid)


def disconnect():
    print("Player disconnect")


def create_game_private(sid, req):
    player_id = req['player_id']
    player_name = req['player_name']
    room_id = str(uuid.uuid4())
    connected_players[player_id] = PlayerData(player_name, sid, room_id)
    my_game = game.TarneebGame(10, 20, room_id)
    my_game.start_game()
    my_game.start_round()

    join_room(room_id, sid=sid)
    p1 = player.Player(player_name=player_name, player_index=0, player_id=player_id)
    p1.get_cards(my_game.player_cards[0])
    my_game.add_player(p1)
    games[room_id] = my_game

    response = {
        'success': True,
        'room_id': room_id,
        'player_index': 0,
        'cards': p1.cards,
        'msg': 'Game created successfully'
    }
    emit('game_created', response, room=sid)


def join_game(sid, req):
    player_id = req['player_id']
    player_name = req['player_name']
    room_id = req['room_id']
    connected_players[player_id] = PlayerData(player_name, sid, room_id)
    if games.get(room_id) is not None:
        my_game = games.get(room_id)
        nbr_players = my_game.number_of_players()
        if nbr_players < 4:
            p = player.Player(player_name=player_name, player_index=nbr_players, player_id=player_id)
            p.get_cards(my_game.player_cards[nbr_players]) #use number of players as player index
            my_game.add_player(p)
            games[room_id] = my_game
            response = {
                'player_index': nbr_players,
                'cards': p.cards,
                'msg': 'You joined the game'
            }
            join_room(room=room_id, sid=sid)
            emit('joined_game_success', response, room=sid)
        else:
            response = {
                'success': False,
                'msg': 'Number of players is fulfilled'
            }
            emit('joined_game_failed', response, room=sid)
    else:
        response = {
            'success': False,
            'msg': 'game is not available'
        }
        emit('joined_game_failed', response, room=sid)


def leave_game(sid, req):
    room_id = req['room_id']
    player_id = req['player_id']
    player_index = req['player_index']
    leave_room(room=room_id, sid=sid)
    games[room_id].remove_player(player_index)
    connected_players[player_id].pop()

def create_game_public(req):
    pass





def play_game(req):
    pass
# connected_players['123'] = PlayerData()
# player_data = connected_players['123']
# del connected_players['123']
# print(connected_players)
