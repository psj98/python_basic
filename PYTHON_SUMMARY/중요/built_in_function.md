중요
========

내장 함수
----------
* abs
    > abs(x) : 숫자의 절댓값을 돌려주는 함수
    ```py
    abs(5) # 5
    abs(-5) # 5
    abs(-1.5) # 1.5
    ```

<br>

* all
    > all(x) : 반복 가능한 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 반환
        >> True : 0을 제외한 나머지 / 빈 값
        >> False : 0이 있는 경우
    ```py
    all([1, 2, 3]) # True
    all([1, 2, 3, 0]) # False거짓이므로
    all([]) # True
    ```

<br>

* any
    > any(x) : 반복 가능한 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True, x가 모두 거짓일 경우 False를 반환
        >> True : 하나라도 참일 경우
        >> False : 모두 거짓인 경우 / 빈 값

    > all(x)의 반대

    ```py
    any([1, 2, 3, 0]) # True
    any([0, '']) # False
    any([]) # False
    ```

<br>

* chr
    > chr(x) : 유니코드(Unicode) 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수

    ```py
    chr(97) # a
    chr(44032) # 가
    ```

<br>

* dir
    > dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌

    ```py
    dir([1, 2, 3]) # ['append', 'count', 'extend', 'index', ...]
    dir({'1':'a'}) # ['clear', 'copy', 'get', 'has_key', ...]
    ```

<br>

* divmod
    > divmod(a, b) : 2개의 숫자를 입력으로 받음

    > a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
        >> ex) (몫, 나머지)

    ```py
    divmod(7, 3) # (2, 1)
    ```

<br>

* enumerate
    > enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 반환

    ```py
    for i, name in enumerate(['body', 'foo', 'bar']):
        print(i, name)
    
    # 0 body
    # 1 foo
    # 2 bar
    ```

<br>

* eval
    > eval(expression) : 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과를 반환

    ```py
    eval('1 + 2') # 3
    eval("'hi' + 'a'") # 'hia'
    eval('divmod(4, 3)') # (1, 1)
    ```

<br>

* filter
    > filter(a, b) : a에는 함수 이름, b에는 a에 차례로 들어갈 반복 가능한 자료형
    
    > 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 **반환 값이 참**인 것만 묶어서 반환

    ```py
    # ex)
    def positive(l): 
        result = [] 
        for i in l: 
            if i > 0: 
                result.append(i) 
        return result

    print(positive([1, -3, 2, 0, -5, 6])) # [1, 2, 6]
    ```

    ```py
    def positive(x):
        return x > 0 # 반환 값이 참인 것 반환

    print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
    ```

    ```py
    # lambda 사용
    list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
    ```

<br>

* hex
    > hex(x) : 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수

    ```py
    hex(234) # '0xea'
    hex(3) # '0x3'
    ```

<br>

* id
    > id(object) : 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수

    ```py
    a = 3
    id(3) # 135072304
    id(a) # 135072304

    b = a
    id(b) # 135072304
    ```

<br>

* input
    > input([prompt]) : 사용자 입력을 받는 함수

    > 매개변수로 문자열을 주면 그 문자열은 프롬프트가 됨

    ```py
    a = input() # hi
    a # 'hi'

    b = input("Enter: ") # Enter: hi
    b # 'hi'
    ```

<br>

* int
    > int(x) : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
    
    > 정수를 입력으로 받으면 그대로 반환

    ```py
    int('3') # 3
    int(3.4) # 3
    ```

    <br>
    
    > int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환하여 반환

    ```py
    # 2진수
    int('11', 2) # 3

    # 16진수
    int('1A', 16) # 26
    ```

<br>

* isinstance
    > isinstance(object, class) : 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받음
    
    > 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False 반환

    ```py
    class Person:
        pass
    
    a = Person()
    isinstance(a, Person) # True

    b = 3
    isinstance(b, Person) # False
    ```

<br>

* len
    > len(s) : 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수

    ```py
    len("python") # 6
    len([1, 2, 3]) # 3
    len((1, 'a')) # 2
    ```

<br>

* list
    > list(s) : 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수

    ```py
    list("python") # ['p', 'y', 't', 'h', 'o', 'n']
    list((1, 2, 3)) # [1, 2, 3]
    ```

    > list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 반환
    ```py
    a = [1, 2, 3]
    b = list(a)
    b # [1, 2, 3]
    ```

<br>

