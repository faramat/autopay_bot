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
        id_tg = "12345"
        logih_tg = "ewrwerwer"
        sub_active = 1
        date_pay = "12345"
        date_end = "65432"
        
        cursor.execute('''
        INSERT INTO users(id_tg,login_tg,sub_active,date_pay,date_end) VALUES (?,?,?,?,?)
        ''',(id_tg,logih_tg,sub_active,date_pay,date_end,))

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


if __name__ == '__main__':
    sql_start()