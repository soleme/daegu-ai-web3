import sqlite3
from sqlite3.dbapi2 import connect
# connect = sqlite3.connect('data.db')
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    sql = ('select id, title, body from topics')
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    