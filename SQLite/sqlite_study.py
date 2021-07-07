import sqlite3
import csv
# db 파일 여는법
a = sqlite3.connect('testdb.db')
cur = a.cursor()    # 해당스키마를 바라보게함
a.execute("INSERT into Artists values (?, ?)", (None, 'kyobong'))    # 단일 삽입

with open('testdb.csv', 'r', encoding='utf-8') as ifp:
    csv_data = csv.reader(ifp)
    # t_csv_data = [tuple(row) for row in csv_data]
    t_csv_data = list(csv_data)
    # print(t_csv_data)
    for i in t_csv_data:
        # print(i[0])
        a.execute("INSERT into Artists values ( ?, ?)", (None, i[0]))    # 대량삽입


for row in cur.execute('SELECT * FROM Artists'):  # sql
    print(row)
