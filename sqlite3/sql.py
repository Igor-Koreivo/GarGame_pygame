# -*- coding: utf-8 -*-
import sqlite3

# Создаём Базу данных
conn = sqlite3.connect('name1.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')

# Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
# Сохраняем изменения
conn.commit()

d = "red"
f = "black"
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
cursor.execute('''INSERT INTO tab_2(col_1,col_2) VALUES (?,?)''', (d, f))
conn.commit()

cursor.execute('''SELECT*FROM tab_2''')
k = cursor.fetchall()
print(k)