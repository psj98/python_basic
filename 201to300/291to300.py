# 파이썬 파일 입출력과 예외처리

# 291번
f = open("C:/매수종목1.txt", 'w')

f.write('005930\n')
f.write("005380\n")
f.write("035420")

f.close()

# 292번
f = open("C:/매수종목2.txt", 'w')

f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")

f.close()

# 293번
import csv

f = open("C:/매수종목.csv", mode='w', encoding='cp949', newline='')

writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])

f.close()

# 294번
f = open("C:/매수종목1.txt", 'r')

lines = f.readlines()

code = []
for i in lines:
  a = i.strip()
  code.append(a)

print(code)

f.close()

# 295번
f = open("C:/매수종목2.txt", 'r')

lines = f.readlines()

data = {}
for i in lines:
  a = i.strip()
  k, v = a.split(' ')
  data[k] = v

print(data)

f.close()

# 296번
per = ["10.31", "", "8.00"]

for i in per:
  try:
    print(float(i))

  except:
    print(0)

# 297번
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
  try:
    val = float(i)
  except:
    val = 0

  new_per.append(val)
  
print(new_per)

# 298번
try:
  a = 2 / 0
except ZeroDivisionError:
  print('0으로 나눔')

# 299번
data = [1, 2, 3]

for i in range(5):
  try:
    print(data[i])
  except IndexError as e:
    print(e)

# 300번
per = ["10.31", "", "8.00"]

for i in per:
  try:
    print(float(per))
  except:
    print(0)
  else:
    print('no data')
  finally:
    print('종료')