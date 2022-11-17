# -*- coding: utf-8 -*-
import sqlite3
# создаём 2 таблицы (по 1 колонке, 1 - текст, 2 - числа)
conn = sqlite3.connect('2tab.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT , col_1 TEXT) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT , col_1 INTEGER) ''')
conn.commit()
Spisok = [1, 3, 'black', 7, 8, 'red', 'white', 4, 5]
print('Наш список', Spisok)
for i in Spisok:
    if type(i) is str:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (i, ))
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (len(i),))
        conn.commit()
    elif type(i) is int:
        if i % 2 == 0:
            cursor.execute(f'''INSERT INTO tab_2(col_1) VALUES ({i})''')
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES ('нечётное')''')
            conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
tab1 = cursor.fetchall()
print(tab1)
cursor.execute('''SELECT*FROM tab_2''')
tab2 = cursor.fetchall()
print(tab2)
if len(tab2) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')# удаляем 1 эл. в таб 1
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')# заменяем 1 эл. в таб 1
    conn.commit()
cursor.execute('''SELECT col_1 FROM tab_1''')
tab1 = cursor.fetchall()
print('Таблица № 1', tab1)
cursor.execute('''SELECT col_1 FROM tab_2''')
tab2 = cursor.fetchall()
print('Таблица № 2', tab2)