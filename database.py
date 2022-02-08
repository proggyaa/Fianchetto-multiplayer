from flaskext.mysql import MySQL

class Manager:
    def __init__(self, mysql : MySQL) -> None:
        self.mysql = mysql
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS game_overview(uid,white_player,black_player,outcome)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS game_moves(uid,moves)''')
        cursor.close()
        conn.close()


    def store_moves(self, uid,move):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO game_moves VALUES(%s,%s)''',(uid,move))
        cursor.close()
        conn.close()

    def store_outcome(self,uid,white_player, black_player, outcome ):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO game_overview VALUES(%s,%s,%s,%s)''',(uid,white_player, black_player, outcome))
        cursor.close()
        conn.close()
