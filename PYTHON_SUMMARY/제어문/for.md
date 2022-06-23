제어문
========

For
----------
* for문의 기본 구조
    #### > 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입
    ```python
    for 변수 in 리스트(또는 튜플, 문자열):
        수행 문장1
        수행 문장2
    ```

* 예제
  + 리스트 
    ```python
    test = ['one', 'two', 'three']
    for i in test:
        print(i)
    # one
    # two
    # three
    ```

  + 튜플
    ```python
    a = [(1, 2), (3, 4)]
    for (first, last) in a:
        print(first + last)
    # 3
    # 7
    ```

* for문과 continue
    ```python
    # 60점 이하인 학생일 경우, continue문에 의해 print문을 수행하지 않고 for문의 처음으로 돌아감
    score = [90, 25, 67, 45, 80]

    number = 0 
    for mark in score: 
        number = number +1 
        if mark <= 60:
            continue 
        print(f"{number}번 학생 축하합니다. 합격입니다.")
    ```

* for문과 자주 사용하는 range 함수
    ```python
    # 끝 숫자는 포함 X
    range(시작 숫자, 끝 숫자)
    ```
    ```python
    a = range(10)
    a # range(0, 10) : 0부터 10미만의 숫자를 포함하는 range 객체 생성 
    ```

    + 예시
        ```python
        sum = 0 
        for i in range(1, 11): 
            sum += i
        print(sum) # 55
        ```

        ```python
        # 구구단
        for i in range(2, 10) # 1번 for문
            for j in range(1, 10): # 2번 for문
                print(i * j, end=" ") 
            print('')
        ```

* 리스트 내포 사용하기
    ```python
    [표현식 for 항목 in 반복가능객체 if 조건문]
    ```

    ```python
    # 원래 코드
    a = [1, 2, 3, 4]
    result = []
    for num in a:
        result.append(num * 3)
    print(result) # [3, 6, 9, 12]
    ```

    ```python
    # 리스트 내포 사용
    a = [1, 2, 3, 4]
    result = [num * 3 for num in a]
    print(result) # [3, 6, 9, 12]
    ```

    ```python
    # 리스트 내포 + if문 사용
    a = [1, 2, 3, 4]
    result = [num * 3 for num in a if num % 2 == 0]
    print(result) # [6, 12]
    ```

    ```python
    # 여러 개의 for문
    [표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        for 항목n in 반복가능객체n if 조건문n]
    ```

    ```python
    # 구구단 표현
    result = [x * y for x in range(2, 10)
        for y in range(1, 10)]
    print(result) # [2, 4, 6, 8, 10, 12, ... , 81]
    ```