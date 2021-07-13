import sqlite3
import csv
# db 파일 여는법
a = sqlite3.connect('testdb.db')
cur = a.cursor()    # 해당스키마를 바라보게함
# cur.execute("INSERT into Artists values (?, ?)", (None, 'kyobong'))    # 단일 삽입
cur.execute("INSERT into Artists (ArtistId,ArtistName) values (30, 'kyobong')")    # 단일 삽입
# cur.execute("INSERT into Artists (ArtistId,ArtistName) values (?, ?)", (None, 'kyodsfdsa'))    # 대량삽입

#
#     csv_data = list(csv.reader(ifp))
#     header = csv_data.pop(0)
#     # print(header, len(csv_data[0]))
#     value_c = []
#     for i in range(len(csv_data[0])):
#         value_c.append('?')
#     for i in csv_data:
#         # print(i[1])
#         # csv = ','.join(i)
#         # print(','.join(header))
#         cur.execute("INSERT into Artists (%s) values (%s)" % (','.join(header), ','.join(value_c)), (None, i[1]))
#     cur.execute('SELECT * FROM Artists WHERE ArtistId = 2')
#     print(cur.fetchall())
#         # cur.execute("INSERT into Artists (ArtistName) values (?)", csv)    # 대량삽입
with open('testdb.csv', 'r', encoding='utf-8') as ifp:
    cooked = csv.reader(ifp)
    sql = "INSERT INTO Albums (AlbumName, Year, ArtistName) VALUES ('{0}', '{1}', '{2}')"
    for i, record in enumerate(cooked):
        esql = sql.format(*record)
        cur.execute(esql)


for row in cur.execute('SELECT * FROM Artists'):  # sql
    print(row)
# print(header, len(csv_data))

