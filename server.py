from flask import Flask, jsonify, request
from flask_socketio import SocketIO, join_room, leave_room, emit
import os
from socket_methods import *

##############################################

os.environ.setdefault('FLASK_ENV', 'development')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'
# CORS_ALLOWED_ORIGINS is the list of origins authorized to make requests.
socketio = SocketIO(app, cors_allowed_origins='*')


#################################################

# Home Page
@app.route('/', methods=['GET', 'POST'])
# @app.route('/')
def index():
    return jsonify({'data': "Web Socket Example"})


#################################################

####Declarations#####################
host = '192.168.65.1'
port = 49152


#################################################

@socketio.on('connect')
def on_connect():
    connect()


@socketio.on('disconnect')
def on_disconnect():
    disconnect()


@socketio.on('create_game_private')
def on_create_game_private(req):
    create_game_private(req)


@socketio.on('join_game')
def on_join_game(req):
    join_game(req)


@socketio.on('create_game_public')
def on_create_game_public(req):
    create_game_public(req)


@socketio.on('join_game')
def on_join_game(req):
    join_game(req)


@socketio.on('play_game')
def on_play_game(req):
    play_game(req)


socketio.run(app, port=port, host=host)
