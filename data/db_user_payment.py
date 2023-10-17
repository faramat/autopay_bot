import sqlite3 as sq
import asyncio

class DatabaseUserSub:
    def __init__(self,db_file):
       self.connection = sq.connect(db_file)
       self.cursor = self.connection.cursor()
    def activate_sub(self,id_tg):
        try:
            with self.connection:
                res = self.cursor.execute('''
                UPDATE users SET sub_active = 1 WHERE id_tg = ?
                ''',(id_tg,)).fetchone()
            if res[3] == 1:
                return True
            else:
                return False
        except Exception as ex:
            return False
        
    
