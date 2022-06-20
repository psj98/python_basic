자료형 
========

리스트 (List)
----------
* 리스트 만들기
  ```python
  리스트명 = [요소1, 요소2, 요소3, ...]
  ```
  ```python
  nothing = []
  num = [1, 2, 3, 4, 5]
  language = ['C', 'C++', 'python']
  doub_li = [1, 2, ['python', 'C++']]
  ```

* 리스트의 인덱싱과 슬라이싱
  + 리스트의 인덱싱 (Indexing)
    ```python
    num = [1, 2, 3, 4, 5]
    num # [1, 2, 3, 4, 5]
    num[0] # 1
    num[0] + num[2] # 4
    num[-1] # 5
    ```
    ```python
    doub_li = [1, 2, ['python', 'C++']]
    doub_li[0] # 1
    doub_li[-1] # ['python', 'C++']
    doub_li[-1][0] # python
    ```

  + 리스트의 인덱싱 (Indexing)
    ```python
    리스트[시작:끝] # 끝은 포함 X
    ```
    ```python
    num = [1, 2, 3, 4, 5]
    num[0:2] # [1, 2]
    num[:2] # [1, 2]
    num[2:] # [3, 4, 5]
    ```

* 리스트 연산
  + 리스트 더하기 (+)
    ```python
    a = [1, 2]
    b = [3, 4]
    a + b # [1, 2, 3, 4]
    ```

  + 리스트 반복하기 (*)
    ```python
    a = [1, 2]
    a * 2 # [1, 2, 1, 2]
    ```

  + 리스트 길이 구하기 (len)
    ```python
    a = [1, 2]
    len(a) # 2
    ```

  + 유의사항
    #### > 같은 type 끼리 연산 가능
    ```python
    a = [1, 2, 3]
    a[2] + "hi" # ERROR -> 형 변경 str(a[2])
    ```

* 리스트의 수정과 삭제
  + 값 수정
    ```python
    a = [1, 2, 3]
    a[2] = 4
    a # [1, 2, 4]
    ```

  + 값 삭제
    #### > Python이 자체적으로 가지고 있는 함수
    ```python
    del 객체
    ```
    ```python
    a = [1, 2, 3]
    del a[1]
    a # [1, 3]

    b = [1, 2, 3, 4, 5]
    del b[2:]
    b # [1, 2]
    ```

* 리스트 관련 함수
  + 리스트에 요소 추가 (append)
    #### > append(x) : 리스트의 맨 마지막에 x를 추가하는 함수
    ```python
    a = [1, 2, 3]
    a.append(4)
    a # [1, 2, 3, 4]
    ```

  + 리스트 정렬 (sort)
    #### > 리스트의 요소를 순서대로 정렬
    ```python
    a = [3, 1, 2]
    a.sort()
    a # [1, 2, 3]
    ```

  + 리스트 뒤집기 (reverse)
    #### > 현재의 리스트를 그대로 거꾸로 뒤집음 (역순 정렬 X)
    ```python
    a = [3, 1, 2]
    a.reverse()
    a # [2, 1, 3]
    ```

  + 위치 반환 (index)
    #### > index(x) : 리스트에 x값이 있으면 x의 위치 값 반환
    ```python
    a = [1, 2, 3]
    a.index(1) # 0
    a.index(0) # ERROR (존재하지 않는 값)
    ```

  + 리스트에 요소 삽입 (insert)
    #### > insert(a, b) : 리스트의 a번째 위치에 b 삽입
    ```python
    a = [1, 2, 3]
    a.insert(3, 4)
    a # [1, 2, 3, 4]
    ```

  + 리스트 요소 제거 (remove)
    #### > remove(x) : 리스트에서 첫 번째로 나오는 x 삭제
    ```python
    a = [1, 2, 3]
    a.remove(3)
    a # [1, 2]
    ```

  + 리스트 요소 끄집어내기 (pop)
    #### > pop() : 리스트의 맨 마지막 요소를 돌려주고 그 요소 삭제
    ```python
    a = [1, 2, 3]
    a.pop() # 3 (맨 마지막 요소)
    a # [1, 2]
    ```

    #### > pop(x) : 리스트의 x번째 요소를 돌려주고 그 요소 삭제
    ```python
    a = [1, 2, 3]
    a.pop(1) # 2
    a # [1, 3]
    ```

  + 리스트에 포함된 요소 x의 개수 세기 (count)
    #### > count(x) : 리스트 안에 x의 개수 반환
    ```python
    a = [1, 2, 3, 1]
    a.count(1) # 2
    ```

  + 리스트 확장 (extend)
    #### > extend(x) : x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더함
    ```python
    a = [1, 2, 3]
    a.extend([4, 5]) # a += [4, 5]와 동일
    a # [1, 2, 3, 4, 5]
    
    b = [6, 7]
    a.extend(b)
    a # [1, 2, 3, 4, 5, 6, 7]
    ```