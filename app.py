import flask
from flask import Response
from flask import Flask, request
from flask_sock import Sock
from game_manager import Game_Manager

app = Flask(__name__)
sock = Sock(app)

game_manager = Game_Manager()


if __name__ == "__main__":
    app.run()



@sock.route("/play")
def move(ws):
    player = request.args.get("player")
    uid = request.args.get("game_id")
    outcome = 'NO'
    game_manager.establish_connection(uid, player, ws)
    while True:
        move, outcome = ws.receive().split(" ")
        if outcome != 'NO':
            break
        game_manager.make_move(uid, move, player)
    return "", 200


@app.route("/challenge")
def challenge():
    challenger = request.args.get("username")
    opponent = request.args.get("opponent_username")
    game_id = game_manager.start_game(challenger, opponent)
    resp = flask.Response(game_id)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp, 201


'''
Dummy endpoint for testing websocket interactiveness
'''
# chat_db = dict()


# @sock.route("/chat")
# def move(ws):
#     sender = request.args.get('sender')
#     id = request.args.get('id')
#     if id not in chat_db:
#         chat_db[id] = []
#     chat_db[id].append(ws)
#     while True:
#         msg = ws.receive()
#         for chat_ws in chat_db[id]:
#             chat_ws.send(sender + " : " + msg)
#     return "", 200
