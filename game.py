from player import Player 

class Game:
    def __init__(self, uid : str, challenger : Player, opponent: Player) -> None:
        self.uid = uid 
        self.challenger = challenger
        self.opponent = opponent
    
    def move(self, move : str, player: str):
        if self.challenger.name == player:
            self.opponent.send_move_to_client(move)
        else:
            self.challenger.send_move_to_client(move)