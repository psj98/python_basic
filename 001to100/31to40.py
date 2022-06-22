# 파이썬 문자열

# 31번
a = "3"
b = "4"
print(a + b) # 34

# 32번
print("Hi" * 3) # HiHiHi

# 33번
print("-" * 80)

# 34번
t1 = 'python'
t2 = 'java'
t3 = t1 + " " + t2 + " "
print(t3 * 4)

# 35번
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s 나이 : %d" %(name1, age1))
print("이름 : %s 나이 : %d" %(name2, age2))

# 36번
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))

# 37번
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

# 38번
상장주식수 = "5,969,782,550"
no_comma = 상장주식수.replace(',', '')
to_int = int(no_comma)
print(to_int, type(to_int))

# 39번
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40번
data = "   삼성전자    "
print(data.strip())