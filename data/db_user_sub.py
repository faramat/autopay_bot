import sqlite3 as sq
import asyncio,datetime
from aiogram import Bot
from config import Tokens


class DatabaseUserSub:
    def __init__(self,db_file):
       self.connection = sq.connect(db_file)
       self.cursor = self.connection.cursor()
    async def check_sub(self,id_tg):
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
    async def check_date_end(self,bot:Bot):
        try:
            with self.connection:
                response = self.cursor.execute('''
                SELECT * FROM users WHERE sub_active = 1
                ''').fetchall()
                for i in range(len(response)):
                    today = datetime.datetime.now()
                    today = (int(today.timestamp()))
                    date_end = self.cursor.execute('''
                    SELECT date_end FROM users WHERE id_tg = ?
                    ''',(response[i][1],)).fetchone()
                    if int(date_end[0]) - today < 0:
                        request = self.cursor.execute('''
                        UPDATE users SET sub_active = 0 WHERE id_tg = ?
                        ''',(response[i][1],))
                        await bot.ban_chat_member(
                            chat_id=f'{Tokens.private_channel_id}',
                            user_id=f'{response[i][1]}',
                            until_date=datetime.timedelta(seconds=31))
        except Exception as ex:
            return False
