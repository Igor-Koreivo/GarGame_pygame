# -*- coding: utf-8 -*-
# Сформулируйте SQL запрос для создания таблицы book.
import sqlite3

with sqlite3.connect('book.db') as conn:
    cursor = conn.cursor()
    # Создадим таблицу.
    cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT ,
     book_id TEXT,title TEXT, author TEXT, price TEXT, amount TEXT) ''')
    # Заполняем таблицу данными.
    cursor.execute('''INSERT INTO tab_1(book_id ,title, author, price, amount) VALUES ('INT PRIMARY KEY AUTO_INCREMENT',
    'VARCHAR(50)', 'VARCHAR(30)', 'DECIMAL(8, 2)', 'INT')''')
    # Добавляем строку.
    cursor.execute('''INSERT INTO tab_1(book_id ,title, author, price, amount) VALUES ('Phiton',
    'Hello', '123', '321', 'ru')''')
    # Сохраняем изменения.
    conn.commit()
    cursor.execute('''SELECT*FROM tab_1''')
    k = cursor.fetchall()

    for i in k:
        i = list(i)
        h = 0
        print(' '.join(str(h) for h in i))
