from operator import le
import socketserver
import uuid
from flaskext.mysql import MySQL
from flask import Flask, request
from flask_sock import Sock
import database

app = Flask(__name__)
sock = Sock(app)
websocket_pool = dict()
game_map = dict()
last_player = dict()

if __name__ == "__main__":
    app.run()

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'fianchetto'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
db = database.Manager(mysql)


@sock.route("/play")
def move(ws):
    challenger, white, black = request.args.get(
        "challenger"), request.args.get("white"), request.args.get("black")
    uid = request.args.get("game_id")
    websocket_pool[challenger] = ws
    outcome = 'NO'

    while True:
        move, outcome = ws.receive().split(" ")
        if last_player[uid] == challenger:
            return "Error", 400

        db.store_moves(uid, move)
        last_player[uid] = challenger
        opponent = game_map[challenger]

        if outcome != 'NO':
            break
        websocket_pool[opponent].send(move+" "+outcome)

    del game_map[challenger]
    del game_map[opponent]
    db.store_outcome(uid, white, black, outcome)
    return "", 200


@app.route("/challenge")
def challenge():
    challenger = request.json["username"]
    opponent = request.args.get("opponent_username")
    if opponent in game_map or challenger in game_map:
        return "Can't start a new game! One player is already playing a game", 400

    game_map[opponent] = challenger
    game_map[challenger] = opponent
    game_id = str(uuid.uuid4())[:30]
    last_player[game_id] = opponent
    return game_id, 201
