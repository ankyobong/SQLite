import csv
import chardet
import pandas as pd

# csv 파이르이 인코딩 형식보는 코드
# filename = "C:\plugins\\argoslabs\datanalysis\pandas3\\tests\Source1.csv"
filename = "C:\plugins\\argoslabs\datanalysis\pandas3\\tests\Target2.csv"
with open(filename, 'rb') as f:
    result = chardet.detect(f.readline())  # or read() if the file is small.
    print(result['encoding'])
    f.close()
# with open(filename, 'r', encoding="Shift_JIS") as j:
#     rdr = csv.reader(j)
#
#     for line in rdr:
#         print(line)
#     j.close()