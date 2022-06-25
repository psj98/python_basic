입출력
========

함수
----------
* 함수란?
    #### > 함수가 하는 일 : 입력값을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓는 것
<br>

* 함수를 사용하는 이유
    #### > 반복되는 부분이 있을 경우
    #### > 자신이 만든 프로그램을 함수화하면 프로그램 흐름을 일목요연하게 볼 수 있음
    #### > 프로그램 흐름도 잘 파악할 수 있고 오류가 어디에서 나는지도 바로 알 수 있음

<br>

* 함수의 구조
    #### > def : 함수 만들 때 사용하는 예약어
    #### > 매개변수 : 함수에 입력으로 전달되는 값을 받는 변수
    ```python
    def 함수명(매개변수):
        수행 문장1
        수행 문장2
    ```
    ```python
    def add(a, b):
        return a + b
    
    a = 3
    b = 4
    c = add(a, b)
    print(c) # 7
    ```

* 매개변수와 인수
    #### > 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수
    #### > 인수(arguments) : 함수를 호출할 때 전달하는 입력값
    
    ```python
    def add(a, b): # a, b는 매개변수
        return a + b
    
    print(add(3, 4)) # 3, 4는 인수
    ```

* 입력값과 결괏값에 따른 함수의 형태
    #### > 입력값 -> 함수 -> 결과값
  + 일반적인 함수 
    ```python
    def 함수이름(매개변수):
        수행할 문장
        return 결과값
    ```
    ```python
    def add(a, b): 
        result = a + b 
        return result
    
    a = add(3, 4) # a는 결과값
    print(a) # 7
    ```

  + 입력값이 없는 함수
    ```python
    def say():
        return 'Hi'
    
    a = say()
    print(a) # Hi
    ```
    
  + 결과값이 없는 함수
    ```python
    def add(a, b):
        print(f'{a} + {b} = {a+b}')

    add(3, 4) # 3 + 4 = 7
    ```

  + 입력값, 결과값 없는 함수
    ```python
    def say():
        print('Hi')
    
    say() # Hi
    ```

* 매개변수 지정하여 호출하기
    ```python
    def add(a, b):
        return a + b

    result = add(a = 3, b = 4)
    print(result) # 7
    ```
    ```python
    # 순서가 바뀌어도 상관 X
    result = add(b = 4, a = 3)
    print(result) # 7
    ```

* 입력값이 몇 개가 될지 모를 때?
    #### > 매개변수 앞에 별 한 개(*) 붙임
    ```python
    def 함수이름(*매개변수):
        수행 문장
    ```

    ```python
    def add_all(*args):
        result = 0
        for i in args:
            result += i
        return result

    result = add_all(1, 2, 3)
    print(result) # 6
    ```

    ```python
    def add_mul(choice, *args):
        if choice == 'add':
            result = 0
            for i in args:
                result += i
        elif choice == 'mul':
            result = 1
            for i in args:
                result *= i
        return result

    result = add_mul('add', 1, 2, 3, 4)
    print(result) # 10

    result = add_mul('mul', 1, 2, 3, 4)
    print(result) # 24
    ```

  + 키워드 파라미터 kwargs
    #### > 매개변수 앞에 별 두개(**) 붙임
    #### > 딕셔너리로 만들어져서 출력
    ```python
    def print_kwargs(**kwargs):
        print(kwargs)
        
    print_kwargs(a = 1) # {'a' : 1}
    print_kwargs(name = 'Kim', age = 20) # {'age':20, 'name':'Kim'}
    ```

* 함수의 결과값은 언제나 하나이다
    #### > 튜플 값 하나로 반환
    ```python
    def add_mul(a, b):
        return a + b, a * b

    result = add_mul(3, 4)
    print(result) # (7, 12)
    ```

    ```python
    result1, result2 = add_mul(3, 4)
    print(result1) # 7
    print(result2) # 12
    ```

    ```python
    # 안좋은 예시
    def add_mul(a, b):
        return a + b
        return a * b # 실행되지 X

    print(add_mul(3, 4)) # 7
    ```

  + return의 또 다른 쓰임새
    #### > return을 단독으로 써서 함수를 빠져나갈 수 있음
    ```python
    def say(talk):
        if talk == 'hi':
            return
        print(f'{talk}라고 말함')

    print('hi') # 
    print('bye') # bye라고 말함
    ```

* 매개변수 초기값 미리 설정하기
    #### > man = True 처럼 매개변수에 미리 값을 넣어주는 경우
    ```python
    def say_myself(name, old, man=True):
        print(f'이름 {name}, 나이 {old}')
        if man:
            print('남자')
        else:
            print('여자')
    
    say_myself('홍길동', 20) # 남자
    say_myself('홍길동', 20, True) # 남자

    say_myself('홍길동', 20, False) #여자
    ```
    
    #### > 초기값이 정해진 매개변수의 위치는 항상 마지막에 위치
    ```python
    def say_myself(name, man=True, old):
        # 이하 동일

    say_myself('홍길동', 20) # ERROR
    ```

* 함수 안에서 선언한 변수의 효력 범위
    #### > 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과 전혀 상관 X
    ```python
    a = 1
    def add(a):
        a += 1

    add(a)
    print(a) # 1 -> 결과값을 전달한 것이 아님
    ```

* 함수 안에서 함수 밖의 변수를 변경하는 방법
    + return 사용
        ```python
        a = 1
        def add(a):
            a += 1
            return a # 결과값 반환

        a = add(a)
        print(a)
        ```
    + global 명령어 사용
        #### > 함수 밖의 변수를 직접 사용
        #### > 사용하지 않는 것이 좋음 -> 함수는 독립적으로 존재하기 때문
        ```python
        a = 1
        def add():
            global a
            a += 1

        a = add(a)
        print(a)
        ```

* lambda
    #### > 보통 함수를 한줄로 간결하게 만들 때 사용 (def와 동일한 역할)
    ```python
    lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
    ```

    ```python
    add = lambda a, b: a+b
    result = add(3, 4)
    print(result) # 7
    ```
    ```python
    # 위와 동일한 함수
    def add(a, b):
        return a + b
    
    result = add(3, 4)
    print(result) # 7
    ```