import sqlite3
from sqlite3.dbapi2 import connect
# connect = sqlite3.connect('data.db')
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    id = input('업데이트하려는 아이디를 알려주세요 : ')

    sql = ('select id, title, body from topics where id = ?')
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    title = row[1]
    body = row[2]
    input_title = input(f'제목 ({title}):')
    input_body = input(f'본문 ({body}):')

    sql = 'update topics set title = ?, body = ? where id = ?'
    cursor.execute(sql, (input_title, input_body, id))