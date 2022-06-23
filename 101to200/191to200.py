# 파이썬 반복문

# 191번
data = [[ 2000,  3050,  2050,  1980],
  [ 7500,  2050,  2050,  1980],
  [15450, 15050, 15550, 14900]]

for i in data:
  for j in i:
    print(j * 1.00014)

# 192번
data = [[ 2000,  3050,  2050,  1980],
  [ 7500,  2050,  2050,  1980],
  [15450, 15050, 15550, 14900]]

for i in data:
  for j in i:
    print(j * 1.00014)
  print('-' * 4)

# 193번
data = [[ 2000,  3050,  2050,  1980],
  [ 7500,  2050,  2050,  1980],
  [15450, 15050, 15550, 14900]]

result = [j * 1.00014 for i in data
          for j in i]
print(result)

# 194번
data = [[ 2000,  3050,  2050,  1980],
  [ 7500,  2050,  2050,  1980],
  [15450, 15050, 15550, 14900]]

result = []

for i in data:
  sub = []
  for j in i:
    sub.append(j * 1.00014)
  result.append(sub)
print(result)

# 195번
ohlc = [["open", "high", "low", "close"],
  [100, 110, 70, 100],
  [200, 210, 180, 190],
  [300, 310, 300, 310]]

for i in ohlc[1:]:
  print(i[3])

# 196번
ohlc = [["open", "high", "low", "close"],
  [100, 110, 70, 100],
  [200, 210, 180, 190],
  [300, 310, 300, 310]]

for i in ohlc[1:]:
  if i[3] > 150:
    print(i[3])

# 197번
ohlc = [["open", "high", "low", "close"],
  [100, 110, 70, 100],
  [200, 210, 180, 190],
  [300, 310, 300, 310]]

for i in ohlc[1:]:
  if i[3] >= i[0]:
    print(i[3])

# 198번
ohlc = [["open", "high", "low", "close"],
  [100, 110, 70, 100],
  [200, 210, 180, 190],
  [300, 310, 300, 310]]

volatility = [i[1] - i[2] for i in ohlc[1:]]
print(volatility)

# 199번
ohlc = [["open", "high", "low", "close"],
  [100, 110, 70, 100],
  [200, 210, 180, 190],
  [300, 310, 300, 310]]

for i in ohlc[1:]:
  if i[3] > i[0]:
    print(i[1] - i[2])

# 200번
ohlc = [["open", "high", "low", "close"],
  [100, 110, 70, 100],
  [200, 210, 180, 190],
  [300, 310, 300, 310]]

sum = 0
for i in ohlc[1:]:
  sum += i[0] - i[3]
print(sum)