제어문
========

If
----------
#### 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 사용
```python
money = True
if money:
    print("Taxi")
else:
    print("Walk")
# Result : Taxi
```

* if문의 기본 구조
    #### > 참일 경우, if문 바로 다음 문장들 수행
    #### > 거짓일 경우, else문 바로 다음 문장들 수행
    ```python
    if 조건문:
        수행 문장
    else 조건문:
        수행 문장
    ```

* 들여쓰기 (Indentation)
    #### > if 조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(indentation)를 해줘야 함
    ```python
    if 조건문:
        수행 문장1
        수행 문장2
    ```
    ```python
    # ERROR
    if 조건문:
        수행 문장1
        수행 문장2   # 들여쓰기 X
        수행 문장3
    ```

    #### > 같은 너비로 들여쓰기를 해야 함
    ```python
    # ERROR
    if 조건문:
        수행 문장1
        수행 문장2
            수행 문장3 # 같은 너비 X
    ```

* 조건문이란? : 참과 거짓을 판단하는 문장
    + 비교 연산자 (<, >, ==, !=, >=, <=)
        - x < y : x가 y보다 작다
        - x > y : x가 y보다 크다
        - x == y : x와 y가 같다
        - x != y : x와 y가 같지 않다
        - x >= y : x가 y보다 크거나 같다
        - x <= y : x가 y보다 작거나 같다
            ```python
            x = 3
            y = 2
            x < y # False
            x > y # True
            x == y # False
            x != y # True
            x >= y # True
            x <= y # False
            ```
            ```python
            # ex)
            money = 1000
            if money >= 2000:
                print('Taxi')
            else:
                print('Walk')
            # Result : Walk
            ```

    + and, or, not
        -  x or y : x와 y 둘중에 하나만 참이어도 참이다
        -  x and y : x와 y 모두 참이어야 참이다
        -  not x : x가 거짓이면 참이다
        ```python
        money = 1000
        card = True
        if money >= 2000 or card:
            print('Taxi')
        else:
            print('Walk')
        # Result : Taxi
        ``` 

    + x in s, x not in s
        - x in 리스트 : x not in 리스트
        - x in 튜플 : x not in 튜플
        - x in 문자열 : x not in 문자열
        ```python
        1 in [1, 2] # True
        1 not in [1, 2] # False
        ``` 
        ```python
        'a' in ('a', 'b') # True
        ```
        ```python
        'a' not in 'python' # True
        ```
        ```python
        pocket = ['money', 'cellphone']
        if 'money' in pocket:
            print('Taxi')
        else:
            print('Walk')
        # Result : Taxi
        ```

    + pass
      #### > 아무런 일도 하지 않음
        ```python
        pocket = ['money', 'cellphone']
        if 'money' in pocket:
            pass
        else:
            print('Walk')
        ```

* 다양한 조건을 판단하는 elif
  #### > 이전 조건문이 거짓일 때 수행 (개수 제한 X)
    ```python
    if 조건문:
        수행 문장1 
        수행 문장2
    elif 조건문:
        수행 문장1
        수행 문장2
    elif 조건문:
        수행 문장1
        수행 문장2
    else:
        수행 문장1
        수행 문장2
    ```

* 조건부 표현식 (Conditional Expression)
    ```python
    조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
    ```
    ```python
    if score >= 60:
        message = 'A'
    else:
        message = 'B'
    ```
    ```python
    # 조건부 표현식 사용
    message = 'A' if score >= 60 else 'B'
    ```