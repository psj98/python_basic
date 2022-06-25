# 파이썬 함수

# 221번
def print_reverse(string):
  print(string[::-1])

# 222번
def print_score(score):
  print(sum(score)/len(score))

# 223번
def print_even(even):
  for i in even:
    if i % 2 == 0:
      print(i)

# 224번
def print_keys(keys):
  for key in keys.keys():
    print(key)

# 225번
def print_value_by_key(input_dict, date):
  print(input_dict[date])

# 226번
def print_5xn(string):
  for i in range(int(len(string) / 5) + 1):
    print(string[i * 5:i * 5 + 5])

# 227번
def printmxn(string, num):
  for i in range(int(len(string) / num) + 1):
    print(string[i * num:i * num + num])

# 228번
def calc_monthly_salary(num):
  print(int(num / 12))

# 229번
# 왼쪽: 100
# 오른쪽: 200

# 230번
# 왼쪽: 200
# 오른쪽: 100