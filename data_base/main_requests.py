import sqlite3


def sql_start():
    try:
        global connection,cursor
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        print('[INFO] Data base connected!')
        cursor.execute('''CREATE TABLE IF NOT EXISTS sellers(
        id integer PRIMARY KEY AUTOINCREMENT,
        id_tg text,
        login_tg text,
        country text)
        ''')
        
        connection.commit()

        cursor.execute('''CREATE TABLE IF NOT EXISTS shops(
        id integer PRIMARY KEY AUTOINCREMENT,
        seller_id integer,
        ozon_client_id text,
        ozon_api_key text,
        FOREIGN KEY (seller_id)  REFERENCES sellers (id))
        ''')

        connection.commit()
    except Exception as ex:
        print('[INFO] Error while working with SQLite: ', ex)
        return False
    finally:
        if connection:
            print('[INFO] Data base closed! OK')
            return True

#Заполнение бд           
# def addInfoSellers(personId,username,country):
#     cursor.execute(f'SELECT id_tg FROM users WHERE id_tg = {personId};')
#     if cursor.fetchone() is None:
#         cursor.execute(f'INSERT INTO users(id_tg,login_tg,country) VALUES(?,?,?);',(personId,username,country))
#         connection.commit()
#     else:
#         connection.commit()