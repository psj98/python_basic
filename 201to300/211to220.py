# 파이썬 함수

# 211번
# 안녕
# Hi

# 212번
# 7
# 15

# 213번
# 파라미터가 입력되지 않음

# 214번
# 같은 타입의 값이 입력되지 않음

# 215번
def print_with_smile(a):
    print(a + ':D')

# 216번
print_with_smile('안녕하세요')

# 217번
def print_upper_price(price):
    print(price * 1.3)

# 218번
def print_sum(a, b):
    print(a + b)

# 219번
def print_arithmetic_operation(a, b):
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b}')

# 220번
def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)


def print_max2(a, b, c):
    print_max2(a, b, c)