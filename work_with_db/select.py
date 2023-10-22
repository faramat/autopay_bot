import sqlite3,datetime

def sql_start():
    try:
        global connection,cursor
        connection = sqlite3.connect('autopay.db')
        cursor = connection.cursor()     
        response = cursor.execute('''
        SELECT * FROM users WHERE sub_active = 1
        ''').fetchall()

        for i in range(len(response)):
            today = datetime.datetime.now()
            today = (int(today.timestamp()))
            date_end = cursor.execute('''
            SELECT date_end FROM users WHERE id_tg = ?
            ''',(response[i][1],)).fetchone()
            if int(date_end[0]) - today < 0:
                request = cursor.execute('''
                UPDATE users SET sub_active = 0 WHERE id_tg = ?
                ''',(response[i][1],))
        connection.commit()

    except Exception as ex:
        print('[INFO] Error while working with SQLite: ', ex)
        return False
    finally:
        if connection:
            print('[INFO] Data base closed! OK')
            return True


if __name__ == '__main__':
    sql_start()




        # today = datetime.datetime.now()
        # date_pay = (int(today.timestamp()))
        # delta = datetime.timedelta(days=7)
        # date_end = today + delta
        # date_end = int(date_end.timestamp())