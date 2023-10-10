import sqlite3 as sq
import asyncio

class DatabaseUser:
    def __init__(self,db_file):
       self.connection = sq.connect(db_file)
       self.cursor = self.connection.cursor()
    def user_start(self,id_tg,login_tg):
       with self.connection:
           self.cursor.execute('''
           INSERT INTO users(id_tg,login_tg,sub_active,date_pay,date_end) VALUES (?,?,0,0,0)
           ''',(id_tg,login_tg,))
    def user_exists_start(self,id_tg):
       with self.connection:
           result = self.cursor.execute('''
           SELECT * FROM users WHERE id_tg = ?
           ''',(id_tg,)).fetchall()
       return bool(len(result))
