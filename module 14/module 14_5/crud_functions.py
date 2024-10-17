import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()


def initiate_db():
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


def insert_product():
    for i in range(1, 5):
        cur.execute("INSERT OR REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
                    (i, f"Продукт: {i}", f"Описание: {i}", i * 100))
    con.commit()


def get_all_products():
    cur.execute('SELECT * FROM Products')
    products = cur.fetchall()
    return products


def add_users(username, email, age):
    cur.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                (username, email, age, '1000'))
    con.commit()


def is_included(username):
    user_list = cur.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    if user_list is None:
        return False
    else:
        return True


con.commit()

if __name__ == '__main__':
    initiate_db()
