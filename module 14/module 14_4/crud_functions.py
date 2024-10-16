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


def insert_product():
    for i in range(1, 5):
        cur.execute("INSERT OR REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
                       (i, f"Продукт: {i}", f"Описание: {i}", i * 100))
    con.commit()


insert_product()


def get_all_products():
    cur.execute('SELECT * FROM Products')
    products = cur.fetchall()
    return products


con.commit()
if __name__ == '__main__':
    initiate_db()
