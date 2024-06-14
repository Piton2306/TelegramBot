from datetime import datetime

import psycopg2

# host.docker.internal используя докер
# localhost, без докера
try:
    # пытаемся подключиться к базе данных
    connection = psycopg2.connect(dbname='postgres', host='host.docker.internal', port='5432', user='root',
                                  password='12345')
    print("Подключение установлено")
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Ошибка соединения с БД')


def add_database():
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dollars (
    id SERIAL PRIMARY KEY,
    Дата TEXT NOT NULL,
    Время TEXT NOT NULL,
    Цена_доллара FLOAT,
    Комментарий TEXT,
    Разница TEXT
    )
    ''')
    connection.commit()


def add_column(name_table, name_colum, data_type):
    cursor = connection.cursor()
    cursor.execute(f'''
        ALTER TABLE {name_table} 
        ADD {name_colum} {data_type};
    ''')
    connection.commit()


# add_column('Dollars', 'Разница', "TEXT")


def insert_into_dollars(price, difference):
    cursor = connection.cursor()
    date = datetime.now().date()
    time_now = str(datetime.now().time())[:8]
    cursor.execute(f'''INSERT INTO Dollars (Дата, Время, Цена_доллара, Разница )
    VALUES ('{date}', '{time_now}' , {price}, '{difference}');
    ''')
    connection.commit()


def select_last_telegram():
    cursor = connection.cursor()
    date = datetime.now().date()
    time_now = str(datetime.now().time())[:8]
    cursor.execute(f'''select Дата,Время,Цена_доллара from Dollars order by id desc
limit 1;''')
    a = cursor.fetchone()
    cursor.close()
    return f'{a[2]} - - {a[1]} || {a[0]}'


def select_last_float():
    cursor = connection.cursor()
    cursor.execute(f'''select Дата,Время,Цена_доллара from Dollars order by id desc
limit 1;''')
    a = cursor.fetchone()
    cursor.close()
    return a[2]
# f'''INSERT INTO Dollars (Дата, Время, Цена)
#    VALUES ({date}, {time_now}, {price});
#    '''
