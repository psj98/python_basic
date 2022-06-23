# 파이썬 반복문

# 141번
리스트 = [100, 200, 300]
for i in 리스트:
  print(i+10)

# 142번
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
  print('오늘의 메뉴 : ', i)

# 143번
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
  print(len(i))

# 144번
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
  print(i, len(i))

# 145번
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
  print(i[0])

# 146번
리스트 = [1, 2, 3]
for i in 리스트:
  print('3 *', i)

# 147번
리스트 = [1, 2, 3]
for i in 리스트:
  print('3 *', i, '=', 3 * i)

# 148번
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
  print(i)

# 149번
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::2]:
  print(i)

# 150번
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
  print(i)