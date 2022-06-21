# 파이썬 딕셔너리

# 81번
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a) # 0
print(b) # 1
print(c) # [2, 3, 4, 5] : *을 사용한 언패킹

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

# 82번
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

# 83번
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores
print(valid_score)

# 84번
temp = {}

# 85번
icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(icecream)

# 86번
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream)

# 87번
print('메로나 가격 :', icecream['메로나'])

# 88번
icecream['메로나'] = 1300
print(icecream)

# 89번
del icecream['메로나']
print(icecream)

# 90번
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바'] # Key 값에 '누가바'가 없음