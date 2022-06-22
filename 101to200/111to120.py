# 파이썬 분기문

# 111번
a = input("입력 : ")
print(a * 2)

# 112번
num = input("숫자를 입력하세요 : ")
print(int(num) + 10)

# 113번
num = input("숫자 입력 : ")
if int(num) % 2 == 0:
  print("짝수")
else:
  print("홀수")

# 114번
num = input("숫자 입력 : ")
result = int(num) + 20
if result > 255:
  print(255)
else:
  print(result)

# 115번
num = input("숫자 입력 : ")
result = int(num) - 20
if result < 0:
  print(0)
elif result > 255:
  print(255)
else:
  print(result)

# 116번
time = input("현재 시간 : ")
if time[-2:] == '00':
  print("정각입니다.")
else:
  print("정각이 아닙니다.")

# 117번
fruit = ["사과", "포도", "홍시"]
result = input("좋아하는 과일은? ")
if result in fruit:
  print("정답입니다.")
else:
  print("오답입니다.")

# 118번
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
result = input("종목명 : ")
if result in warn_investment_list:
  print("투자 경고 종목입니다.")
else:
  print("투자 경고 종목이 아닙니다.")

# 119번
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
result = input("제가 좋아하는 계절은 : ")
if result in fruit:
  print("정답입니다.")
else:
  print("오답입니다.")

# 120번
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
result = input("좋아하는 과일은? ")
if result in fruit.values():
  print("정답입니다.")
else:
  print("오답입니다.")