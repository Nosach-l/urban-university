import sqlite3


con = sqlite3.connect('not_telegram.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cur.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
for i in range(1, 11):
    cur.execute('INSERT INTO Users(username, email, age ,balance) VALUES(?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

for i in range(1, 11, 2):
    cur.execute('UPDATE Users SET balance = ? WHERE id = ?', ('500', f'{i}'))

for i in range(1, 11, 3):
    cur.execute('DELETE FROM Users WHERE id = ?', (f'{i}',))

cur.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', ('60',))
users = cur.fetchall()
for user in users:
    print(user)
con.commit()
con.close()
