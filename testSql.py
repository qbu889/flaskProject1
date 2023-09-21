import sqlite3

conn = sqlite3.connect('/Users/nol/PycharmProjects/flaskProject1/web2020.db')

cursor = conn.execute('SELECT content FROM news')
rows = cursor.fetchall()
forcount = len(rows)
for i in range(forcount):
    text = rows[i][0]
    print(text)
