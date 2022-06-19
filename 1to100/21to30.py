# 파이썬 문자열

# 21번
letters = 'python'
print(letters[0], letters[2])

# 22번
license_plate = "24가 2210"
print(license_plate[-4:])

# 23번
string = "홀짝홀짝홀짝"
print(string[::2])

# 24번
string = "PYTHON"
print(string[::-1])

# 25번
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 26번
phone_number = "010-1111-2222"
print(phone_number.replace("-", ""))

# 27번
url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split[-1])

# 28번
lang = 'python'
lang[0] = 'P' # error
print(lang)

# 29번
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

# 30번
string = 'abcd'
string.replace('b', 'B')
print(string) # abcd