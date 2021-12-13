import sqlite3
from sqlite3.dbapi2 import connect
# connect = sqlite3.connect('data.db')
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    id = input('아이디를 입력해주세요: ')
    sql = ('delete from topics where id = ?')    
    cursor.execute(sql, (id))
    