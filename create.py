import sqlite3
from sqlite3.dbapi2 import connect
# connect = sqlite3.connect('data.db')
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    title = input('제목을 알려주세요 : ')
    body = input('본문을 알려주세요 : ')

    sql = ('insert into topics (title,body) values (?,?)')
    cursor.execute(sql, (title, body))
    connect.commit()