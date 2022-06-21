자료형
========

딕셔너리
----------
#### Key와 Value를 한 쌍으로 갖는 자료형
```python
# Key에는 변하지 않는 값
# Value에는 변하는 값과 변하지 않는 값 모두 사용
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```
```python
# ex)
dic = {'name':'Kim', 'phone':'01012345678', 'birth': '010101'}
```
```python
# Value에 리스트 넣을 수 있음
a = {'a': [1, 2, 3]}
```

* 딕셔너리 쌍 추가, 삭제
  + 딕셔너리 쌍 추가하기
    ```python
    a = {1:'a'}
    a[2] = 'b' # Key : 2, Value : 'b'
    a # {1:'a', 2:'b'}
    ```

  + 딕셔너리 삭제하기
    ```python
    a = {1:'a', 2:'b'}
    del a[1] # Key : 1, Value : 'a'
    a # {2:'b'}
    ```

* 딕셔너리 사용 방법
  + Key로 Value 얻기
    #### > 딕셔너리_변수_이름[Key] 사용
    ```python
    a = {1:'a', 2:'b'}
    a[1] # 'a'
    a[2] # 'b'
    ```

  + 딕셔너리 주의 사항
    #### > Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지는 모두 무시
    ```python
    a = {1:'a', 1:'b'}
    a # {1:'b'} : Key값인 1이 중복되므로 {1:'a'} 값은 무시
    ```

    #### > Key에 리스트 사용 불가 -> 리스트는 값이 변할 수 있기 때문
    ```python
    a = {[1, 2]:'hi'}
    ```
    
* 딕셔너리 관련 함수
  + Key 리스트 만들기 (keys)
    ```python
    dic = {'name':'Kim', 'phone':'01012345678', 'birth': '010101'}
    dic.keys() # dict_keys(['name', 'phone', 'birth'])
    ```
    ```python
    # 리스트로 바꿀 경우
    list(dic.keys()) # ['name', 'phone', 'birth']
    ```
    ```python
    # 반복문을 사용한 Key 값 출력
    for k in dic.keys():
      print(k) # name \n phone \n birth
    ```

  + Value 리스트 만들기 (values)
    ```python
    dic = {'name':'Kim', 'phone':'01012345678', 'birth': '010101'}
    dic.values() # dict_values(['Kim', '01012345678', '010101'])
    ```
    
  + Key, Value 쌍 얻기 (items)
    #### > Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 반환
    ```python
    dic = {'name':'Kim', 'phone':'01012345678', 'birth': '010101'}
    dic.items()
    ```
    
  + Key: Value 쌍 모두 지우기 (clear)
    #### > 딕셔너리 안의 모든 요소 삭제
    ```python
    dic = {'name':'Kim', 'phone':'01012345678', 'birth': '010101'}
    dic.clear() # {}
    ```
    
  + Key로 Value얻기 (get)
    ```python
    dic = {'name':'Kim', 'phone':'01012345678', 'birth': '010101'}
    dic.get('name') # Kim
    dic.get('a') # None

    dic['a'] # ERROR
    ```
    #### > get(x, 'default') : 딕셔너리 안에 찾으려는 Key 값이 없을 경우 'default' 값 반환
    ```python
    dic.get('a', 'aaa') # aaa
    ```
    
  + 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)
    ```python
    dic = {'name':'Kim', 'phone':'01012345678', 'birth': '010101'}
    print('name' in dic) # True
    print('a' in dic) # False
    ```
    
  + update 메서드
    #### > 딕셔너리에 딕셔너리를 추가하는 메서드
    ```python
    a = {1:'a', 2:'b'}
    c = {3:'c', 4:'d'}
    a.update(c)
    print(a) # {1:'a', 2:'b', 3:'c', 4:'d'}
    ```

  + zip
    #### > Key와 Value로 변환 -> dict(zip(Key 값, Value 값))
    ```python
    # 튜플
    keys = (1, 2)
    vals = ('a', 'b')
    result = dict(zip(keys, vals))
    print(result) # {1:'a', 2:'b'}
    ```
    ```python
    # 리스트
    keys = [1, 2]
    vals = ['a', 'b']
    result = dict(zip(keys, vals))
    print(result) # {1:'a', 2:'b'}
    ```