# 1번
sen = "a:b:c:d"
a = sen.split(':')
result = "#".join(a)
print(result)

# 2번
a = {'A':90, 'B':80}
print(a.get('C', 70))

# 3번
# + : 두 리스트가 더해진 새로운 리스트가 반환 -> 주소 변경
# extend : 주소 변경되지 않음

# 4번
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0

for i in A:
  if i >= 50:
    sum += i

print(sum)

# 5번
def fibonacci(num):
  if num == 0:
    return 0

  if num == 1:
    return 1

  return fibonacci(num - 2) + fibonacci(num - 1)

for i in range(10):
  print(fibonacci(i))

# 6번
num = list(map(int, input('숫자 입력 : ').split(',')))
sum = 0

for i in num:
    sum += i

print(sum)

# 7번
dan = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))

for i in range(1, 10):
    print(dan * i, end = ' ')

# 8번
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines = lines.reverse()

f = open('abc.txt', 'w')
for i in lines:
    i = i.strip()
    f.write(i + '\n')
f.close()

# 9번
f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

sum = 0
for i in lines:
    sum += int(i)

avg = sum / len(lines)

f = open('sample.txt', 'w')
f.write(str(avg))
f.close()

# 10번
class Calculator():
    def __init__(self, li):
        self.li = li

    def sum(self):
        total = 0
        for i in self.li:
            total += i

        return total

    def avg(self):
        return self.sum() / len(self.li)

cal1 = Calculator([1,2,3,4,5]) 
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10]) 
print(cal2.sum())
print(cal2.avg())