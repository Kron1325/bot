import sqlite3

# Создаем или открываем базу данных
conn = sqlite3.connect('example.db')

# Создаем курсор для выполнения операций
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Вставляем данные
cursor.execute(

)

cursor.execute(
    
)

# Сохраняем изменения
conn.commit()

# Выбираем данные
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Выводим данные
for row in rows:
    print(row)

# Закрываем соединение
conn.close()
