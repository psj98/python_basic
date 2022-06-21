자료형
========

불
----------
#### 참(True)과 거짓(False)을 나타내는 자료형
```python
a = True
b = False
```

#### 조건문의 반환 값으로도 사용
```python
1 == 1 # True
1 > 2 # False
```

* 자료형의 참(True)과 거짓(False)
  #### > 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있는 경우 False
  ```python
  "python" # True
  "" # False
  [1, 2] # True
  [] # False
  () # False
  {} # False
  1 # True
  0 # False
  None # False
  ```

* 불 연산
  #### > bool 내장 함수
  ```python
  bool('python') # True
  bool('') # False
  ```