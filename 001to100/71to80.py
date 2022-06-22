# 파이썬 튜플

# 71번
my_variable = ()

# 72번
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# 73번
num = (1, ) # 쉼표를 붙여야 Tuple로 인식

# 74번
t = (1, 2, 3)
t[0] = 'a' # Tuple은 수정 불가

# 75번
t = 1, 2, 3, 4 # Tuple : 괄호 없어도 동작

# 76번
t = ('a', 'b', 'c') # 값 변경 불가 -> 기존 튜플 삭제 후, 새로 생성

# 77번
interest = ('삼성전자', 'LG전자', 'SK Hynix')
li_interest = list(interest)
print(type(li_interest))

# 78번
interest = ['삼성전자', 'LG전자', 'SK Hynix']
tu_interest = tuple(interest)
print(type(tu_interest))

# 79번
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) # apple, banana, cake

# 80번
num = tuple(range(2, 100, 2))
print(num)