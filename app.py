import socketserver
import uuid
from flask import Flask, request, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)
websocket_pool = dict()
game_map = dict()
last_player = dict()

if __name__ == "__main__":
    app.run()

@sock.route("/play")
def move(ws):
    challenger = request.args.get("player")
    uid = request.args.get("gameId")
    websocket_pool[challenger] = ws
    
    while True:
        move = ws.receive()
        if last_player[uid] ==  challenger:
            return "Error",400
        
        last_player[uid] = challenger
        opponent = game_map[challenger]
        websocket_pool[opponent].send(move)
        return "", 200


@app.route("/challenge")
def challenge():
    challenger = request.json["username"]
    opponent = request.args.get("opponent_username")
    if opponent in game_map or challenger in game_map:
        return "Can't start a new game! One player is already playing a game", 400
    
    global game_id
    game_id = str(uuid.uuid4())
    while game_id in last_player:
        game_id = str(uuid.uuid4())    
    last_player[game_id] = opponent
    return "", 201
