from flaskext.mysql import MySQL

class Manager:
    def __init__(self, mysql : MySQL) -> None:
        self.mysql = mysql
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS game_overview(uid VARCHAR(30),white_player VARCHAR(20),black_player VARCHAR(20),outcome VARCHAR(8))''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS game_moves(uid VARCHAR(30),moves VARCHAR(5))''')
        cursor.close()
        conn.close()


    def store_moves(self, uid,move):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO game_moves VALUES(%s, %s)''',(uid,move))
        cursor.close()
        conn.close()

    def store_outcome(self,uid,white_player, black_player, outcome ):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO game_overview VALUES(%s, %s, %s, %s)''',(uid,white_player,black_player,outcome))
        cursor.close()
        conn.close()
