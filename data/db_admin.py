import sqlite3 as sq
import asyncio

class DatabaseAdmin:
    def __init__(self,db_file):
       self.connection = sq.connect(db_file)
       self.cursor = self.connection.cursor()
    async def getPrice(self):
        try:
            with self.connection:
                response = self.cursor.execute('''
                SELECT * FROM price
                ''').fetchone()
            data = []
            data.append(response[1])
            data.append(response[2])
            data.append(response[3])
            return data
        except Exception as ex:
            print(ex)
    async def updatePrice(self,data):
        try:
            with self.connection:
                self.cursor.execute('''
                UPDATE price SET first_sum = ?, second_sum = ?, third_sum = ? WHERE id = 1
                ''',(data['first_sum'],data['second_sum'],data['third_sum'],))
        except Exception as ex:
            print(ex)
    async def get_users(self):
        try:
            with self.connection:
                res = self.cursor.execute('''SELECT * FROM users''').fetchall()
                return res
        except Exception as ex:
            print(ex)
    
