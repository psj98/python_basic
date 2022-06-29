# 파이썬 모듈

# 241번
import datetime

now = datetime.datetime.now()

print(now)

# 242번
print(type(now))

# 243번
for i in range(5, 0, -1):
  a = datetime.timedelta(days = i)
  date = now - a
  print(date)

# 244번
print(now.strftime('%H:%M:%S'))

# 245번
day = '2020-05-04'
a = datetime.datetime.strptime(day, "%Y-%m-%d")
print(a)

# 246번
import time

while True:
  print(now)
  time.sleep(1)

# 247번
# import 모듈이름
# from 모듈 이름 import 모듈 함수

# 248번
import os

a = os.getcwd()
print(a)

# 249번
os.rename("C:/Users/본인디렉토리/test.txt", "C:/Users/본인디렉토리/now.txt")

# 250번
# float이기 때문에 numpy.arange 사용
import numpy

for i in numpy.arange(0, 5, 0.1):
    print(i)