* map
    > map(function, iterable) : 함수와 반복 가능한 자료형을 입력으로 받음
    
    > 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수

    ```py
    # ex)
    def two_times(numberList):
        result = []
        for number in numberList:
            result.append(number * 2)
        return result

    result = two_times([1, 2, 3, 4])
    print(result) # [2, 4, 6, 8]
    ```

    ```py
    def two_times(x): 
        return x * 2
    
    list(map(two_times, [1, 2, 3, 4])) # [2, 4, 6, 8]
    ```

    ```py
    # lambda 사용
    list(map(lambda x: x * 2, [1, 2, 3, 4])) # [2, 4, 6, 8]
    ```

<br>

* max
    > max(iterable) : 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수

    ```py
    max([1, 2, 3]) # 3
    max("python") # 'y'
    ```

<br>

* min
    > min(iterable) : max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수

    ```py
    min([1, 2, 3]) # 1
    min("python") # 'h'
    ```

<br>

* oct
    > oct(x) : 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수

    ```py
    oct(34) # '0o42'
    oct(12345) # '0o30071'
    ```

<br>

* open
    > open(filename, [mode]) : "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수
    
    > 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 반환

    <br>

    + w : 쓰기 모드로 파일 열기
    + r : 일기 모드로 파일 열기
    + a : 추가 모드로 파일 열기
    + b : 바이너리 모드로 파일 열기

        ```py
        # b는 w, r, a와 함께 사용
        f = open("binary_file", "rb") # 바이너리 읽기 모드
        ```

        ```py
        # 동일한 방법
        fread = open("read_mode.txt", 'r')
        fread2 = open("read_mode.txt")
        ```

        ```py
        # 추가 모드
        fappend = open("append_mode.txt", 'a')
        ```

<br>

* ord
    > ord(c) : 문자의 유니코드 값을 돌려주는 함수

    > chr 함수와 반대

    ```py
    ord('a') # 97
    ord('가') # 44032
    ```

<br>

* pow
    > pow(x, y) : x의 y 제곱한 결과 반환

    ```py
    pow(2, 4) # 16
    pow(3, 3) # 27
    ```

<br>

* range
    > range([start,] stop [,step]) : for문과 함께 자주 사용하는 함수
    
    > 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환

    + 인수가 1개일 경우
        > 시작 숫자를 지정하지 않으면 0부터 시작
        ```py
        list(range(5)) # [0, 1, 2, 3, 4]
        ```

    + 인수가 2개일 경우
        > 시작 숫자와 끝 숫자 지정.
        
        > 단 끝 숫자는 해당 범위에 포함 X
        ```py
        list(range(5, 10)) # [5, 6, 7, 8, 9]
        ```

    + 인수가 3개일 경우
        > 숫자 사이의 거리
        ```py
        list(range(1, 10, 2)) # [1, 3, 5, 7, 9]
        list(range(0, -10, -1)) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
        ```

<br>

* round
    > round(number[, ndigits]) : 숫자를 입력받아 반올림해 주는 함수

    ```py
    round(4.6) # 5
    round(4.2) # 4
    ```

    ```py
    # ex) 소수점 2자리까지만 반올림
    round(5.678, 2) # 5.68
    ```

<br>

* sorted
    > sorted(iterable) : 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수

    ```py
    sorted([3, 1, 2]) # [1, 2, 3]
    sorted(['a', 'c', 'b']) # ['a', 'b', 'c']
    sorted("zero") # ['e', 'o', 'r', 'z']
    ```

<br>

* str
    > str(object) : 문자열 형태로 객체를 변환하여 돌려주는 함수

    ```py
    str(3) # '3'
    str('hi') # 'hi'
    ```

<br>

* sum
    > sum(iterable) : 입력 받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수

    ```py
    sum([1, 2, 3]) # 6
    sum((4, 5, 6)) # 15
    ```

<br>

* tuple
    > tuple(iterable) : 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수
    
    > 만약 튜플이 입력으로 들어오면 그대로 반환

    ```py
    tuple("abc") # ('a', 'b', 'c')
    tuple([1, 2, 3]) # (1, 2, 3)
    tuple((1, 2, 3)) # (1, 2, 3)
    ```

<br>

* type
    > type(object) : 입력값의 자료형이 무엇인지 알려 주는 함수

    ```py
    type("abc") # <class 'str'>
    type([]) # <class 'list'>
    type(open("test", 'w')) # <class '_io.TextIOWrapper'>
    ```

<br>

* zip
    > zip(*iterable) : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수

    ```py
    list(zip([1, 2, 3], [4, 5, 6])) # [(1, 4), (2, 5), (3, 6)]
    list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    list(zip("abc", "def")) # [('a', 'd'), ('b', 'e'), ('c', 'f')]
    ```