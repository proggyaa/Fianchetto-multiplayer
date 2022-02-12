import uuid
from game import Game
from player import Player


class Game_Manager:
    def __init__(self) -> None:
        self.game_map = dict()

    def start_game(self, challenger_name: str, opponent_name: str) -> str:
        challenger = Player(name=challenger_name, ws_connection=None)
        opponent = Player(name=opponent_name, ws_connection=None)
        uid = str(uuid.uuid4())
        game = Game(uid, challenger, opponent)
        print("DEBUG game", game)
        print("DEBUG game map", self.game_map)
        self.game_map[uid] = game
        return uid

    def establish_connection(self, uid: str, player: str, ws_connection):
        game = self.game_map[uid]
        if game.challenger.name == player:
            game.challenger.ws_connection = ws_connection
        else:
            game.opponent.ws_connection = ws_connection

    def make_move(self, uid: str, move: str, outcome: str, player: str):
        self.game_map[uid].move(move, outcome, player)

    def end_game(self, uid: str):
        self.game_map[uid].end()
        del self.game_map[uid]
