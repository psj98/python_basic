자료형
========

집합
----------
#### 집합에 관련된 것을 쉽게 처리 -> set 키워드 사용
```python
# 빈 집합 자료형
s = set()
```
```python
s = set([1, 2, 3])
print(s) # {1, 2, 3}
```

* 특징
  + 중복 허용 X
    #### > 중복 제거하기 위한 필터로 사용
    ```python
    # 중복 값이 있는 경우, 하나만 들어감
    s = set("Hello")
    print(s) # {'e', 'H', 'l', 'o'}
    ```
  + 순서 X
    #### > 인덱싱으로 접근하려면 리스트나 튜플로 변환 후 해야함
    ```python
    # 리스트
    s = set([1, 2, 3])
    l = list(s)
    l # [1, 2, 3]
    l[0] # 1
    ```
    ```python
    # 튜플
    s = set([1, 2, 3])
    t = tuple(s)
    t # (1, 2, 3)
    t[0] # 1
    ```

* 교집합, 합집합, 차집합 구하기
  ```python
  # 예시 집합
  s1 = set([1, 2, 3, 4])
  s2 = set([3, 4, 5, 6])
  ```
  + 교집합
    #### > '&' 기호 사용
    ```python
    s1 & s2 # {3, 4}
    ```

    #### > intersection 함수 사용
    ```python
    s1.intersection(s2) # {3, 4}
    s2.intersection(s1) # 위와 동일
    ```

  + 합집합
    #### 중복 값은 한 개만 표현
    #### > '|' 기호 사용
    ```python
    s1 | s2 # {1, 2, 3, 4, 5, 6}
    ```

    #### > union 함수 사용
    ```python
    s1.union(s2) # {1, 2, 3, 4, 5, 6}
    s2.union(s1) # 위와 동일
    ```

  + 차집합
    #### > '-' 기호 사용
    ```python
    s1 - s2 # {1, 2}
    s2 - s1 # {5, 6}
    ```

    #### > difference 함수 사용
    ```python
    s1.difference(s2) # {1, 2}
    s2.difference(s1) # {5, 6}
    ```

* 집합 관련 함수
  + 값 1개 추가하기 (add)
    #### > 집합.add(값)
    ```python
    s = set([1, 2])
    s.add(3)
    s # {1, 2, 3}
    ```
  
  + 값 여러 개 추가하기 (update)
    #### > 집합.update(값)
    ```python
    s = set([1, 2])
    s.update([3, 4])
    s # {1, 2, 3, 4}
    ```
  
  + 특정 값 제거하기 (remove)
    #### > 집합.remove(값)
    ```python
    s = set([1, 2])
    s.remove(2)
    s # {1}
    ```