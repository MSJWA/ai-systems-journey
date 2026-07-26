import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()