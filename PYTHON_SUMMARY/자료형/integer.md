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
    ```python
    a = 3
    b = 4
    a + b # 7
    a - b # -1
    a * b # 12
    a / b # 0.75
    ```

  + 제곱 (**)
    ```python
    a = 2
    b = 3
    a ** b # 8
    ```

  + 나머지 (%)
    ```python
    7 % 3 # 1
    3 % 7 # 3
    ```

  + 몫 (//)
    ```python
    7 // 4 # 1
    ```