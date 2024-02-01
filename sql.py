import sqlite3
from datetime import datetime

name_database = 'database_parser_dollars.db'


def add_database():
    connection = sqlite3.connect(name_database)
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dollars (
    id INTEGER PRIMARY KEY,
    Дата TEXT NOT NULL,
    Время TEXT NOT NULL,
    Цена_доллара INTEGER,
    Комментарий TEXT,
    Разница TEXT
    )
    ''')
    connection.commit()
    connection.close()


def add_column(name_table, name_colum, data_type):
    connection = sqlite3.connect(name_database)
    cursor = connection.cursor()
    cursor.execute(f'''
        ALTER TABLE {name_table} 
        ADD {name_colum} {data_type};
    ''')
    connection.commit()
    connection.close()


# add_column('Dollars', 'Разница', "TEXT")


def insert_into_dollars(price, difference):
    connection = sqlite3.connect(name_database)
    cursor = connection.cursor()
    date = datetime.now().date()
    time_now = str(datetime.now().time())[:8]
    cursor.execute(f'''INSERT INTO Dollars (Дата, Время, Цена_доллара, Разница )
    VALUES ('{date}', '{time_now}' , {price}, '{difference}');
    ''')
    connection.commit()
    connection.close()


def select_last_telegram():
    connection = sqlite3.connect(name_database)
    cursor = connection.cursor()
    date = datetime.now().date()
    time_now = str(datetime.now().time())[:8]
    a = cursor.execute(f'''select Дата,Время,Цена_доллара from Dollars order by id desc
limit 1;''')
    for i in a:
        return f'{i[2]} - - {i[1]} || {i[0]}'
    connection.commit()
    connection.close()

def select_last_float():
    connection = sqlite3.connect(name_database)
    cursor = connection.cursor()
    date = datetime.now().date()
    time_now = str(datetime.now().time())[:8]
    a = cursor.execute(f'''select Дата,Время,Цена_доллара from Dollars order by id desc
limit 1;''')
    for i in a:
        return i[2]
    connection.commit()
    connection.close()

# f'''INSERT INTO Dollars (Дата, Время, Цена)
#    VALUES ({date}, {time_now}, {price});
#    '''
