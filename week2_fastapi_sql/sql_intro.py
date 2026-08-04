import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Ali", 21))

people = [("Shoaib",25), ("Rafhan", 20), ("Ahmad", 23), ("Haseeb", 22)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", people)

cursor.execute("SELECT * FROM users WHERE age > 20")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()