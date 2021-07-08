import sqlite3
import csv
# db 파일 여는법
a = sqlite3.connect('testdb.db')
cur = a.cursor()    # 해당스키마를 바라보게함
a.execute("INSERT into Artists values (?, ?)", (None, 'kyobong'))    # 단일 삽입

with open('testdb.csv', 'r', encoding='utf-8') as ifp:
    csv_data = list(csv.reader(ifp))
    for i in csv_data:
        a.execute("INSERT into Artists values ( ?, ?)", (None, ','.join(i)))    # 대량삽입


for row in cur.execute('SELECT * FROM Artists'):  # sql
    print(row)
