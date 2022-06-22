# 파이썬 분기문

# 121번
a = input('')

if a.islower():
  print(a.upper())
else:
  print(a.lower())

# 122번
score = input("score: ")
score = int(score)

if 81 <= score <= 100:
  print("grade is A")
elif 61 <= score <= 80:
  print("grade is B")
elif 41 <= score <= 60:
  print("grade is C")
elif 21 <= score <= 40:
  print("grade is D")
else:
  print("grade is E")

# 123번
money = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
num = input("입력 : ")
name, currency = num.split(' ')
print(float(name) * money[currency], "원")

# 124번
num1 = int(input("input number1 : "))
num2 = int(input("input number2 : "))
num3 = int(input("input number3 : "))

if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)

# 125번
phone = input("휴대전화 번호 입력 : ")
num = phone.split('-')[0]

if num == '011':
  com = 'SKT'
elif num == '016':
  com = 'KT'
elif num == '019':
  com = 'LGU'
else:
  com = '알수없음'
print(f"당신은 {com} 사용자입니다.")

# 126번
num = input("우편번호 : ")

if num[:3] in ['010', '011', '012']:
  print('강북구')
elif num[:3] in ['013', '014', '015']:
  print('도봉구')
else:
  print('노원구')

# 127번
num = input("주민등록번호 : ")
a, b = num.split('-')

if b[0] == '1' or b[0] == '3':
  print("남자")
else:
  print("여자")

# 128번
num = input("주민등록번호 : ")
a, b = num.split('-')

if 0 <= int(b[1:3]) <=8:
  print("서울입니다.")
else:
  print("서울이 아닙니다.")

# 129번
num = input("주민등록번호 : ")
total = 0
count = 2

for i in range(12):
  if count > 9:
    count = 2
  if i >= 6:
    i += 1
  total += int(num[i]) * count 
  count += 1

if 11 - int(str(total % 11)[-1]) == int(num[-1]):
  print('유효한 주민등록번호입니다.')
else:
  print('유효하지 않은 주민등록번호입니다.')

# 130번
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

change = float(btc['max_price']) - float(btc['min_price'])
price = float(btc['opening_price'])
max_pr = float(btc['max_price'])

if (change + price) > max_pr:
  print('상승장')
else:
  print('하락장')