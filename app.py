import socketserver
from flask import Flask, request, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)
websocket_pool = dict()
game_map = dict()

if __name__ == "__main__":
    app.run()


@sock.route("/play")
def check(ws):
    challenger = request.args.get("player")
    websocket_pool[challenger] = ws
    while True:
        move = ws.receive()
        opponent = game_map[challenger]
        websocket_pool[opponent].send(move)
    return "", 200


@app.route("/challenge")
def challenge():
    challenger = request.json["username"]
    opponent = request.args.get("opponent_username")
    if opponent in game_map or challenger in game_map:
        return "Can't start a new game! One player is already playing a game", 400
    game_map[challenger] = opponent
    game_map[opponent] = challenger
    return "", 201
