import sqlite3 as sq
import asyncio

class DatabaseUserPay:
    def __init__(self,db_file):
       self.connection = sq.connect(db_file)
       self.cursor = self.connection.cursor()
    async def activate_sub(self,id_tg,date_pay,date_end):
        try:
            with self.connection:
                self.cursor.execute('''
                UPDATE users SET sub_active = 1, date_pay = ?, date_end = ? WHERE id_tg = ?
                ''',(date_pay,date_end,id_tg,))
        except Exception as ex:
            print(ex)
        
    
