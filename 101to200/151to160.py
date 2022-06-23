# 파이썬 반복문

# 151번
리스트 = [3, -20, -3, 44]
for i in 리스트:
  if i < 0:
    print(i)

# 152번
리스트 = [3, 100, 23, 44]
for i in 리스트:
  if i % 3 == 0:
    print(i)

# 153번
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
  if i % 3 == 0 and i < 20:
    print(i)

# 154번
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
  if len(i) >= 3:
    print(i)

# 155번
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
  if i.isupper():
    print(i)

# 156번
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
  if i.islower():
    print(i)

# 157번
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
  print(i.capitalize())

# 158번
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
  print(i.split('.')[0])

# 159번
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
  if i.split('.')[1] == 'h':
    print(i)

# 160번
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
  if i.split('.')[1] == 'h' or i.split('.')[1] == 'c':
    print(i)