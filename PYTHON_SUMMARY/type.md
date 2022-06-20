자료형
========

숫자
----------
숫자형(Number) : 숫자 형태로 이루어진 자료형

* 정수형(Integer) : 정수를 뜻하는 자료형
  + ex) 123, -222, 0
  + 예시 코드
      ```python
      a = 123
      a = -222
      a = 0
      ```

* 실수형(Floating-point) : 소수점이 포함된 숫자
  + ex) 123.45, -111.11, 3.5e3
  + 예시 코드
    ```python
    a = 123.45
    a = -111.11
    a = 3.5e3 # E도 상관 X
    ```

* 8진수(Octal) : 숫자가 0o 또는 0O(숫자 0 + 알파벳 소문자 o 또는 대문자 O)로 시작
  + ex) 0o11, 0o22
  + 예시 코드
    ```python
    a = 0o11
    a = -0o22
    ```

* 16진수(Hexadecimal) : 숫자가 0x로 시작
  + ex) 0x1A, 0xF3
  + 예시 코드
    ```python
    a = 0x1A
    a = 0xF3
    ```

* 연산자
  + 사칙연산 (+, -, *, /)
  + 예시 코드
    ```python
    a = 3
    b = 4
    a + b # 7
    a * b # 12
    a / b # 0.75
    ```

  + 제곱 (**)
  + 예시 코드
    ```python
    a = 2
    b = 3
    a ** b # 8
    ```

  + 나머지 (%)
  + 예시 코드
    ```python
    7 % 3 # 1
    3 % 7 # 3
    ```

  + 몫 (//)
  + 예시 코드
    ```python
    7 // 4 # 1
    ```


문자열
----------
문자열(String) : 문자, 단어 등으로 구성된 문자들의 집합
```python
"Life is too short"
"PYTHON"
"123"
```

문자열 만드는 방법
* 큰따옴표(")
  ```python
  "PYTHON"
  ```
* 작은따옴표(')
  ```python
  'PYTHON'
  ```
* 큰따옴표 3개 연속(""")
  ```python
  """PYTHON"""
  ```
* 작은따옴표 3개 연속(''')
  ```python
  '''PYTHON'''
  ```

문자열 연산
* 문자열 연결
  ```python
  a = "a"
  b = "b"
  a + b # 'a b'
  ```
* 문자열 곱하기
  ```python
  a = "a"
  a * 2 # 'aa'
  ```
* 문자열 길이 구하기
  ```python
  a = "I like python"
  len(a) # 13
  ```

문자열 인덱싱과 슬라이싱
* 문자열 인덱싱(Indexing) : 가리킴
  ```python
  a = "python"
  a[0] # p
  a[4] # o
  a[-1] # n : 마지막 문자
  a[-3] # h : 뒤에서 세 번째 문자
  ```

* 문자열 슬라이싱(Slicing) : 잘라냄
  + 문자열 나누기
  + 마지막은 포함 X
  ```python
  a = 'python is best'
  a[0:5] # python : 0번째부터 5번째까지
  a[:] # 전체
  a[:-1] # python is bes
  ```

문자열 포맷팅(Formatting)
* % 포맷팅
  + %s : 문자열(String)
  + %c : 문자 1개(Character)
  + %d : 정수(Integer)
  + %f : 부동소수(Floating-point)
  + %o : 8진수
  + %x : 16진수
  + %% : Literal % (퍼센트 기호)
    ```python
    a = "python"
    b = 3
    "%s is best" % a # python is best
    "%d balls" % b # 3 balls
    "%d balls, %s" % (b, a) # 3 balls, python
    ```

  + 정렬과 공백
    ```python
    "%4s" % "hi" # '  hi' # 4칸 중 오른쪽 정렬 (나머지는 공백)
    "%-4s" % "hi" # 'hi  ' # 4칸 중 왼쪽 정렬 (나머지는 공백)
    ```

  + 소수점 표현
    #### > '.'은 소수점 포인트
    #### > '.' 뒤의 숫자는 표현할 소수점 자리수
    ```python
    "%0.2f" % 1.2345 # '1.23'
    "%6.2f" % 1.2345 # '  1.23'
    ```

* format 함수
  ```python
  a = "python"
  b = 3
  "{} is best".format(a) # python is best
  "{} balls, {}" % (b, a) # 3 balls, python
  ```
  + 왼쪽 정렬(:<)
    ```python
    "{:<10}".format("hi")
    ```
  + 오른쪽 정렬(:>)
    ```python
    "{:>10}".format("hi")
    ```
  + 가운데 정렬(:^)
    ```python
    "{:^10}".format("hi")
    ```
  + 공백 채우기
    ```python
    "{:!<10}".format("hi") # hi!!!!!!!!
    ```
  + 소수점 표현
    ```python
    "{:0.2f}".format(1.2345) # 1.23
    ```

* f 문자열 포매팅 : 파이썬 3.6 버전부터 가능
  ```python
  a = "python"
  b = 3
  f"{a} is best" # python is best
  f"{b} balls, {a}" # 3 balls, python
  ```
  + 왼쪽 정렬
    ```python
    f"{"hi":<10}"
    ```
  + 오른쪽 정렬
    ```python
    f"{"hi":>10}"
    ```
  + 가운데 정렬
    ```python
    f"{"hi":^10}"
    ```
  + 공백 채우기
    ```python
    f"{'hi':!<10}"
    ```
  + 소수점 표현
    ```python
    a = 1.2345
    f"{a:0.2f}" # 1.23
    ```

문자열 관련 함수
* 문자 개수 세기 (count)
  #### > 해당 문자가 나온 개수 반환
  ```python
  a = 'python'
  a.count('p') # 1
  ```
* 위치 알려주기 1 (find)
  #### > 처음 나온 문자 위치 반환
  #### > 찾는 문자가 없을 경우, -1 반환
  ```python
  a = 'python'
  a.find('y') # 1
  a.find('c') # -1
  ```
* 위치 알려주기 2 (index)
  #### > 처음 나온 문자 위치 반환
  #### > 찾는 문자가 없을 경우, ERROR
  ```python
  a = 'python'
  a.index('y') # 1
  a.index('c') # ERROR
  ```
* 문자열 삽입 (join)
  #### > 문자 사이에 삽입
  ```python
  a = 'best'
  a.join('!') # b!e!s!t
  ```
* 소문자를 대문자로 바꾸기 (upper)
  ```python
  a = 'python'
  a.upper() # PYTHON
  ```
* 대문자를 소문자로 바꾸기 (lower)
  ```python
  a = 'PYTHON'
  a.lower() # python
  ```
* 맨 앞 글자만 대문자로 바꾸기 (capitalize)
  ```python
  a = 'python'
  a.capitalize() # Python
  ```
* 왼쪽 공백 지우기 (lstrip)
  ```python
  a = ' python'
  a.lstrip() # python
  ```
* 오른쪽 공백 지우기 (rstrip)
  ```python
  a = 'python '
  a.rstrip() # python
  ```
* 양쪽 공백 지우기 (strip)
  ```python
  a = ' python '
  a.strip() # python
  ```
* 문자열 바꾸기 (replace)
  #### > replace(바뀌게 될 문자열, 바꿀 문자열)
  ```python
  a = 'python'
  a.replace('n', 'r') # pythor
  ```
* 문자열 나누기 (split)
  #### > split(나눌 문자)
  #### > 문자열을 나누면 리스트에 하나씩 들어감
  ```python
  a = 'python is best'
  a.split(' ') # ['python', 'is', 'best']
  ```


리스트
----------

튜플
----------

딕셔너리
----------

집합
----------

불
----------

