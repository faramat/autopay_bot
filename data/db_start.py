import sqlite3
    
def sql_start():
    try:
        global connection,cursor
        connection = sqlite3.connect('autopay.db')
        cursor = connection.cursor()
        print('[INFO] Data base connected!')
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY AUTOINCREMENT,
        id_tg text,
        login_tg text,
        sub_active bool,
        date_pay text,
        date_end text
        )
        ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS price(
        id integer PRIMARY KEY AUTOINCREMENT,
        first_sum text,
        second_sum text,
        third_sum text
        )
        ''')
        response = cursor.execute('''
        SELECT * FROM price
        ''').fetchall()
        if response:
            pass
        else:
            cursor.execute('''
            INSERT INTO price(first_sum,second_sum,third_sum) VALUES(?,?,?)
            ''',('0','0','0'))
        connection.commit()
    except Exception as ex:
        print('[INFO] Error while working with SQLite: ', ex)
        return False
    finally:
        if connection:
            print('[INFO] Data base closed! OK')
            return True
