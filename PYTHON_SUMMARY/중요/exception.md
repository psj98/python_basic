중요
========

예외 처리
----------
* 오류는 어떤 때 발생하는가?
    > 다양한 오류들

    ```py
    # FileNotFoundError - 없는 파일일 경우
    f = open('none.txt', 'r')
    ```

    ```py
    # ZeroDivisionError - 0으로 다른 숫자를 나누는 경우
    4 / 0
    ```

    ```py
    # IndexError - 리스트에서 얻을 수 없는 값일 경우
    a = [1, 2, 3]
    a[4]
    ```

<br>

* 오류 예외 처리 기법
    + try, except문
        > try 블록 수행 중 오류가 발생하면, except 블록 수행

        > try 블록에서 오류가 발생하지 않으면, except 블록 수행 X

        ```py
        try:
            ...

        # [] 안의 내용은 생략 가능
        except [발생 오류[as 오류 메시지 변수]]:
            ...
        ```
        
        1. try, except만 쓰는 방법
            ```py
            try:
                ...
            except:
                ...
            ```
            > 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행

        2. 발생 오류만 포함한 except문
            ```py
            try:
                ...
            except 발생 오류:
                ...
            ```
            > 오류가 발생했을 때, except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행

        3. 발생 오류와 오류 메시지 변수까지 포함한 except문
            ```py
            try:
                ...
            except 발생 오류 as 오류 메시지 변수:
                ...
            ``` 
            > 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법

            ```py
            try:
                4 / 0
            except ZeroDivisionError as e:
                print(e)

    + try ... finally
        > finally문은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행
        ```py
        f = open('a.txt', 'w')
        try:
            ...
        finally:
            f.close()
        ```

    + 여러 개의 오류 처리하기
        ```py
        try:
            ...
        except 발생오류1:
            ...
        except 발생오류2:
            ...
        ```

        ```py
        # ex) 따로 처리
        try:
            a = [1, 2]
            print(a[3])
            4 / 0
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
        except IndexError:
            print("인덱싱 할 수 없습니다.")
        ```
        > 먼저 발생한 오류만 출력


        ```py
        # ex) 한꺼번에 처리
        try:
            a = [1, 2]
            print(a[3])
            4 / 0
        except (ZeroDivisionError, IndexError) as e:
            print(e)
        ```

    + try문에 else절 사용
        ```py
        try:
            ...
        except [발생 오류[as 오류 메시지 변수]]:
            ...
        else: # 오류가 없을 경우 수행
            ...
        ```

        ```py
        # ex)
        try:
            age = int(input('나이 입력 : '))
        except:
            print('입력이 정확하지 않습니다.')
        else:
            if age <= 18:
                print('미성년자는 출입금지입니다.')
            else:
                print('환영합니다.')
        ```

<br>

* 오류 회피하기
    ```py
    try:
        f = open('none.txt', 'r')
    except FileNotFoundError:
        pass # 회피
    ```

<br>

* 오류 일부러 발생시키기
    > raise 명령어를 사용해 오류를 강제로 발생시킬 수 있음
    ```py
    # ex) Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현하도록 만들고 싶은 경우
    class Bird:
        def fly(self):
            raise NotImplementedError
    ```

    > 만약 자식 클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출하면
    ```py
    class Eagle(Bird):
        pass

    eagle = Eagle()
    eagle.fly() # ERROR
    ```
    
<br>

* 예외 만들기
    ```py
    class MyError(Exception):
        pass

    def say_nick(nick):
        if nick == '호':
            raise MyError()
        print(nick)

    say_nick('야')
    say_nick('호') # MyError 발생
    ```

    ```py
    try:
        say_nick("야")
        say_nick("호") # except 실행
    except MyError:
        print("허용되지 않는 별명입니다.")
    ```
    
    <br>
    
    > 오류 메시지를 사용하고 싶은 경우 : \_\_str\_\_ 메서드 구현
    ```py
    class MyError(Exception):
        def __str__(self):
            return "허용되지 않는 별명입니다."
    
    try:
        say_nick("야")
        say_nick("호") # except 실행
    except MyError as e:
        print(e)
    ```