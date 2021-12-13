import sqlite3
from sqlite3.dbapi2 import connect
connect = sqlite3.connect('data.db')
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE topics (
        id        INTEGER      PRIMARY KEY AUTOINCREMENT,
        title     VARCHAR (50) NOT NULL,
        body      TEXT
    )
''')
cursor.close()
connect.close()