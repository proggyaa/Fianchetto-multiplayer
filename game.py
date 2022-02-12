from player import Player


class Game:
    def __init__(self, uid: str, challenger: Player, opponent: Player) -> None:
        self.uid = uid
        self.challenger = challenger
        self.opponent = opponent

    def move(self, move: str, outcome: str, player: str):
        if self.challenger.name == player:
            self.opponent.send_move_to_client(move+" "+outcome)
        else:
            self.challenger.send_move_to_client(move+" "+outcome)

    def end(self):
        self.challenger.terminate_connection_with_client()
        self.opponent.terminate_connection_with_client()
