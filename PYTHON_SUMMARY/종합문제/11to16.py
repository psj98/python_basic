# 11번
# 생략

# 12번
# [1, 2, 3][3] 에서 IndexError가 발생
# -> result += 3 
# -> finally문으로 이동하여 result += 4
# 결과 : 7

# 13번
def DashInsert(num):
  to_int = list(map(int, num)) # int형으로 리스트에 각각 저장
  result = []

  for i in range(len(to_int) - 1):
    result.append(str(to_int[i]))

    # 짝수인 경우
    if to_int[i] % 2 == 0 and to_int[i + 1] % 2 == 0:
      result.append('*')

    # 홀수인 경우
    elif to_int[i] % 2 == 1 and to_int[i + 1] % 2 == 1:
      result.append('-')

  result.append(str(to_int[-1])) # 마지막 숫자 추가

  return "".join(result)
  
print(DashInsert('4546793'))

# 14번
def compress(sen):
  before = '' # 이전 단어
  result = '' # 결과
  count = 0 # 같은 단어 개수

  for i in sen:
    # 이전 단어와 다르면
    if before != i:
      before = i
      if count != 0:
        result += str(count) # 단어 개수 추가
      result += i
      count = 1

    # 이전 단어와 같으면 단어 개수 +1
    else:
      count += 1

  # 마지막 단어 개수 추가
  if count != 0:
    result += str(count)

  return result

print(compress("aaabbcccccca"))  # a3b2c6a1 출력

# 15번
def checkDupNum(num):
  result = [] # 리스트에 숫자를 넣어서 판단
  for i in num:
    if i not in result:
      result.append(i)
    else:
      return False

  return len(result) == 10  

print(checkDupNum("0123456789"))   # True 리턴
print(checkDupNum("01234"))        # False 리턴
print(checkDupNum("01234567890"))  # False 리턴
print(checkDupNum("6789012345"))   # True 리턴
print(checkDupNum("012322456789")) # False 리턴

# 16번
morseDic = {
  '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
  '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
  '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
  '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
  '-.--':'Y','--..':'Z'
}

def decodeMorse(sen):
  result = []
  
  for i in sen.split("  "): # 공백 두 개 단위로 나눔
    for j in i.split(" "):
      result.append(morseDic[j])
    result.append(' ')

  return "".join(result)

print(decodeMorse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))