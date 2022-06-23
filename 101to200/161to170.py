# 파이썬 반복문

# 161번
for i in range(100):
  print(i)

# 162번
for i in range(2002, 2051, 4):
  print(i)

# 163번
for i in range(3, 31, 3):
  print(i)

# 164번
for i in range(99, -1, -1):
  print(i)

# 165번
for i in range(10):
  print(i/10)

# 166번
for i in range(1, 10):
  print('3 * {} = {}'.format(i, 3 * i))

# 167번
for i in range(1, 10):
  if i%2 == 1:
    print('3 * {} = {}'.format(i, 3 * i))

# 168번
sum = 0
for i in range(1, 11):
  sum += i
print(sum)

# 169번
sum = 0
for i in range(1, 11, 2):
  sum += i
print(sum)

# 170번
sum = 1
for i in range(1, 11):
  sum *= i
print(sum)