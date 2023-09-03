import flask_socketio
from flask import Flask, jsonify, request

from flask_socketio import SocketIO, join_room, leave_room, emit
import game, player
import uuid
import os
from enumerations import GameState
os.environ.setdefault('FLASK_ENV', 'development')

# Flask App Config
# app: Flask = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

# CORS_ALLOWED_ORIGINS is the list of origins authorized to make requests.
socketio = SocketIO(app, cors_allowed_origins='*')
# socketio = SocketIO(app)


# Home Page
@app.route('/', methods=['GET', 'POST'])
# @app.route('/')
def index():
    return jsonify({'data': "Web Socket Example"})


####Declarations#####################
# host = '192.168.65.1'
# host = '192.168.65.1'
host = '0.0.0.0'
port = 80
games = {}
connected_players = {}


@socketio.on('connect')
def on_connect():
    # player_id = msg['player_id']
    sid = request.sid
    # check if this player is not in connected players
    # if connected_players.get(player_id) is None:
    #     player_data = {
    #         'socket_id': sid,
    #         'room_id': '',
    #         'playing': False
    #     }
    # else:
        # if he is already joined, then get his data
        # player_data = connected_players[player_id]
        # update the socket id to new id
        # player_data['socket_id'] = sid
        # check if player was in a game
    #     if player_data['room_id']:
    #         # check if game is still going on
    #         # rejoin to game
    #         player_data['playing'] = True
    #         # put in place of AI player.....
    #
    # connected_players[player_id] = player_data
    # print(player_data)
    # emit('connect_success', player_data, room=sid)
    msg = sid + ' from AWS server'
    print(msg)
    emit('connect_success', msg, room=sid)




@socketio.on('create_game')
def create_game(msg):
    nick_name = msg['nick_name']
################# create a new game and give it a unique room id
    room_id = str(uuid.uuid4())
    print('Hi', nick_name)
#     new_game = game.TarneebGame(10, 20, room_id)
# ################# store the game in dictionary
#     games[room_id] = new_game
#     print('game_created', {'room_id': room_id})

    join_room(room_id)
    msg = {'room_id': room_id + ' on AWS'}

    emit('game_created', msg, room=room_id)
#
#     new_game.start_round()
#     p1 = player.Player(nick_name, 0, request.sid)
#     new_game.add_player(p1)
#
#     print(new_game.player_cards)
#     print(new_game.players)
#     player1_data = p1.player_data()
#     emit('distribute_cards', player1_data)
#     print('Player1:', player1_data)


# @socketio.on("disconnect")
# def disconnect(msg):
#     sid = msg['socket_id']
#     player_id = msg['player_id']
#     if not connected_players[player_id]['room_id']:
#         connected_players.pop(player_id)
#
#     print("Client disconnected")
#
#
# @socketio.on('join_game')
# def join(msg):
#     nick_name = msg['nick_name']
#     room_id = msg['roomId']
#     print(f"Player {nick_name} has joined the game")
# ##### check if the room_id exists in the dictionary, so the player can joine
#     my_game = games[room_id]
#     if my_game:
#         join_room(room_id)
#         p = player.Player(nick_name, 0, request.sid)
#         my_game.add_player(p)
#         player_data = p.player_data()
#         emit('player_joined', player_data, room=room_id)
#
#
# @socketio.on('play_card')
# def play_card(msg):
#     room_id = msg['room_id']
#     player_index = msg['player_index']
#     socket_id = msg['socket_id']
#
#
#
# @socketio.on('player_leave')
# def left(msg):
#     room = msg['roomId']
#     nick_name = msg['nick_name']
#     socket_id = msg['socketId']
#     my_game = games[socket_id]
#     my_player = next((p for p in my_game.players_indices if p.socket_id == socket_id), None)
#     leave_room(room=room)
#     #
#     # data = {
#     #     'nick_name': nick_name,
#     #
#     # }
#     # emit('player_left'', , room=room)


# if __name__ == '__main__':
# Run Flask-SocketIO App
socketio.run(app, port=port, host=host)
