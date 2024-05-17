import sqlite3


conn = sqlite3.connect("db.sqlite")

c = conn.cursor()

print(c.execute("SELECT * FROM USERS LIMIT 1").fetchall())

