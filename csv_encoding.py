import csv
import chardet
import pandas as pd

# csv 파이르이 인코딩 형식보는 코드
# filename = "C:\plugins\\argoslabs\datanalysis\pandas3\\tests\Source1.csv"
# filename = "C:\plugins\\argoslabs\datanalysis\pandas3\\tests\Target2.csv"
# with open(filename, 'rb') as f:
#     result = chardet.detect(f.readline())  # or read() if the file is small.
#     print(result['encoding'])
#     f.close()
# with open(filename, 'r', encoding="Shift_JIS") as j:
#     rdr = csv.reader(j)
#
#     for line in rdr:
#         print(line)
#     j.close()
# with open("test.txt")as text:
#     t=text.read()
#     print(t)
# a = [1,2,3,4,5,6]
# print(a[-1])
# print(a[-2])

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1])