
import flask_socketio
from flask import Flask, jsonify, request

from flask_socketio import SocketIO, join_room, leave_room, emit

import game, player
import uuid
import os

os.environ.setdefault('FLASK_ENV', 'development')

# Flask App Config
# app: Flask = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

# CORS_ALLOWED_ORIGINS is the list of origins authorized to make requests.
# socketio = SocketIO(app, cors_allowed_origins='*')
socketio = SocketIO(app)



# Home Page
@app.route('/', methods=['GET', 'POST'])
# @app.route('/')
def index():
    return jsonify({'data': "Web Socket Example"})


# p1 = player.Player()
# p2 = player.Player()
# p3 = player.Player()
# p4 = player.Player()
# game = game.TarneebGame(5, 10)

@socketio.on('connect')
def on_connect():
    print(request.sid)
    print('client Connected')
    emit('connect_success', 'Hi you are connected', broadcast=True)


@socketio.on('create_game')
def create_game(user_name):
    # global game
    new_game = game.TarneebGame(5, 10)
    print(request.sid)
    print(user_name)
    room_id = str(uuid.uuid4())
    print('game_created', {'room_id': room_id})
    join_room(room_id)
    emit('game_created', {'room_id': room_id}, room= room_id)
    new_game.roomId = room_id
    new_game.start_round()
    p1 = player.Player(user_name['nickName'], 0, request.sid)
    p1.cards = new_game.player_cards[0]
    new_game.players.append(p1)
    print(new_game.player_cards)
    print(new_game.players)
    # game.joinedPlayers += 1
    # emit('distribute_cards', {'nickName': user_name['nickName'],'turnIndex': 1, 'socketId': request.sid, 'points': 0, 'cards':p1.cards, 'playerType': 'L'})
    player1_data = p1.player_data()
    emit('distribute_cards', {'playerData': player1_data})
    print('Player1:', player1_data)


@socketio.on("disconnect")
def disconnect():
    print("Client disconnected")


@socketio.on('join')
def join(message):
    # we need roomId and Username for joining the room
    print(message)
    print('user joined')


    # username = message['username']
    # join room
    # join_room(room)
    # print(room)
    # Emit message or notifier to other user of same room
    # emit('message', {"msg": {str(username) + 'has joined the room.'}}, room=room)


@socketio.on('playCard')
def text(message):
    nickName = message['nickName']
    socketId = message['socketId']
    cardNo = message['cardNo']
    # msg = message['msg']
    # print(message)
    # emit('message', {"msg": {str(username) + ' : ' + str(msg)}}, room=room)
    print(f'player: {nickName} on socket: {socketId}, played card no: {cardNo}')


@socketio.on('left', namespace='/chat')
def left(message):
    room = message['room']
    username = message['username']
    # leaving the room
    leave_room(room=room)
    emit('message', {"msg": {str(username) + 'has left the room.'}}, room=room)


# if __name__ == '__main__':
# Run Flask-SocketIO App
socketio.run(app, debug=True, allow_unsafe_werkzeug=True, port='3232', host='192.168.189.1')
