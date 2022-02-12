class Player:
    def __init__(self, name, ws_connection) -> None:
        self.name = name 
        self.ws_connection = ws_connection
    
    def send_move_to_client(self, move : str):
        self.ws_connection.send(move)
