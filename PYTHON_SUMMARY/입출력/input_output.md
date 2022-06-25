입출력
========

사용자 입력과 출력
----------
* 사용자 입력
    + input의 사용
        ```python
        변수 = input()
        ```

    + 프롬프트를 띄워서 사용자 입력 받기
        #### > input()의 괄호 안에 질문을 입력하여 프롬프트를 띄움
        ```python
        변수 = input('질문 내용')
        ```
        ```python
        # ex
        num = input('숫자 입력')
        ```

        #### > input은 입력되는 모든 것을 문자열로 취급
        ```python
        type(num) # <class 'str'>
        ```

* print 자세히 알기
    + 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일
        ```python
        # 결과 : pythonbest
        print('python' 'best')
        print('python'+'best')
        ```
    + 문자열 띄어쓰기는 콤마로 함
        ```python
        print('python', 'best) # python best
        ```

    + 한 줄에 결과값 출력하기
        #### > 매개변수 end를 사용해 끝 문자를 지정
        ```python
        for i in range(5):
            print(i, end = ' ')
        # 0 1 2 3 4
        ```