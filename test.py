

import sqlite3 as sq
import asyncio

class DatabaseUserPay:
    def __init__(self,db_file):
       self.connection = sq.connect(db_file)
       self.cursor = self.connection.cursor()
    def activate_sub(self,id_tg,date_pay,date_end):
        print(self)
        try:
            with self.connection:
                self.cursor.execute('''
                UPDATE users SET sub_active = 1, date_pay = ?, date_end = ? WHERE id_tg = ?
                ''',(date_pay,date_end,id_tg,))
        except Exception as ex:
            print(ex)
        
class DatabaseUserSub:
    def __init__(self,db_file):
       self.connection = sq.connect(db_file)
       self.cursor = self.connection.cursor()
    def check_sub(self,id_tg):
        try:
            with self.connection:
                res = self.cursor.execute('''
                SELECT * FROM users WHERE id_tg = ?
                ''',(id_tg,)).fetchone()
            if res[3] == 1:
                return True
            else:
                return False
        except Exception as ex:
            return False
        
    

# res = DatabaseUserPay.activate_sub("x",'456','789')
rest = DatabaseUserSub.check_sub('123')
print(res)
print(rest)